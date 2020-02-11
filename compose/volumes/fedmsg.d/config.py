import logging

config = {
    'ciconsumer': True,
    'moksha.blocking_mode': True,
    'moksha.monitoring.socket': 'tcp://0.0.0.0:10030',
    'validate_signatures': False,
    'stomp_heartbeat': 1000,

    'stomp_uri': 'umb:61612',
    'resultsdb-updater.log_level': logging.DEBUG,
    'resultsdb-updater.resultsdb_api_url': 'http://resultsdb:5001/api/v2.0',
    'resultsdb-updater.resultsdb_api_ca': None,
    'resultsdb-updater.topics': ['*'],
    'resultsdb-updater.requests_timeout': 15,

    'topic_prefix': '/topic/VirtualTopic.eng',
    'environment': 'ci',
    'endpoints': {
        'relay_outbound': [
            'tcp://127.0.0.1:4001',
            'tcp://127.0.0.1:4002',
            'tcp://127.0.0.1:4003',
            'tcp://127.0.0.1:4004',
            'tcp://127.0.0.1:4005',
        ],
    },
    'relay_inbound': 'tcp://127.0.0.1:2003',
    'zmq_enabled': True,
}
