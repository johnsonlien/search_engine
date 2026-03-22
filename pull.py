from kafka import KafkaConsumer

consumer = KafkaConsumer('Johnson')
# consumer.subscribe(['Johnson'])

for msg in consumer:
    print(msg)