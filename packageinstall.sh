#Install pip packages
sudo echo "start installing pip packages..."
sudo /opt/rh/rh-python36/root/usr/bin/pip install --upgrade pip
sudo /opt/rh/rh-python36/root/usr/bin/pip install psycopg2-binary
sudo /opt/rh/rh-python36/root/usr/bin/pip install requests
sudo /opt/rh/rh-python36/root/usr/bin/pip install Django
sudo /opt/rh/rh-python36/root/usr/bin/pip install django-toolbelt
sudo /opt/rh/rh-python36/root/usr/bin/pip install django-heroku
sudo echo "Pip installation done!"
/opt/rh/rh-python36/root/usr/bin/pip freeze > /vagrant/requirements.txt