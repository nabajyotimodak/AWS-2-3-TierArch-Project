### TO START ###

import json
import boto3
import logging
region = 'us-east-1'
instance1 = ('testnotebookinstance')
instance2 = ('Test-Notebook-Instance')
instance3 = ("Name-of-the-Instance-as-per-the-Console")
from datetime import datetime as dt
notebook_client = boto3.client('sagemaker' , region_name=region)
client = boto3.client('sagemaker' , region_name=region)

def lambda_handler(event, context):

    if dt.now().hour + 1 ==8:       #This is 8am WAT. You can adjust to your preference
        notebook_client.start_notebook_instance(NotebookInstanceName=instance1)
        notebook_client.start_notebook_instance(NotebookInstanceName=instance2)
        # notebook_client.stop_notebook_instance(NotebookInstanceName="Name-of-the-Instance")
        # notebook_client.delete_notebook_instance(NotebookInstanceName="Name-of-the-Instance")
        print(dt.now().hour + 1)
        print("Notebook Instances have been Started")




#### TO STOP ALL RUNNING/INSERVICE INSTANCES IN GENERAL ####
    if dt.now().hour + 1 ==19:      #This is 7pm WAT. You can adjust to your preference
        response_nb_list = notebook_client.list_notebook_instances(StatusEquals= 'InService') #retrieves a list of notebooks that are running
        for nb in response_nb_list['NotebookInstances']:
            notebook_client.stop_notebook_instance(NotebookInstanceName=nb['NotebookInstanceName'])     #stop all notebooks in service at exactly 7pm
            # notebook_client.delete_notebook_instance(NotebookInstanceName=nb['NotebookInstanceName'])   # To delete instances
            print(dt.now().hour)
            print('stopped your instances!')





### TO STOP AND DELETE ###

import json
import boto3
import logging
region = 'us-east-1'
instance1 = ('testnotebookinstance')
instance2 = ('Test-Notebook-Instance')
from datetime import datetime as dt
notebook_client = boto3.client('sagemaker' , region_name=region)

def lambda_handler(event, context):
    # if dt.now().hour + 1 ==19: #This is 7pm WAT. You can adjust to your preference
        response_nb_list = notebook_client.list_notebook_instances(StatusEquals= 'InService') #retrieves a list of notebooks that are running
        for nb in response_nb_list['NotebookInstances']:
            notebook_client.stop_notebook_instance(NotebookInstanceName=nb['NotebookInstanceName']) #stop all notebooks in service at exactly 7pm
            # notebook_client.delete_notebook_instance(NotebookInstanceName=nb['NotebookInstanceName'])
            #print(dt.now().hour)
            print('stopped your instances!')







