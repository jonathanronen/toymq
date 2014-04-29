import json
import argparse
from Queue import Queue, Empty
from flask import Flask, abort, request

app = Flask(__name__)

queue = Queue()

@app.route('/post', methods=['POST'])
def post_message():
    try:
        message = json.loads(request.data)
        queue.put(message)
        return 'ok'
    except Exception as e:
        raise e
        abort(400)

@app.route('/pop', methods=['GET'])
def pop_message():
    try:
        return json.dumps(queue.get_nowait())
    except Empty:
        abort(404)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--host', type=str, dest='host', default='0.0.0.0', help='Default 0.0.0.0')
    parser.add_argument('-p', '--port', type=int, dest='port', default=26016, help='Default 26016')
    parser.add_argument('--debug', action='store_true', default=False, dest='debug', help='Run flask in debug mode')
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=args.debug)
