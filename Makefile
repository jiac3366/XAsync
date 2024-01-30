N ?= 4

.PHONY: venv
venv:
	test -d venv || test -n "${VIRTUAL_ENV}" || python3 -m venv venv

.PHONY: worker
worker: venv
	celery -A mo_tasks worker -l INFO -c"$(N)"

.PHONY: beat
beat: venv
	celery -A mo_tasks beat --scheduler django_celery_beat.schedulers:DatabaseScheduler -l INFO

.PHONY: dist
dist: venv
	venv/bin/pip install -U setuptools wheel
	venv/bin/python setup.py bdist_wheel --universal

install: venv
	venv/bin/pip install --force-reinstall ./*.whl
