# TODO: add checks to verify commands

cd ~/Spring2019-Group26-Backend/src/asltutor
rm -rf venv
python3 -m venv venv
source venv/bin/activate
cd ..
pip install -r requirements.txt
python setup.py develop
deactivate
sudo rm /etc/systemd/system/asltutor.service
sudo cp asltutor.service /etc/systemd/system/asltutor.service
sudo systemctl start asltutor
sudo systemctl enable asltutor
sudo ufw allow 5000
