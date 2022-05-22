# django-app

This is test application
- https://docs.docker.com/compose/django/
- https://docs.djangoproject.com/ja/3.1/intro/tutorial01/

## memo

- How to operate to migrate
- How to connect PostgreSQL, (named = db container)

```
[Zset ~/sampledjango]{feature/djangoapp}$ docker-compose exec web python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying polls.0001_initial... OK
[Zset ~/sampledjango]{feature/djangoapp}$ docker-compose exec db psql -h db -U postgres
Password for user postgres:
psql (13.2 (Debian 13.2-1.pgdg100+1))
Type "help" for help.

postgres=# \dt
                   List of relations
 Schema |            Name            | Type  |  Owner
--------+----------------------------+-------+----------
 public | auth_group                 | table | postgres
 public | auth_group_permissions     | table | postgres
 public | auth_permission            | table | postgres
 public | auth_user                  | table | postgres
 public | auth_user_groups           | table | postgres
 public | auth_user_user_permissions | table | postgres
 public | django_admin_log           | table | postgres
 public | django_content_type        | table | postgres
 public | django_migrations          | table | postgres
 public | django_session             | table | postgres
 public | polls_choice               | table | postgres
 public | polls_question             | table | postgres
(12 rows)
```

## Test
```
[Zset ~/django-app]{feature/djangoapp}$ docker-compose run web python manage.py test polls
Creating django-app_web_run ... done
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.200s

OK
Destroying test database for alias 'default'...
```
