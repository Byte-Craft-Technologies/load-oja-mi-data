import os
import psycopg2.pool

_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=5,
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
    database=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
)


def get_connection():
    return _pool.getconn()


def release_connection(conn):
    _pool.putconn(conn)
