# Database

Run database locally.

## Installation


Installing python libraries.
```
$ poetry install
```

Installing MySql in your local environment by any measures.

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

