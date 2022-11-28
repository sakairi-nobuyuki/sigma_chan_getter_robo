SRCS = sigma_chan_getter_robo tests
#SRCS = db_oparators sigma_chan_db tweet_getter tests post_process
POETRY_PREFIX = poetry run
CONTAINER_NAME = getter-robo
REGISTORY_NAME = nsakairi
DEFAULT_TAG = latest

format:
	@for SRC in $(SRCS); do $(POETRY_PREFIX) black $$SRC --config pyproject.toml; done
	@for SRC in $(SRCS); do $(POETRY_PREFIX) isort $$SRC --profile black; done

build-app:
	docker-compose build --no-cache app

build-app-and-push:
	docker-compose build --no-cache app
	docker push $(REGISTORY_NAME)/$(CONTAINER_NAME):$(DEFAULT_TAG)

build-run-app:
	docker-compose up -d --build app

exec-up:
	docker exec -it getter-robo 

clear_app_container:
	docker stop $(CONTAINER_NAME)
	docker rm $(CONTAINER_NAME)

clear_images:
	docker stop $(docker ps -q)
	docker rm $(docker ps -q)
	docker rmi $(docker images -q)