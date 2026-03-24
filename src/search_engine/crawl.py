import json
import re
from collections import Counter

from confluent_kafka import Consumer
from opensearchpy import OpenSearch
from bs4 import BeautifulSoup

# ---- CONFIG ----
KAFKA_BOOTSTRAP = "kafka:9092"
INPUT_TOPIC = "raw_html"

INDEX_NAME = "webpages"
OPENSEARCH_HOST = "http://opensearch:9200"

# ---- KAFKA ----
consumer = Consumer({
    'bootstrap.servers': KAFKA_BOOTSTRAP,
    'group.id': 'parser-group',
    'auto.offset.reset': 'earliest'
})
consumer.subscribe([INPUT_TOPIC])

# ---- OPENSEARCH ----
os_client = OpenSearch(OPENSEARCH_HOST)

STOPWORDS = set([
    "the","and","is","in","to","of","for","on","with",
    "as","by","at","an","be","this","that","it"
])

def extract_keywords(html, top_n=15):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style"]):
        tag.extract()

    text = soup.get_text(" ")
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())

    filtered = [w for w in words if w not in STOPWORDS]

    freq = Counter(filtered)
    return [w for w, _ in freq.most_common(top_n)]

print("Parser started...")

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print(msg.error())
        continue

    data = json.loads(msg.value().decode("utf-8"))
    doc_id = data["doc_id"]

    try:
        res = os_client.get(index=INDEX_NAME, id=doc_id)
    except Exception as e:
        print(f"Fetch failed: {e}")
        continue

    html = res["_source"].get("html", "")
    if not html:
        continue

    keywords = extract_keywords(html)

    os_client.update(
        index=INDEX_NAME,
        id=doc_id,
        body={"doc": {"keywords": keywords}}
    )

    print(f"Updated {doc_id}")