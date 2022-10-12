docker build -t flask-app . 
sudo docker run -it -p 5000:5000 -d flask-app  
docker containers ls 