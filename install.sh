set -e
rm -rf tmp
mkdir tmp
cd tmp
git clone https://github.com/typd/basicplib.git
sudo python basicplib/setup.py install
cd ..
rm -rf tmp
