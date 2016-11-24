if [ -f /etc/nginx/sites-enabled/default ]; then
sudo rm /etc/nginx/sites-enabled/default
fi

sudo ln -sf /home/nicolas/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

