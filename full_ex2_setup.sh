#Install Python 2.7, as root:
sudo yum install python27-devel –y
mv /usr/bin/python /usr/bin/python266
ln -s /usr/bin/python2.7 /usr/bin/python

#Install streamparse and create EX2Tweetwordcount topology, as root:
cd exercise_2_repo
sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
sudo python ez_setup.py
sudo /usr/bin/easy_install-2.7 pip
sudo pip install virtualenv
wget --directory-prefix=/usr/bin/ https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
chmod a+x /usr/bin/lein
sudo /usr/bin/lein

lein version
pip install streamparse

#Use EasyButton setup


#clone exercise_2 repo directory, as root:
git clone https://github.com/eperkins1/exercise_2.git
