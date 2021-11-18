createenv:
	python3 -m venv devduo-env
setenv:
	source ../devduo-env/bin/activate
createproject:
	django-admin startproject djangoproject
createapp:
	./manage.py startapp devduo
installenv:
	pip3 install django-environ
installpsycopg2:
	pip3 install psycopg2-binary
remotedb:
	docker exec -it djangoproject_db_1 /bin/bash
psql:
	psql -d devduo -U root -W
dbup:
	docker-compose -f docker-compose.yml --env-file ./djangoproject/.env up -d
dbdown:
	docker-compose -f docker-compose.yml down --volumes
initdb:
	python manage.py migrate
	python manage.py test