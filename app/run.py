from celery import chain
from celery_batch import reader
def run_batch():
    reader.delay()

if __name__ == '__main__':
    run_batch()
