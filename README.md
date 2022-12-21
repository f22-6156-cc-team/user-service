# User-Microservice

## Introduction

This is a simple Flask based user microservice.

Demo: [Video Recording](https://youtu.be/IW4IQe46KFg), [Presentation Slides](https://docs.google.com/presentation/d/1HG4Q6YdYU-IPsPstCrpNPSzbTTi_HwuTJENlMxSjNfc/edit?usp=sharing)


## Environment Setup
### Local Environment
- PyCharm Professional is suggested to be installed.
- Also, please make sure that your system has already installed:
  - Python (3.9 or greater)
  - MySQL Community Server
- Open the project in PyCharm and create a new virtual environment for the project.
- In the root of the directory, run ```pip install -r requirements.txt``` to install the necessary Python requirements.
- Connecting to database:
  - Go to ```./application.py``` and right click to ```More Run/Debug > Modify Run Configuration```.
  - Set the environment variables ```DBUSER=<dbusername>;DBPW=<dbpassword>;DBHOST=localhost;DBNAME=user_service;SECRET_KEY=694ccc6b3fe51e399b581d78654ff6229bcac52305119def3ade27bd1152f534```.

### AWS EC2 Environment
- Go to the created EC2 instance ```Userservice``` and connect to the console
- Run ```sudo yum update``` to update all the packages
- Run ```sudo yum install git```to install git
- ```git clone https://github.com/f22-6156-cc-team/user-service.git``` to the EC2 instance
- Run ```pip3 install -r requirements.txt``` to install necessary Python requirements.
- Connecting to database deployed in RDS instance:
  - Run ```export DBUSER="<dbusername>" DBPW="<dbpassword>" DBHOST="database-1.cpkam03owo3l.us-east-1.rds.amazonaws.com" DBNAME="user_service" SECRET_KEY="694ccc6b3fe51e399b581d78654ff6229bcac52305119def3ade27bd1152f534"``` to set environment variables

## Setting Up the Database
### Local MySQL Server
- Create a new schema named ```user_service```
- Right click the schema and go to ```Run SQL script```
- Select ```./sql/config.sql```

### AWS RDS instance
- Create a new MySQL datasource
- Set the host name to be ```database-1.cpkam03owo3l.us-east-1.rds.amazonaws.com``` (or any other instances you created) and port ```3306```
- Set the user and password to be your username and password
- Then follow the steps in ```Local MySQL Server```

## Executing the Program
### Local
- Run ```./application.py```
- Run ```./test_application.py``` and use the displayed message to verify if the end-to-end test worked
- Play around with APIs using Postman

### AWS EC2
- Run ```nohup python3 application.py &``` so that the application keeps running in the background even after logout
- Calling the APIs by pointing to ```http://54.175.182.198:5011```
- If you want to shut it down:
  - Find the process id by ```ps x```
  - Kill the job by id ```kill <pid>```
