MAKEFILE_DIR:=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
IMAGE_NAME=getter-robo-db
DEV_IMAGE_NAME=getter-robo-db_dev
IMAGE_TAG=00.00
CONTAINER_NAME=$(IMAGE_NAME)
DEV_CONTAINER_NAME=$(DEV_IMAGE_NAME)
K8S_NAMESPACE=time-series
CONTAINER_START_FLAG=-it --rm
CONTAINER_ATTACH_FLAG=/bin/bash

image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
dev_env_image:
	docker build -t $(DEV_IMAGE_NAME):$(IMAGE_TAG) -f ./Dockerfile-dev .
run:
	docker run -v $(MAKEFILE_DIR)/volume:/home/sigma_chan/volume -e TZ=Asia/Tolyo --name $(IMAGE_NAME) -it $(IMAGE_NAME):$(IMAGE_TAG) /bin/bash
attache:
	docker exec -v $(MAKEFILE_DIR)/volume:/home/sigma_chan/volume -e TZ=Asia/Tolyo -it $(IMAGE_NAME) /bin/bash
migration:
	poetry run alembic init migrations
revise_db:
	poetry run alembic revision --autogenerate -m "create tables"	

db_start_after_reboot:
	sudo /etc/init.d/mysql start
	sudo mysql_secure_installation
	sudo mysql

start_container:
	docker run --name $(CONTAINER_NAME) $(CONTAINER_START_FLAG) $(IMAGE_NAME):$(IMAGE_TAG) $(CONTAINER_ATTACH_FLAG)
exec_container:
	docker exec -t $(CONTAINER_NAME) $(CONTAINER_ATTACH_FLAG)
clear_container:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)
clear_image:
	docker rmi $(IMAGE_NAME):$(IMAGE_TAG)
clear_all_images:
	docker images -aq | xargs docker rmi
clear_all_containers:
	docker ps -aq | xargs docker stop

start_dev_container:
	docker run --name $(DEV_CONTAINER_NAME) -v $(PWD):/home/sigma_chan $(CONTAINER_START_FLAG) $(DEV_IMAGE_NAME):$(IMAGE_TAG) $(CONTAINER_ATTACH_FLAG)
exec_dev_container:
	docker exec -t $(DEV_CONTAINER_NAME) $(CONTAINER_ATTACH_FLAG)
clear_dev_container:
	docker stop $(DEV_CONTAINER_NAME)
	docker rm $(DEV_CONTAINER_NAME)
clear_dev_image:
	docker rmi $(DEV_IMAGE_NAME):$(IMAGE_TAG)
