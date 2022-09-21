# DB in Docker container

## What is this ?

To avoid exhaustive and painful environment setting, a database with MySQL is created in a Docker container.

## Usage

### Build a Docker image and start a container

```
$ docker-compose -d up --build
```

### Start a container with an existing Docker image

```
$ docker-compose up
```

### Attach to the container

You could attach to a container in any means, however,

```
$ docker exec --rm -it getter_db_host /bin/bash
```

### Mingrations and DB use

Once after the Docker image is created, you can play with this MySQL DB.

You can find the DB configuration in `docker-compose.yaml`.