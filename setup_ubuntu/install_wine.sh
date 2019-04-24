pswd=${1}
echo ${pswd} | sudo -S dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key
echo ${pswd} | sudo -S apt-key add winehq.key
#cosmic - 18.10
#xenial - 16.04
echo ${pswd} | sudo -S apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ xenial main'
echo ${pswd} | sudo -S apt update
echo ${pswd} | sudo -S apt install --install-recommends winehq-stable
winecfg