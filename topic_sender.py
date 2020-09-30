import pika
import sys

conn = pika.BlockingConnection(
    pika.ConnectionParameters(
        host="localhost",port=5672
    )
)
channel = conn.channel()
channel.exchange_declare(
    exchange="topic_logs",
    exchange_type="topic"
)
severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = " ".join(sys.argv[2:]) or "hello world"
channel.basic_publish(
    exchange="topic_logs",
    routing_key=severity,
    body=message
)
print(" [x] Sent %r:%r" % (severity, message))

conn.close()