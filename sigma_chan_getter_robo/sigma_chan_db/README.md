# Database

Run database locally.

## Installation


Installing python libraries.
```
$ poetry install
```

Installing MySql in your local environment by any measures.

## IP adress for WSL and container usage

Using database operator or database in a Docker conteiner with WSL environment, following procedure to determine the IP address of the data base is needed.

Open a command prompt in Windows environment and run,

```
> ipconfig
```

and you could find a IPv4 address.

You should replace IP address written in `alembic.ini` and `operators/setting.py` to that IP address got from the command prompt.

## Migration

### In local
Create a database table.
```
$ poetry run alembic revision --autogenerate -m "create tables"
$ poetry run alembic upgrade head
```


Confirm in MySql.
```
$ sudo mysql
mysql> show columns from job_id in getter_db;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| job_id   | varchar(64) | NO   | PRI | NULL    |       |
| tweet_id | varchar(64) | NO   |     | NULL    |       |
| modified | datetime    | NO   |     | NULL    |       |
| created  | datetime    | NO   |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
```


### In a Docker container

Migration in a container. At first attach to the container once after the containers are 
built with `docker-compose up -d --build`.
```
$ docker exec -it getter-robo /bin/bash
```

Run the program by,
```
$ alembic -c sigma_chan_getter_robo/sigma_chan_db/alembic.ini revision --autogenerate -m "create table"
$ alembic -c sigma_chan_getter_robo/sigma_chan_db/alembic.ini upgrade head
```
You can find a newly created tables by connecting the DB by MySQL in the container by the following commands.
```
$ mysql -u root -p -h 192.168.0.16
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 6
Server version: 5.7.40 MySQL Community Server (GPL)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| getter_db          |
| mysql              |
| performance_schema |
| sys                |
| test_db            |
+--------------------+
6 rows in set (0.01 sec)

mysql> use getter_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+---------------------+
| Tables_in_getter_db |
+---------------------+
| alembic_version     |
| job_id              |
+---------------------+
2 rows in set (0.00 sec)

mysql>
```

## Tests

### In a container 

After the initial migration, creating tables, are finished, attach to the container and run,

```
$ docker exec -it getter-robo /bin/bash
sigma_chan@f56bcf658c89:~$ pytest tests/sigma_chan_db/
=================================================================================================== test session starts ===================================================================================================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/sigma_chan
collected 4 items

tests/sigma_chan_db/test_getter_robo_db.py ....                                                                                                                                                                     [100%]

==================================================================================================== warnings summary =====================================================================================================
../nsakairi/sigma_chan_getter_robo/tests/sigma_chan_db/test_getter_robo_db.py:8
  /home/nsakairi/sigma_chan_getter_robo/tests/sigma_chan_db/test_getter_robo_db.py:8: PytestUnknownMarkWarning: Unknown pytest.mark.db_operation - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
============================================================================================== 4 passed, 1 warning in 0.23s ===============================================================================================
```