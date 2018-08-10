# flask-sqlalchemy-alembic

A proof of concept for getting them to work together.

## Setup

* `cd flask-sqlalchemy-alembic`
* `docker-compose up -d`
* Visit http://localhost:5000

## Alembic

Generate migrations automatically with:
`docker-compose run --rm app alembic revision --autogenerate -m "Your migration message"`

Update the database to the latest migration with:
`docker-compose run --rm app alembic upgrade head` (this also gets run on `docker-compose up`)
