from kafka import KafkaProducer, KafkaConsumer

import json

producer = KafkaProducer()
another_consumer = KafkaConsumer('Another')
johnson_consumer = KafkaConsumer(
    'Johnson',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='some_group'
)

# print(producer.metrics())

print("Sending messages to broker")
for i in range(2):
    message = f"message_{i}"
    future = producer.send('Johnson', b'hello world')
    result = future.get(timeout=10)
    print(result)
producer.close()

for msg in johnson_consumer:
    print(msg)

# print("Trying to read messages from topic...")
# try:
#     for msg in johnson_consumer:
#         # print(msg.header)
#         print(f"Received message: \nTopic: {msg.topic}\nMessage: {msg.value}")
# except Exception as ex:
#     print("Error!")
#     print(f"Exception: {ex}")
