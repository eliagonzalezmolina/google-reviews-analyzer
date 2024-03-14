include .env

pre-commit:
	pre-commit run --all-files
install:
	poetry install
	pre-commit install # it fails if shell is not reset. TODO: fix it
dvc-init:
	dvc init
	mkdir -p ${DVC_REMOTE_PATH}/${PWD##*/}
	dvc remote add -d myremote ${DVC_REMOTE_PATH}/${PWD##*/}
