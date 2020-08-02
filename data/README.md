# Pokemon-Teams-Data

Data model isn't very good, really just trying to focus on frontend with this project.


I decided to make this whole app local and single user so there's no user table.


## PostgreSQL ODBC Setup
install ODBC driver - ```apt-get install odbc-postgresql```

edit ODBC config: **/etc/odbcinst.ini**
Postgres libraries default location: **/usr/lib/x86_64-linux-gnu/odbc/**

Definitely use the Unicode driver, the ANSI driver doesn't play nice.

```ini
[PostgreSQL Unicode]
Driver=/usr/lib/x86_64-linux-gnu/odbc/psqlodbca.so
Setup=/usr/lib/x86_64-linux-gnu/odbc/libodbcpsqlS.so
# ...
```

Verify driver is acknowledged by pyodbc
```python
import pyodbc 

print(pyodbc.drivers())
```


## Allow Remote Connections
By default running on 127.0.0.1:5432 and reject anything from outside.
So, some stuff needs to be opened up.

Find file - ```sudo find / -type f -iname "postgresql.conf"```

Edit **/etc/postgresql/11/main/postgresql.conf** (Postgres Configuration)

Change ```listen_addresses = 'localhost'``` to ```listen_addresses = '*'```

Add entry to **/etc/postgresql/11/main/pg_hba.conf** (Client Auth Configuration)
```ini
host    all             all             <LOCAL-IP>/32          md5
```


I'm not taking security into account at all here. This is my dumb pi server for development purposes.

Restart Postgres - ```sudo systemctl restart postgresql```


## Postgres Client (Remote)
* Install client - ```sudo apt-get install -y postgresql-client```
* Connect - ```psql -U <USER> -p <PORT> -h <HOST>```



## Postgres ANSI Driver - Unsupported Type
If using the Postgres ANSI driver:

To fix this error:
```pyodbc.Error: ('07006', '[07006] Received an unsupported type from Postgres. (14) (SQLGetData)')```

I stumbled on https://github.com/mkleehammer/pyodbc/wiki/Connection#ctype

By default in python3, pyodbc uses unicode.

```python
cnxn.setencoding(encoding='utf-8')
```


## Misc
```sql
-- Verify port
select * from pg_settings where name = 'port';

```

List all tables in schema: ```\dt pokemon.*```
