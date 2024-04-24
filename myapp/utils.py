# utils.py
import redis
from django.conf import settings

redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

def create_author(name, age, family_name):
    author_key = f"author:{name}"
    redis_client.hmset(author_key, {"name": name, "age": age, "family_name": family_name})

def create_book(name, author):
    book_key = f"book:{name}"
    redis_client.hmset(book_key, {"name": name, "author": author})
