include .env

PROJECT_NAME := $(shell basename "$(PWD)")

install:
	poetry install
pre-commit-init:
	pre-commit install
dvc-init:
	dvc init
	mkdir -p ${DVC_REMOTE_PATH}/${PROJECT_NAME}
	dvc remote add -d myremote ${DVC_REMOTE_PATH}/${PROJECT_NAME}
pre-commit:
	pre-commit run --all-files
