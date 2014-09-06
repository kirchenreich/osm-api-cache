# osm-api-cache

## mission

create a fast and reliable cache for Openstreetmap elements (nodes, ways, relations)
if your application is not using the full osm database.


## requirements

* Python 3.3+
* see requirements.txt

## settings

add the following settings to `credentials.py`

```
POSTGRES_USERNAME = 'osmcache'
POSTGRES_DBNAME = 'osmcache'
POSTGRES_PASSWORD = 'password'

TEST_POSTGRES_USERNAME = 'test_osmcache'
TEST_POSTGRES_DBNAME = 'test_osmcache'
TEST_POSTGRES_PASSWORD = 'password'
```


## usage

### help

```python osmcache --help```

### initial db creation

```python osmcache.py initdb```
