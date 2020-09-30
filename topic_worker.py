import pika
import sys
conn = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",
        port=5672
    )
)
channel = conn.channel()
channel.exchange_declare(
    exchange="topic_logs",
    exchange_type="topic"
)
queue = channel.queue_declare(
    "",
    exclusive=True
)
queue_name = queue.method.queue
binding_keys = sys.argv[1:]
if not binding_keys:
    print(sys.stderr, "Usage: %s [binding_key]..." % (sys.argv[0],))
    sys.exit(1)
for key in binding_keys:
    channel.queue_bind(
        exchange="topic_logs",
        routing_key=key,
        queue=queue_name
    )
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body,))
channel.basic_consume(
    queue=queue_name,auto_ack=True,on_message_callback=callback
)
channel.start_consuming()