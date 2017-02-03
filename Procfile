web: gunicorn config.wsgi:application
worker: newrelic-admin run-program celery worker --app=echarli2.taskapp --loglevel=info
