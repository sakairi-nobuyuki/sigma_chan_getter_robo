MAKEFILE_DIR:=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
IMAGE_NAME=getter-robo-db
IMAGE_TAG=00.00

K8S_NAMESPACE=time-series


image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
run:
	docker run -v $(MAKEFILE_DIR)/volume:/home/sigma_chan/volume -e TZ=Asia/Tolyo --name $(IMAGE_NAME) -it $(IMAGE_NAME):$(IMAGE_TAG) /bin/bash
attache:
	docker exec -v $(MAKEFILE_DIR)/volume:/home/sigma_chan/volume -e TZ=Asia/Tolyo -it $(IMAGE_NAME) /bin/bash
migration:
	poetry run alembic init migrations
revise_db:
	poetry run alembic revision --autogenerate -m "create tables"	

clear_containers:
	docker ps -aq | xargs docker rm
clear_images:
	docker images -aq | xargs docker rmi -f 
stop_containers:
	docker ps -aq | xargs docker stop	