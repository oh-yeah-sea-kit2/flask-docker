NAME=flaskapp

run:
	docker-compose build
	docker-compose up -d

stop:
	docker-compose down

status:
	docker-compose ps

run-no:
	docker-compose build --no-cache
	docker-compose up -d
