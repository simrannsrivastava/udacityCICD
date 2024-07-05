[![Python application test with Github actions](https://github.com/simrannsrivastava/udacityCICD/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/simrannsrivastava/udacityCICD/actions/workflows/pythonapp.yml)
# Overview

For this project, we will do CI/CD with Github Actions and Azure Pipeline. I have set up the Azure Pipelines to deploy the Flask ML Service Project to Azure App Service.

## Project Plan
1. A Trello Board (https://trello.com/invite/b/kuDhnMIa/ATTI0c5e057312e2c7f9bbfa7dcfc7a86622171E4479/building-ci-cd-pipeline-udacity) for tracking tickets in the project.
2. A Spreadsheet (https://docs.google.com/spreadsheets/d/1heqqlP7qrt7Sa0xwsOovOV-XoL3yavBUnWw3Ex_ohZQ/edit?usp=sharing) for managing project timeline.

## Instructions

![image](https://github.com/simrannsrivastava/udacityCICD/assets/54073955/e3c89e5f-1935-420b-b6f0-9537c0ed025f)

### Set up Azure cloud shell

1. Acess to Azure Portal Page and open Azure Cloud Shell
2. Generate ssh keys by running "ssh-keygen -t rsa cmd
3. Copy the value of the ssh-keys by running the cat cmd
4. Navigate to SSH and GPH keys and upload the ssh key generated.
<img width="1440" alt="image" src="https://github.com/simrannsrivastava/udacityCICD/assets/54073955/e4c8300b-d7eb-4604-854e-52a16cf77d28">

### Clone the repo into Azure Cloud Shell
1. After adding the SSH keys to GitHub, run the cmd below in Azure cloud shell to clone the project:
   git clone <"git repo using ssh">
![image](https://github.com/simrannsrivastava/udacityCICD/assets/54073955/eb6bf9b6-dfba-462a-9136-cb93cb2153da)

 
### Run Makefile
1. Set up virtual env:
   python3 -m venv ~/.flask-ml-sevice
   source ~/.flask-ml-service/bin/activate
2. Run make install cmd to install all the files, run pylint and pytest
   ![image](https://github.com/simrannsrivastava/udacityCICD/assets/54073955/47f4a75a-6f07-4b46-a9ed-d38d63069ea0)

### Deploy to Azure App Service
1. Run az webapp up -n flask-ml-service --resource-group Azuredevops to deploy the project to Azure app service.
2. After deployment is sucessful, we can see the following page:
   <img width="1440" alt="image" src="https://github.com/simrannsrivastava/udacityCICD/assets/54073955/0539f063-75a4-4381-aa84-4395e5605c87">

### Test REun Using Github Actions
1. Output of the test run on Github actions
   <img width="1440" alt="image" src="https://github.com/simrannsrivastava/udacityCICD/assets/54073955/d2bab446-3006-4683-af70-01ca380478d0">

### Set up Azure Pipelines
1. Create an azure devops project and connect to azure.
2. Use CI/CD to deploy a python web app to azure app service on linux.
3. Run the Azure pipeline and output after deploying sucessfully.
<img width="1440" alt="image" src="https://github.com/simrannsrivastava/udacityCICD/assets/54073955/4e0967b2-36b2-4db0-ac20-9d0df551e1a0">
4. The logs can be seen too.
![image](https://github.com/simrannsrivastava/udacityCICD/assets/54073955/726fab54-473a-4c12-bd6e-4fe7f27a0bc1)

5. Run ./make_predict_azure_app.sh cmd to test the predict API and output looks like this:
<img width="1440" alt="image" src="https://github.com/simrannsrivastava/udacityCICD/assets/54073955/95ae59c6-776f-4175-bd8a-3cb80f69594f">

### Locust load test
<img width="1440" alt="image" src="https://github.com/simrannsrivastava/udacityCICD/assets/54073955/403cccc2-9f1a-40d9-8ebb-abd39493a042">

## Enhancements
1. Remove code not used.

## Demo 
Link: https://youtu.be/tbn-Y8nSLkc


