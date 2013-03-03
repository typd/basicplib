set -e
rm -rf tmp
mkdir tmp
cd tmp
git clone https://github.com/typd/basicplib.git
cd basicplib
./install.sh
cd ..
cd ..
sudo rm -rf tmp
