from .abstract_db import AbstractDB

from opensearchpy import OpenSearch

# data_format = {
#     'url': '',          # Primary Key
#     'html': '',
#     'lastScraped': '',
#     'authors': [] # optional
# }

class OpenSearchDB(AbstractDB):
    def __init__(self, ip="127.0.0.1", port="9200", auth=('admin', 'str0ngp@ssword'), index_name="some_name"):
        self.index_name = index_name
        self.client = OpenSearch(
            hosts=[{'host': f"{ip}", 'port': f"{port}"}],
            http_auth = auth,
            use_ssl=True,
            verify_certs=False,
            ssl_show_warn=False
        )

    def insertDoc(self, doc):
        response = self.client.index(
            index=self.index_name,
            body=doc,
            id=doc.url,         # Use URL as unique ID,
            refresh=True,       # Make document immediately searchable
        )