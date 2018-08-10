# flask-sqlalchemy-alembic

Generate migrations automatically with:
`docker-compose run --rm app env PYTHONPATH=. alembic revision --autogenerate -m "Your migration message"`

You need to set `PYTHONPATH` otherwise alembic's env.py doesn't know where to import `models` from.
