from kafka import KafkaProducer

producer = KafkaProducer()
future = producer.send('Johnson', b'HOWS THIS')
result = future.get(timeout=2)
# producer.flush()