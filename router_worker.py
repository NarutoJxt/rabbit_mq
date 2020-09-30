import pika
import sys
conn = pika.BlockingConnection(pika.ConnectionParameters(host="localhost",port=5672))
channel = conn.channel()
channel.exchange_declare(exchange="direct_logs",exchange_type="direct")

severities = sys.argv[1:]
if not severities:
    print(sys.stderr, "Usage: %s [info] [warning] [error]" % \
                         (sys.argv[0],))
    sys.exit(1)
queue_name_list = []
def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body,))
for severity in severities:
    result = channel.queue_declare("", exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange="direct_logs", routing_key=severity, queue=queue_name)
    channel.basic_consume(queue_name, callback, auto_ack=True)

print(' [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()