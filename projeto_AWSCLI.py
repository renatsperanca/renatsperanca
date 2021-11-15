aws s3api create-bucket --bucket dio-datalake --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1
aws s3api put-object --bucket dio-datalake --key data/
aws s3 cp C:\Users\Eu\OneDrive\Área de Trabalho\DIO - Data Engeneer\1e1d5efe-8823-4a17-8d50-9b584c037541\DIO-LiveCoding-AWS-BigData-master\sherlock.txt s3://dio-datalake/data/
aws s3api put-object --bucket dio-datalake --key output/
aws s3api put-object --bucket dio-datalake --key temp/
aws ec2 create-key-pair --key-name dio-live-key-prod --query 'KeyMaterial' --output text > dio-live-key-prod.pem
aws ec2 describe-key-pairs --key-name dio-live-key-prod
aws iam create-access-key --user-name renatsperanca

#powershell
virtualenv --python=python3.6 venv_diolive_prod
source venv_diolive_prod/bin/activate
nano -/.mrjob.conf
#alterar as chaves de acesso para dio-live-key-prod / arquivo pem tbm
pip install boto3
pip instal mrjob

python3 dio-live-wordcount-test.py -r emr s3://dio-datalake/data/sherlock.txt --output-dir=s3://dio-datalake/output/logs1 --cloud-tmp-dir=s3://dio-datalake/temp/

#pythonfile sdk aws

import boto3
import json
import time

# Create the amscm client
cm = boto3.client('amscm')

# Define the execution parameters for EC2 Create
AMSExecParams = {
    "Description": "EC2-Create",
    "VpcId": "VPC_ID",
    "Name": "My-EC2",
    "TimeoutInMinutes": 60,
    "Parameters": {
        "InstanceAmiId": "INSTANCE_ID",
        "InstanceSubnetId": "SUBNET_ID"
    }
}

# Create the AMS RFC
cts = cm.create_rfc(
    ChangeTypeId="ct-14027q0sjyt1h",
    ChangeTypeVersion="3.0",
    Title="Python Code RFC Create",
    ExecutionParameters=json.dumps(AMSExecParams)
)

# Extract the RFC ID from the response
NewRfcID = cts['RfcId']

# Submit the RFC
RFC_Submit_Return=cm.submit_rfc(RfcId=NewRfcID)

# Check the RFC status every 30 seconds
RFC_Status = cm.get_rfc(RfcId=NewRfcID)
RFC_Status_Code = RFC_Status['Rfc']['Status']['Name']

while RFC_Status_Code != "Success":
    if RFC_Status_Code == "PendingApproval":
        print(RFC_Status_Code)
        time.sleep(30)
    elif RFC_Status_Code == "InProgress":
        print(RFC_Status_Code)
        time.sleep(30)
    elif RFC_Status_Code == "Failure":
        print(RFC_Status_Code)
        break
    else:
        print(RFC_Status_Code)

    RFC_Status = cm.get_rfc(RfcId=NewRfcID)
    RFC_Status_Code = RFC_Status['Rfc']['Status']['Name']


    