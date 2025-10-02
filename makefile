_create_venv:
	python -m venv .venv

_install_requirements:
	pip install -r source/requirements.txt

# User functions
local_setup:
	make _create_venv
	make _install_requirements

docker_startup:
	mkdir ../log -p
	docker compose down
	docker compose build --no-cache
	docker compose up -d
	docker system prune -fa

docker_shutdown:
	docker compose down
	docker system prune -fa