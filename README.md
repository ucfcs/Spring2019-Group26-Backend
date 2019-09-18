# Spring2019-Group26-Backend
This repository holds the REST API for Group 26's ASL Tutor as well as the admin web portal.

## Requirements
* Python 3.7+
* Vagrant
* Virtual Box
* Docker

## Install
Install virtual box and vagrant

Make a directory and clone the repo into it

---
# Running the server

For all methods requests will be directed to `http://localhost:1337/`

## Build/Start the vagrant box and login
From the terminal `cd` into the project root (you should see a `Vagrantfile`) then run the following commands:

```bash
vagrant up
vagrant ssh
```

## To run a local sever for testing frontend and server deployment
From the terminal run the following commands:
```bash
cd ~/Spring2019-Group26-Backend
chmod +x deploy.sh
./deploy.sh
```
The deploy script will seem like it is hanging, there 40 seconds wait to make sure
mongo is started

If you make changes and they do not automatically take affect run:
```bash
sudo systemctl restart asltutor
```

## To run the server for backend development
From the terminal run the following commands:
```bash
cd ~/Spring2019-Group26-Backend
chmod +x setupenv.sh
./setupenv.sh
```
This sets up the virtual environment, starts mongo and adds the systemd config for
asltutor

To start the server you have 3 options:
1. with python3: this run using python without uWSGI and outputs logs to the console
If you choose this method
From the terminal run the following commands:
```bash
cd ~/Spring2019-Group26-Backend
chmod +x runpydev.sh
./runpydev.sh
```

2. with uWSGI:
The first time run the following commands:
```bash
cd ~/Spring2019-Group26-Backend
chmod +x runuwsgi.sh
./runuwsgi.sh
```

After the first time running it using uwsgi control it using systemd
- To stop:
```bash
sudo systemctl stop asltutor
```
- To start:
```bash
sudo systemctl start asltutor
```
- To restart:
```bash
sudo systemctl restart asltutor
```
- To check status run respectively:
```bash
sudo systemctl status mongod
sudo systemctl status asltutor
```

3. Follow the commands for front end to test deployment and operation\
    **<span style="color:red">Always test using the deployment script before making a PR</span>**
---
# Troubleshooting errors
If you are getting an internal server error or you can hit `hello world` but nothing else   the most likely cause is mongo has not been started or was not running before asltutor started

## To start diagnosing the problem we start by checking mongo
Run the following command to check if mongo is running:
```bash
sudo systemctl status mongod
```
If it is running without errors skip to the part about asltutor

If it is not running run the following command to start it
```bash
sudo systemctl start mongod
```
Then wait 30 seconds to a minute and check the status again.
```bash
sudo systemctl status mongod
```
If it is running without errors move on to the part about asltutor

If it is running but has errors you can try running the following commands:
```bash
sudo systemctl restart mongod
```
Then wait 30 seconds to a minute and check the status again.
```bash
sudo systemctl status mongod
```
If it still has errors try to google them or rebuild you vagrant machine:
```bash
exit
vagrant halt
vagrant destroy -y
vagrant up
```
After you have verified that mongo is working correctly now check asltutor
Run the following command to check to see if it is running:
```bash
sudo systemctl status asltutor
```
If it is not running run:
```bash
sudo systemctl start asltutor
```
If it is running run:
```bash
sudo systemctl restart asltutor
```
If this does not fix the problem try to google errors and check logs
uWSGI logs are located in
request logs: `/tmp/reqlog`
error logs: `/tmp/errlog`

While developing, for changes in the backend code to be reflected in the app you will have to restart the app
```bash
sudo systemctl restart asltutor
```

[Not yet enabled] To launch the integration tests, use tox:

```bash
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t app .

# starting up a container
docker run -p 5000:1337 app
```
