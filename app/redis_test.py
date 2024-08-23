import redis

def test_redis_connection(host='3.85.11.138', port=6379, db=0):
    try:
        # Create a Redis client
        client = redis.Redis(host=host, port=port, db=db)
        
        # Test the connection
        response = client.ping()
        
        if response:
            print("Successfully connected to Redis.")
        else:
            print("Failed to connect to Redis.")
    
    except redis.ConnectionError as e:
        print(f"Redis connection error: {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_redis_connection()
