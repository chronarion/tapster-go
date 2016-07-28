# Install deps
sudo apt-get install build-essential cmake git pkg-config
sudo apt-get update
sudo apt-get install libzmq3-dev
sudo apt-get install python-pip
sudo apt-get install python-dev #so that you can compile zerorpc
sudo pip install zerorpc

# Install not old nodejs
curl -sL https://deb.nodesource.com/setup_6.x | bash -
apt-get install -y nodejs

# install node package
cd software
npm install

# opencv
sudo apt-get install libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev
#sudo apt-get install libgtk2.0-dev # optional
#sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev # video only
sudo apt-get install libatlas-base-dev gfortran
pip install numpy

wget https://raw.githubusercontent.com/milq/scripts-ubuntu-debian/master/install-opencv.sh
bash install-opencv.sh
