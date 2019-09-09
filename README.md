## Spring2019-Group26-Backend
ASL Tutor project for senior design group 26

## Requirements
Python 3.0+

## Usage
Recommend using virtualenv to manage your environment:
```
python3 -m venv venv
source myenv/bin/activate
```

To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m app
```

requests will be directed to here:

```
http://localhost:1337/
```

[Not yet enabled] To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Vagrant

If running with Vagrant be sure to enable port forwarding in your Vagrantfile like so:
```
config.vm.network "forwarded_port", guest: 5000, host: 1337, host_ip: "127.0.0.1"
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t app .

# starting up a container
docker run -p 5000:1337 app
```
