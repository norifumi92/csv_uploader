###Install Python 3.7###
#Use SCL
sudo yum -y install centos-release-scl;
sudo yum -y install rh-python36;
sudo scl enable rh-python36 bash;
#Set rh-python36 into PATH
sudo echo 'check if root directory of python3 exists in PATH'
if [ "`echo $PATH | grep "rh-python36"`" ]; then echo "FOUND"; else echo "export PATH="/opt/rh/rh-python36/root/bin:/usr/bin:/usr/sbin"" >> ~/.bash_profile; fi
source ~/.bash_profile

##To check file location, run `which [package name]`
##PATH is set as `/usr/bin` by default. To change the setting, edit ~/.bash_profile

# Install MySQL
#sudo yum -y install http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
#sudo yum -y install mysql-community-server

#Install Postgresql
sudo yum -y install postgresql-devel;

#Install wget
sudo yum -y install wget;

##upgrade yum
sudo yum -y upgrade;
#Install sqlite 3.29
if [ "`sqlite3 --version | grep "3.7"`" ]; then 
	wget https://www.sqlite.org/2019/sqlite-autoconf-3290000.tar.gz
	tar xvfz sqlite-autoconf-3290000.tar.gz
	rm -f *.tar.gz*
	cd sqlite-autoconf-3290000
	./configure --prefix=/usr/local
	make
	sudo make install
	sudo mv /usr/bin/sqlite3 /usr/bin/sqlite3_old
	sudo ln -s /usr/local/bin/sqlite3 /usr/bin/sqlite3
	echo "export LD_LIBRARY_PATH="/usr/local/lib"" >> ~/.bashshrc;	
fi
#Load sqlite 3.29
source ~/.bashshrc;

#Install GCC
sudo yum -y install gcc;
#Install Extra Packages for Enterprise Linux since lentos does not recognise pip by default
sudo yum -y install epel-release;
#Install Pip
sudo yum -y install python-pip;
sudo yum -y install python-virtualenv;
#Start MySQL when vagrant is up
#sudo systemctl enable mysqld.service
#sudo systemctl start mysqld.service