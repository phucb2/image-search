wget https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz -O /tmp/102flowers.tgz
mkdir -p data
tar -xvf /tmp/102flowers.tgz > /dev/null

podman run -p 9000:9000 -p 9001:9001 \
  quay.io/minio/minio server /data --console-address ":9001"