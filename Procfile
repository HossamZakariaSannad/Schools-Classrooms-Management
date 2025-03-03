release: python manage.py collectstatic --noinput && python manage.py migrate
web: gunicorn core.wsgi:application --bind 0.0.0.0:8080
