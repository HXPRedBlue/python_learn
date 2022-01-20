from kafka import KafkaConsumer
from kafka.consumer import group
from kafka.errors import KafkaError
import json

def consumer_demo():
    consumer = KafkaConsumer(
        'kafka_demo1',
        bootstrap_servers='10.32.0.8:9092',
        group_id="test"
    )

    for message in consumer:
        print(f"receive key: {json.loads(message.key.decode())} value:{json.loads(message.value.decode())}")


if __name__ == '__main__':
    consumer_demo()