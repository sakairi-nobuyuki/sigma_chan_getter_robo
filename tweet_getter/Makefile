MAKEFILE_DIR:=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
IMAGE_NAME=tw-getter
DEV_IMAGE_NAME=tw-getter-dev
IMAGE_TAG=00.00
CONTAINER_NAME=$(IMAGE_NAME)
DEV_CONTAINER_NAME=$(DEV_IMAGE_NAME)
K8S_NAMESPACE=time-series
CONTAINER_START_FLAG=-it --rm
CONTAINER_ATTACH_FLAG=/bin/bash
SRCS = db_oparators  pyproject.toml  sigma_chan_db  tweet_getter tests
POETRY_PREFIX = poetry run


image:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
run:
	docker run -v $(MAKEFILE_DIR)/volume:/home/sigma_chan/volume -e TZ=Asia/Tolyo --name $(IMAGE_NAME) -it $(IMAGE_NAME):$(IMAGE_TAG) /bin/bash

format:
	$(foreach DIR, $(SRCS), $($(POETRY_PREFIX) black $(DIR) --config pyproject.toml))
	$(foreach DIR, $(SRCS), $($(POETRY_PREFIX) isort $(DIR) --profile black))