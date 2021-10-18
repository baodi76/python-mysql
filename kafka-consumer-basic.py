from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
   'testTopic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='None11',
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    bootstrap_servers=['119.13.83.68'])

for m in consumer:
    print(m.value)

