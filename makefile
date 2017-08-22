release: pull collectstatic migrate

pull:
	git pull

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic

run:
	/home/xcorter/env/purple/bin/python3 /home/xcorter/env/purple/bin/gunicorn purpleServer.wsgi -b 127.0.0.1:8004
