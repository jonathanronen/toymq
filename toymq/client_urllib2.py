import json
import urllib
import urllib2
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
        req = urllib2.Request(self.post_url,
            headers={'Content-Type': 'application/json'},
            data=m)
        resp = urllib2.urlopen(req)
        if not resp.code == 200:
            raise Exception('Unable to post to MQ', resp)

    def pop_message(self):
        """
        Reads a message from server. Should be used in a try-block, as it raises Empty if there are no messages.
        """
        try:
            resp = urllib2.urlopen(self.pop_url)
            m = json.load(resp)
            return m
        except urllib2.HTTPError as e:
            if e.code == 404:
                raise Empty
            else:
                raise e
