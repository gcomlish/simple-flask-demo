from app import app

from flask import Flask, request, render_template, Response
from pykafka import  KafkaClient

def get_kafka_client():
    return KafkaClient(hosts='134.105.1.174:9092')

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))

#topicname = 'example-topic'
@app.route('/topic/<topicname>')
def get_messages(topicname):
    client = get_kafka_client()
    def events():
        for i in client.topics['topicname'].get_simple_consumer():
            yield 'data:{0}\n\n'.format(i.value.decode())
    return Response(events(), mimetype='text/event-stream')

