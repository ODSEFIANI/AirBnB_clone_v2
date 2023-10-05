#!/usr/bin/env bash
# configure server to deploy web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/{releases/test,shared,current}
page="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
echo "$page" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
str="\\\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "35i $str" /etc/nginx/sites-available/default
sudo service nginx restart
