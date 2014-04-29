# Toy Message Queue
This is a very simple MQ to pass simple messages between a producer and a consumer.

### Install
    python setup.py install

### Server
    python -mtoymq.server

And you can start posting and poping messages:

    curl localhost:26016/post -X POST -H "Content-Type: application/json" -d '{"shalom" : "olam"}'
    curl localhost:26016/pop


### Client
    from toymq.client import ToyMQClient

    mq = ToyMQClient(server, port)
    mq.add_message({'hello' : 'world'})

    message = mq.pop_message()

    assert message['hello'] == 'world'

#### Another client
There's also a client using `urllib2`, because my phone has that but not `requests`.

    from toymq.client_urllib2 import ToyMQClient
