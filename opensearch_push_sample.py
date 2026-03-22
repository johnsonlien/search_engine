from opensearchpy import OpenSearch

import json

auth = ('admin', 'G@-AS1;S3cur!ty')

client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=auth,
    use_ssl=True,
    verify_certs=False,
    ssl_show_warn=False
)

# Define an index and a document
index_name = 'python-test-index'
document = {
 'title': 'Contemporary Art Sucks',
 'director': 'Johnson Lien',
 'year': '2026',
 'html': '<head><title>Website</title></head><body><h1>Hello OpenSearch</h1></body>'
}

response = client.index(
    index=index_name,
    body=document,
    id='1',
    refresh=True # Makes the document immediately searchable
)

print(f"Indexed document response: {json.dumps(response, indent=2)}")