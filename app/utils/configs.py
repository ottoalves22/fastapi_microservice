try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
import logging
import json
import os
from pathlib import Path


data = ConfigParser()
data.read('settings.ini')

#[elasticsearch]
els_host = data.get('elasticsearch', 'ELASTICSEARCH_HOST', vars=os.environ)
els_port = data.get('elasticsearch', 'ELASTICSEARCH_PORT', vars=os.environ)
els_user = data.get('elasticsearch', 'ELASTICSEARCH_USERNAME', vars=os.environ)
els_pwd = data.get('elasticsearch', 'ELASTICSEARCH_PASSWORD', vars=os.environ)

#[postgresql]
pg_host = data.get('postgres', 'PG_HOST', vars=os.environ)
pg_port = data.get('postgres', 'PG_PORT', vars=os.environ)
pg_user = data.get('postgres', 'PG_USERNAME', vars=os.environ)
pg_pwd = data.get('postgres', 'PG_PASSWORD', vars=os.environ)
pg_database = data.get('postgres', 'PG_DATABASE', vars=os.environ)

