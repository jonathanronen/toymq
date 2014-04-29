# Toy Message Queue
This is a very simple MQ to pass simple messages between a producer and a consumer.

### Server
    python server.py -h

### Client
    from toymq import ToyMQClient

    mq = ToyMQClient(server, port)
    mq.add_message({'hello' : 'world'})

    message = mq.pop_message()

    assert message['hello'] == 'world'