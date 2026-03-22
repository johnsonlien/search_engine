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

q='hello'
index_name = 'python-test-index'
query={
    'size': 5,
    'query': {
        'multi_match': {
            'query': q,
            'fields': ['title^2', 'director', 'html']
        }
    }
}
response = client.search(
    body=query,
    index=index_name
)

print(f"Search results: {json.dumps(response, indent=2)}" )