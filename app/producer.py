import time

from kafkalib import conf, client
from kafkalib.models.base import KafkaBaseModel
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

kafka_conf: dict = {
        "default": {
            "base": {
                "bootstrap.servers": "kafka-broker:9092",
                "socket.timeout.ms": 2000,
                "socket.connection.setup.timeout.ms": 2000,
                "security.protocol": "PLAINTEXT",
                "sasl.mechanism": "PLAIN",
            },
            "ext": {
                "operation_timeout_s": 2,
                "producer_poll_timeout_s": 1,  # default timeout when not specified
                "producer_threaded_poll_timeout_s": 1,  # continuous threaded poll
            },
            "producer": {
                "acks": 1,
                "linger.ms": 5,
                "message.timeout.ms": 10000,
            },
            "consumer": {},
            "admin_client": {},
            "logger": {"get_logger": logging.getLogger},
        }
    }



class KafkaClickhouseTest(KafkaBaseModel):

    #
    #
    # base validators in constructor
    topic: str = 'clickhouse_test'
    cluster_name: str = 'default'

    name: str
    surname: str





conf.setup(kafka_conf)


ct = KafkaClickhouseTest(
    name='test',
    surname='test'
)
ct.produce()


time.sleep(20)
