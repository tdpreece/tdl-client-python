from .utils.jmx.broker.remote_jmx_broker import RemoteJmxBroker


def before_all(context):
    context.broker = RemoteJmxBroker.connect(
        'localhost',
        '28161',
        'TEST.BROKER'
    )
