import pylibmc
import os

servers = os.getenv('MEMCACHIER_SERVERS', '').split(',')
username = os.getenv('MEMCACHIER_USERNAME', '')
password = os.getenv('MEMCACHIER_PASSWORD', '')

mc = pylibmc.Client(
    servers,
    username=username,
    password=password,
    binary=True
)

mc.set('key', 'value')

value = mc.get('key')

if value is not None:
    print(value)
