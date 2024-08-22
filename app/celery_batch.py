from celery import Celery
import random
import string
from celery import shared_task
import time

# Global start time
start_time = None
total_records = 0
app = Celery('celery_batch', 
             broker='amqp://guest:guest@127.0.0.1:5672/',
             backend="rpc://127.0.0.1:6379")

# Enable retrying connections on startup
app.conf.broker_connection_retry_on_startup = True


@shared_task
def reader():

    global start_time, total_records
    if start_time is None:
        start_time = time.time() 

    total_records=5

    for i in range(total_records):
        value = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        data = {"key": value}
        print(f"Reader output: {data}")
        processor.apply_async((data,))

@shared_task
def processor(data):
    processed_data = data['key'].upper()
    print(f"Processor received: {data}, Processor output: {processed_data}")
    writer.apply_async((processed_data,))

@shared_task
def writer(processed_data):
    global total_records
    print(f"Writer received: {processed_data}")
    if total_records is 5:
        end_time = time.time()  # Record end time when the last chunk is written
        total_time = end_time - start_time
        print(f"************ Total time for processing: {total_time} seconds")
    total_records = total_records + 1 


