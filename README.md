# User-Microservice

## Introduction

This is a simple Flask based user microservice.


## Environment Setup

- PyCharm Professional is suggested to be installed.
- Also, please make sure that your system has already installed:
  - Python (3.9 or greater)
  - MySQL Community Server
- Open the project in PyCharm and create a new virtual environment for the project.
- In the root of the directory, execute the command ```pip install -r requirements.txt```. This should install the necessary Python requirements.

## Connecting to the Database
### Connecting to Local MySQL Server
- Go to ```./application.py``` and right click to ```More Run/Debug > Modify Run Configuration```. 
- Set the environment variables ```DBUSER=<dbusername>;DBPW=<dbpassword>;DBHOST=localhost;DBNAME=<dbname>```.

### Connecting to Remote Database Host
(TODO)

## Executing the Program

- Run ```./application.py```
- Run ```./test_application.py``` and use the displayed message to verify if the end-to-end test worked
- Play around with APIs using Postman
