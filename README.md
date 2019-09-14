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
cd /vagrant
```

## To run the server

From the terminal 'cd' into the project Spring2019-Group26 and run the following commands:
```bash
chmod +x deploy.sh
./deploy.sh
```
If you make changes and they do not automatically take affect run:
```bash
./deploy.sh
```

The `deploy.sh` does not install MongoDB at this time. Run the following to install MongoDB:
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```

Start MongoDB with:
```bash
sudo service mongod start
```

You can confirm it's running with:
```bash
sudo service mongod status
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
