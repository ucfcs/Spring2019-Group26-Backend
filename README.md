## Spring2019-Group26-Backend
ASL Tutor project for senior design group 26

## Requirements
Python 3.0+

## Install
Install virtual box and vagrant

Make a directory and clone the repo into it

From the terminal 'cd' into the project root (you should see a `Vagrantfile`) then run the following commands:

```bash
vagrant up
vagrant ssh
```

Install virtualenv to manage your environment:

```bash
python3 -m venv venv
source myenv/bin/activate
```

To run the server, please execute the following from the project root directory:

```bash
pip3 install -r requirements.txt
python3 -m app
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
