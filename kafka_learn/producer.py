from kafka import KafkaProducer
from kafka.errors import KafkaError
import json


def producer_demo():
    producer = KafkaProducer(
        bootstrap_servers=["10.32.0.8:9092"],
        key_serializer=lambda k: json.dumps(k).encode(),
        value_serializer=lambda v: json.dumps(v).encode()
    )

    for i in range(0, 3):
        future = producer.send(
            'kafka_demo1',
            key='count_num',
            value=str(i),
            partition=1
        )
        print(f"send {str(i)}")
        try:
            future.get(timeout=10)
        except KafkaError as e:
            print(e)
        

if __name__ == '__main__':
    producer_demo()