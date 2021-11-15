...
from googleapiclient import discovery
from oauth2client.client import OAuth2Credentials as creds
crm = discovery.build(
    'cloudresourcemanager', 'v3', http=creds.authorize(httplib2.Http()))

operation = crm.projects().create(
body={
    'project_id': flags.projectId,
    'name': 'projeto_dataproc_dio'
}).execute()


$ gcloud services enable compute.googleapis.com
$ gcloud services enable dataproc.googleapis.com

gsutil mb gs://renatsperanca321
gsutil cp C:\Users\Eu\OneDrive\Área de Trabalho\DIO - Data Engeneer\0b97b8c7-507b-4bcf-87a4-1b93c0f677d2\dio-desafio-dataproc-main/livro.txt gs://renatsperanca321/
gsutil cp C:\Users\Eu\OneDrive\Área de Trabalho\DIO - Data Engeneer\0b97b8c7-507b-4bcf-87a4-1b93c0f677d2\dio-desafio-dataproc-main/contador.py gs://renatsperanca321/


gcloud dataproc clusters create desafio_dataproc --region=us-central1
--enable=component-gateway
--optional-components=JUPYTER, ZEPPELIN, ZOOKEEPER /
--num-workers=3 /

import re


from google.cloud import dataproc_v1 as dataproc
from google.cloud import storage


glcoud dataproc jobs submit spark \
--cluster=desafio_dataproc
--region="us-central1"
--

def submit_job(desafio-dio, us-central1, renatsperanca321):
    # Create the job client.
    job_client = dataproc.JobControllerClient(
        client_options={"api_endpoint": "{}-dataproc.googleapis.com:443".format(region)}
    )

    # Create the job config. 'main_jar_file_uri' can also be a
    # Google Cloud Storage URL.
    job = {
        "placement": {"cluster_name": desafio_dataproc},
        "spark_job": {
            "main_class": "org.apache.spark.examples.SparkPi",
            "jar_file_uris": ["file:///usr/lib/spark/examples/jars/spark-examples.jar"],
            "args": ["1000"],
        },
    }

    operation = job_client.submit_job_as_operation(
        request={"project_id": desafio-dio, "region": us-central1, "job": job}
    )
    response = operation.result()

    # Dataproc job output gets saved to the Google Cloud Storage bucket
    # allocated to the job. Use a regex to obtain the bucket and blob info.
    matches = re.match("gs://(.*?)/(.*)", response.driver_output_resource_uri)

    output = (
        storage.Client()
        .get_bucket(matches.group(1))
        .blob(f"{matches.group(2)}.000000000")
        .download_as_string()
    )

    print(f"Job finished successfully: {output}")





...