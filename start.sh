# Activate virtualenv

cd ..
source venv/bin/activate
cd - 


# Start nginx
sudo systemctl start nginx

# start supervisor
sudo systemctl stop supervisord.service 

# Start supervisor
sudo systemctl start supervisord.service 

# Reread the configuration
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl add bi

# Start mof services
sudo supervisorctl start bi

# see status
sudo supervisorctl status bi

