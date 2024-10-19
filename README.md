# End-to-end-Machine-Learning-Project-with-MLflow
This is a basic learning end-to-end MLOPs project involving tools like MLflow, Docker, AWS, Flask, and CI/CD with GitHub actions.


<!-- 
## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py
 -->

 ## Prerequisites

Make sure you have the following installed:

- **Python**: `>=3.11`
- **Git**: To clone the repository
- **Poetry**: Dependency manager (details on installation below)


## Installation

### Clone the repository
```bash
git clone https://github.com/ArtemStrashko/end_to_end_mlops_project
cd end_to_end_mlops_project
```

### Poetry Installation
To install Poetry, use the following command in your terminal:

```bash
# This command downloads and installs the latest version of Poetry
# It uses Python to run the installation script
curl -sSL https://install.python-poetry.org | python3 -

# After installation, make sure Poetry is accessible from your PATH
# You can check the installation with:
poetry --version

# Poetry will automatically create a virtual environment and install dependencies
poetry install

# This activates the virtual environment for running project commands
poetry shell
```


## Running the app locally
```bash
# If you're inside the Poetry shell, run the app with:
python app.py

# If you're not using the Poetry shell, prefix commands with `poetry run`:
poetry run python app.py
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)

### dagshub
[dagshub](https://dagshub.com/)

For setting up MLFLOW_TRACKING_URI, MLFLOW_TRACKING_USERNAME and MLFLOW_TRACKING_USERNAME, it is recommended to put them into an untracked `.env` file, install `python-dotenv` and then use the following code wherever needed:
```
from dotenv import load_dotenv
import os

if os.path.exists(".env"):
    load_dotenv()  # Load environment variables from .env if available
    print("Loaded .env file for local development")
    
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
os.environ.get("MLFLOW_TRACKING_USERNAME")
os.environ.get("MLFLOW_TRACKING_PASSWORD")
``` 

If you are using CI/CD pipelines, such as GitHub Actions or GitLab CI, you can store the MLFLOW_TRACKING_PASSWORD and MLFLOW_TRACKING_USERNAME as secrets and access them in your CI/CD pipeline. See `.github/workflows/main.yaml` for details.



# AWS CICD Deployment with GitHub Actions

## 1. Login to AWS console.

## 2. Creat IAM user for deployment.

Attach the following policies directly: `AmazonEC2ContainerRegistryFullAccess` and `AmazonEC2FullAccess`, create and download access key (CLI), which will contain `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

## 3. ECR (Elastic Container Registry) setup.

Create a private repository and copy its name, which will be your `ECR_REPOSITORY_NAME`. In my case it is `408292891334.dkr.ecr.us-east-1.amazonaws.com/mlproj`.

## 4. Create EC2 instance.

Select `Ubuntu`, pick up not a very big machine, e.g., `t2.large`, create a new key pair (RSA, `.pem`), tick `Allow SSH traffic ...`, `Allow HTTPS traffic ...`, `Allow HTTP traffic ...`, add a but more memory for storage, e.g., 32GB. 

## 5. VS code and ssh to EC2.

In VSCode hit `shift  command  p` (for Mac users) and choose `Remote-SSH: Open SSH Configuration File`, which is usually located in `.ssh/config` and modify it accordingly. It should look like this:
```
Host 1.23.456.789
  HostName 1.23.456.789
  User ubuntu
  IdentityFile ~/.ssh/your_aws_key.pem
```

After that, hit `shift  command  p` and choose `Remote-SSH: Conect to Host`.


## 6. Open EC2 and Install docker in EC2 Machine.
	
```
	sudo apt-get update -y

	sudo apt-get upgrade
	
	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
```
	
## 7. Configure EC2 as self-hosted runner.
    setting>actions>runner>new self hosted runner> choose os> then run command one by one on the EC2 instance. 


## 8. Setup github secrets:

    AWS_ACCESS_KEY_ID=
    AWS_SECRET_ACCESS_KEY=
    AWS_REGION = 
    AWS_ECR_LOGIN_URI = 
    ECR_REPOSITORY_NAME = 
	MLFLOW_TRACKING_URI = 
	MLFLOW_TRACKING_USERNAME = 
	MLFLOW_TRACKING_PASSWORD = 

## 9. Push the code to GitHub.

Pushing code to GitHub will activate CI/CD workflow. 


# Using deployed app.

Once the project has been deployed with GitHub CI/CD, go the AWS EC2 manager, select your EC2 instance, select Security Groups, then click Edit inbound rules, click on add rule. Keep it Custup TCP add port `8080` and select `ip 0.0.0.0/0` and click on save rules. Now you can copy EC2 instance public ip and past it in your browser. The app is ready to be used.

## More detailed info about the contents of this repo.