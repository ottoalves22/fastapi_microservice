from typing import Dict
from elasticsearch_dsl import Search, Q
import pandas as pd
from elasticsearch import Elasticsearch, helpers, exceptions


class ElasticsearchHandler():
    def __init__(self, host: str, port: str, username: str, password: str, index: str, mapping: dict = None):
        if username is None or password is None:
            url = f'{host}:{port}'
        else:
            url = f'{username}:{password}@{host}:{port}'

        self._es = Elasticsearch(hosts=url)
        self._index = index

        if self._es.indices.exists(self._index) == False:
            if mapping is not None:
                self._es.indices.create(index=self._index, ignore=400, body=mapping)
            else:
                self._es.indices.create(index=self._index, ignore=400)

    def get_result_source(self, els_response: dict):
        result = []
        if 'hits' in els_response and 'hits' in els_response['hits']:
            for res in els_response['hits']['hits']:
                data = res['_source']
                data['_id'] = res['_id']
                result.append(data)
        return result

    def close(self):
        self._es.close()

    def get_by_id(self, _id: str):
        try:
            res = self._es.get(index=self._index, id=_id)
            return res
        except exceptions.NotFoundError:
            return None

    def get_all(self):
        try:
            res = self._es.search(index=self._index, size=1000,
                                  body={"sort": {"total_recent": "desc"}, 'from': 0, 'size': 100})
            res = self.get_result_source(res)
            return res
        except exceptions.NotFoundError:
            return None

    def create_doc(self, index: str, id_: str, body: Dict = None):
        return self._es.create(index=index, body=body, id=id_)

