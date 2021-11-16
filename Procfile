release: python manage.py makemigrations main --no-input
release: python manage.py migrate --no-input

web: gunicorn django_test.wsgi