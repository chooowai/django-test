all: install migrate run

install:
	pip install -r ./requirements.txt

migrate:
	python manage.py makemigrations main
	python manage.py migrate

run:
	python manage.py runserver

show-urls:
	python manage.py show_urls

populate:
	python populate.py