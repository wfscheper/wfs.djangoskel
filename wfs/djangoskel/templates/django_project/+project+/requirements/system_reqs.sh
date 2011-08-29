#!/bin/bash
add-apt-repository ppa:nginx/stable
add-apt-repository ppa:bchesneau/gunicorn
apt-get update 
apt-get install nginx gunicorn
