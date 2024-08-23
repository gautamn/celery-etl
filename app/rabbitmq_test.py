import pika

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('3.85.11.138', 5672, 'celery_vhost', credentials)

try:
    connection = pika.BlockingConnection(parameters)
    print("Connection successful")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")
