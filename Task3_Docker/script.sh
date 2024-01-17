#!/bin/bash
sudo apt-get install python3
sudo pip install git

#Create dockerfile
touch dockerfile
echo "FROM httpd:2.4" >> dockerfile
echo "COPY files/index.html /usr/local/apache2/htdocs/" >> dockerfile

#build and run the container
echo "dockerfile has been built"
docker pull httpd
docker build -t dockerimagevitaltyrsu .
docker run -dit --name containervitaltyrsu -p 8080:80 dockerimagevitaltyrsu

#sleep for 7 sec to let build the container
sleep 7
curl localhost:8080

#VitalTyrsu