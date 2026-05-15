echo "building app1 image with dockerfile"
docker build -t app1:latest .
echo "done building image, now starting containers using docker compose"
docker compose up -d
echo "started all the services"