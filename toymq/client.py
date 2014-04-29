import json
import requests
from Queue import Empty

class ToyMQClient():
    """
    Python client for ToyMQ. Implements posting and poping messages.
    """
    def __init__(self, address='localhost', port=26016):
        self.base_url = "http://{address}:{port}".format(address=address, port=port)
        self.post_url = self.base_url + '/post'
        self.pop_url = self.base_url + '/pop'

    def add_message(self, message):
        """
        Posts a message to MQ. Raises exception if http response is not 200s.
        """
        m = json.dumps(message)
        resp = requests.post(self.post_url,
                headers={'Content-Type': 'application/json'},
                data=m)
        if not resp.ok:
            raise Exception('Unable to post to MQ', resp)

    def pop_message(self):
        """
        Reads a message from server. Should be used in a try-block, as it raises Empty if there are no messages.
        """
        resp = requests.get(self.pop_url)
        if resp.status_code == 404:
            raise Empty
        m = json.loads(resp.content)
        return m
