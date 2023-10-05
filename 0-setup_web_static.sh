#!/usr/bin/env bash
# Setup for web servers for the deployment of web_static

if ! command -v nginx &>/dev/null; then
    sudo apt-get update
    sudo apt-get install nginx -y
    sudo ufw allow 'Nginx HTTP'
fi
folders=("/data/" "/data/web_static/" "/data/web_static/releases/" "/data/web_static/shared/"
"/data/web_static/releases/test/")

for folder in "${folders[@]}"; do
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
    fi
done

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

link_target="/data/web_static/releases/test/"
link_name="/data/web_static/current"

if [ -L "$link_name" ]; then
    rm -f "$link_name"
fi
ln -s "$link_target" "$link_name"
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/^[^#]*server_name.*;$/a \ \n\t\tlocation \/hbnb_static/ {\n\t\t\t\talias /data/web_static/current/;\n\t\t}' /etc/nginx/sites-available/default
sudo service nginx start
sudo nginx -s reload
