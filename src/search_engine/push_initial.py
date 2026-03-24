from kafka import KafkaProducer

def getInitialUrls(file: str):
    try:
        with open(file, 'r') as f:
            return [url for url in f]
    except Exception as ex:
        print(f"Could not open file {file}! Exception: {ex}")
        raise

def pushInitialUrls(urls: list[str]):
    try:
        producer = KafkaProducer(bootstrap_servers=["127.0.0.1:9092"])
    except Exception as ex:
        print(f"Could not connect to Kafka: {ex}")
        raise
    successful = []
    failed = []
    for url in urls:
        try:
            future = producer.send("url", url.encode('utf-8'))
            response = future.get(timeout=10)
            print(response)
            successful.append(url)
        except Exception as ex:
            print(f"Could not push {url} to Kafka: {ex}")

if __name__ == "__main__":
    urls = getInitialUrls("url_list.txt")
    pushInitialUrls(urls)