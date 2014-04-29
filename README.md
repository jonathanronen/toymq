# Toy Message Queue
This is a very simple MQ to pass simple messages between a producer and a consumer.

### Server
    python -mtoymq.server

And you can start posting and poping messages:
    curl localhost:26016/post -X POST -H "Content-Type: application/json" -d '{"shalom" : "olam"}'
    curl localhost:26016/pop


### Client
    from toymq import ToyMQClient

    mq = ToyMQClient(server, port)
    mq.add_message({'hello' : 'world'})

    message = mq.pop_message()

    assert message['hello'] == 'world'