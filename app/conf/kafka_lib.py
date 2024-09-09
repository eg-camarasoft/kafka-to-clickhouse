import logging

kafka_conf: dict = {
        "default": {
            "base": {
                "bootstrap.servers": "kafka-dev.service.consul",
                "socket.timeout.ms": 2000,
                "socket.connection.setup.timeout.ms": 2000,
                "security.protocol": "SASL_PLAINTEXT",
                "sasl.mechanism": "PLAIN",
            },
            "ext": {
                "operation_timeout_s": 2,
                "producer_poll_timeout_s": 0,  # default timeout when not specified
                "producer_threaded_poll_timeout_s": 1,  # continuous threaded poll
            },
            "producer": {
                "compression.type": "zstd",
                "linger.ms": 5,
                "sasl.username": "p0",
                "sasl.password": "password",
            },
            "consumer": {"sasl.username": "c0", "sasl.password": "password"},
            "admin_client": {"sasl.username": "p0", "sasl.password": "password"},
            "logger": {"get_logger": logging.getLogger("kafka-lib")},
        }
    }