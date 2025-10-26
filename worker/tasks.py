import os
import time

import dramatiq
from dramatiq.brokers.redis import RedisBroker

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_broker = RedisBroker(url=redis_url)
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def countdown_task(seconds: int = 10):
    for i in range(seconds, 0, -1):
        print(f"Countdown: {i} seconds remaining")
        time.sleep(1)
    print("Countdown finished!")
    return "Task completed"
