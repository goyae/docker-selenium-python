SHELL=/bin/sh

u: upd

i: install

c: bash

install:
	docker-compose down --volumes --remove-orphans
	docker-compose build
	docker-compose up -d

bash:
	docker-compose exec selenium bash

upd:
	docker-compose up -d

d:
	docker-compose down

ps:
	docker-compose ps

r: d u bash

test:
	docker-compose exec selenium python test-goyalog.py
