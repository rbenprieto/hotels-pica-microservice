migrate:
	docker compose exec hotels_microservice ./manage.py makemigrations
	docker compose exec hotels_microservice ./manage.py migrate

requirements:
	docker-compose exec hotels_microservice pip install -r requirements.txt

statics:
	docker compose exec hotels_microservice ./manage.py collectstatic --no-input

superuser:
	docker compose exec hotels_microservice ./manage.py createsuperuser

app:
	docker compose exec hotels_microservice ./manage.py startapp $(APP_NAME)

logs:
	docker compose logs -f -t --tail=$(lines) $(service)

mergemigrations:
	docker compose exec hotels_microservice ./manage.py makemigrations --merge

reset:
	docker compose down -v

clean:
	rm -rf src/*/migrations/00**.py
	find . -name "*.pyc" -exec rm -- {} +
	rm -rf src/*/migrations/__pycache__/*

tests:
	docker compose exec hotels_microservice pytest

black:
	docker compose exec hotels_microservice black .