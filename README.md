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

From the terminal 'cd' into the project root (you should see a `Vagrantfile`) then run the following commands:

```bash
vagrant up
vagrant ssh
```

## To run the server

From the terminal 'cd' into the project Spring2019-Group26 and run the following commands:
```bash
sudo systemctl start mongod
cd ~/Spring2019-Group26-Backend
chmod +x deploy.sh
./deploy.sh
```
If you make changes and they do not automatically take affect run:
```bash
./deploy.sh
```


You can confirm everything is running with running with:
```bash
sudo systemctl status mongod
sudo systemctl status asltutor
```

If either is not running make sure mongo is up before starting or restarting asltutor
To start
```bash
sudo systemctl start mongod
sudo systemctl start asltutor
```

or restart
```bash
sudo systemctl restart mongod
sudo systemctl restart asltutor
```

Requests will be directed to `http://localhost:1337/`

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
