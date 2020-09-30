import pika
import uuid

class FibonacciRpcClient(object):
    def __init__(self):
        self.conn = pika.BlockingConnection(
            parameters=pika.ConnectionParameters(
                host="localhost",port=5672
            )
        )
        self.channel = self.conn.channel()
        result = self.channel.queue_declare(
            queue="",
            exclusive=True
        )
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            self.callback_queue,
            self.on_response,
        )
    def on_response(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body
    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        print(self.corr_id)
        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_queue",

            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id
            ),
            body=str(n),
        )
        while self.response is None:
            self.conn.process_data_events()
        return self.response
fibonacci_rpc = FibonacciRpcClient()
print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(10)
print(" [.] Got %r" % (response,))