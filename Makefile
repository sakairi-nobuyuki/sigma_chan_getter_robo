SRCS = db_oparators sigma_chan_db tweet_getter tests
POETRY_PREFIX = poetry run


format:
	@for SRC in $(SRCS); do $(POETRY_PREFIX) black $$SRC --config pyproject.toml; done
	@for SRC in $(SRCS); do $(POETRY_PREFIX) isort $$SRC --profile black; done

build-app:
	docker-compose build --no-cache app

clear_images:
	docker stop $(docker ps -q)
	docker rm $(docker ps -q)
	docker rmi $(docker images -q)