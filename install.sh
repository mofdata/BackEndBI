# Create virutal environment


# Install python dependencies
pip install -r requirements.txt

# Install nginx
sudo yum install nginx -y 
sudo systemctl stop nginx

# Copy nginx configration
sudo cp nginx.conf /etc/nginx/conf.d/default.conf

# Start nginx
sudo systemctl start nginx

# Install supervisor
sudo yum install supervisor -y

# Create configuration file. 
echo_supervisord_conf > /etc/supervisord.conf

# Start supervisord. 
sudo systemctl start supervisord.service

# Copy configuration of supervisor.
sudo cp supervisor.conf  /etc/supervisord.d/supervisor.conf 

#Echo 
echo "Uncomment files directory in supervisord.conf file under /etc/ directory" 

# Run gunicorn 
source start.sh

