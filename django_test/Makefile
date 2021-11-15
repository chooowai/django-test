all: install migrate run

install:
	pip install -r ./requirements.txt

migrate:
	python manage.py makemigrations quickstart
	python manage.py migrate

run:
	python manage.py runserver