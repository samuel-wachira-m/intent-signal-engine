from celery import Celery

# Initialize Celery app
app = Celery('reddit_fetcher',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0')

# Task serialization settings
app.conf.task_serializer = 'json'
app.conf.result_serializer = 'json'

# Beat schedule for fetching Reddit posts every 5 minutes
app.conf.beat_schedule = {
    'fetch_reddit_posts': {
        'task': 'tasks.fetch_posts',
        'schedule': 300.0,  # every 5 minutes
    },
}