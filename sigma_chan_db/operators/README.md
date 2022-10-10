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

