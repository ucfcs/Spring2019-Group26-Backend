# TODO: test install script for vegrant

sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip -y
sudo apt install python3-dev -y
sudo apt install build-essential -y
sudo apt install libssl-dev -y
sudo apt install libffi-dev -y
sudo apt install python3-setuptools -y
sudo apt install python3-venv -y
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
