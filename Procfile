release: python crimpulse/manage.py migrate
web: python crimpulse/manage.py collectstatic --no-input; daphne proj.asgi:application --port $PORT --bind 0.0.0.0
worker: python crimpulse/manage.py process_tasks