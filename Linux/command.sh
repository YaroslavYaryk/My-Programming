cd /etc/
sudo echo """nameserver 8.8.8.8  
nameserver 8.8.4.4
options edns0 trust-ad
search .
"""  >> resolv.conf 

