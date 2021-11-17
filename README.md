# Django Test

## What is this?

A django-rest-framework basic CRUD test using psql.

Hosted on [Demo](https://cho-django-test.herokuapp.com/) using Heroku.

There are two main end points
- students/
- schools/

and one nested end point
- schools/{id}/students

[PUT, POST, GET, DELETE] methods are avialable for all endpoints.
For example
- GET students/ will return all students
- GET students/{id} will return a student
- POST students/ will create new students
- PUT students/{id} will update a student
- DELETE students/{id} will delete a student

Order, Filter and Pagination are also available.
For example
- GET students/?gpa=3&school=2 will return only students who has gpa 3 and register under school 2
- GET students/?ordering=gpa will return the result sorted by gpa
- GET students?/page=2 will return 2nd page paginated by 25 sizes

Bad request are handled in such manners
- Business logic are validated in serializers, e.g. gpa must be between 0 and 4, the school can't accept students more than max limit
- General validations are handled in model itsef, e.g. school name can't be null and can't accept more than 20 characters

They all will return BadRequest HTTP Response with proper message

Test cases for all APIs are added in /tests

## Dependenices for Local

#### Database

Needs to intall psql and create a user root with password Password12@!
Create a database django_test.

#### Python Package manager

PIP is required to install necessary libairies listed in requirement.txt

#### Make

Make is recommended to install to run command from Makefile that makes the bash commmand eaiser

## How to run in Local

Install the required python libraries

$ make install

After running the database locally, you can start with database migration.

$ make migrate

Populate fake data, for testing purpose

$ make populate

finally run it :D

$ make run

run tests

$ make test

[Optional] check url list

$ make show_urls

## Diary Log

Initial setup [drf + pip + models + views + serializers + make + databases]: 2 hr

Implement Validation: 1hr 30m

Nested Api: 2hr

sort, search, filter: 1hr

refactor [project structure + fix warning]: 30 mins

add populate file: 10 mins

Heroku deployment and preparation: 1hr



