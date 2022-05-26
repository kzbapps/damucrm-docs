Установка Приложения DamuBPM через docker
================================================================================================================================================

1. Установите базу данных локально и восстановите локальный дамп:

.. code-block:: bash

	psql
	postgres=#create user demo_test with password 'demo_test';
	postgres=#create database demo_test owner demo_test;
	postgres=#exit;
	psql -d demo_test
	postgres=#create extension if not exists "uuid-ossp";
	postgres=#exit;
	pg_restore -U demo_test --verbose --host=localhost --port=5432 --format=c --dbname=demo_test dump-demo.sql

2. Создать файл docker-compose.yaml с содержимым:

.. code-block:: text

	version: "3.1"
	services:
	  frontend:
		image: damubpm/frontend
		ports:
		 - 28080:28080
		depends_on:
		  - "core"

	  core:
		image: damubpm/core
		hostname: service-core
		container_name: core
		environment:
		  - DAMU_LICENSE=YOUR_LICENSE		
		  - CRM_DB_TYPE=pgsql
		  - DAMUCRM_SALT=YOUR_RANDOM_SALT
		  - CRM_DB_CONN_STR=postgres://demo_test:demo_test@host.docker.internal:5432/demo_test?sslmode=disable
		  - OPENSHIFT_GO_IP=0.0.0.0
		  - OPENSHIFT_GO_PORT=19999
		  - OPENSHIFT_APP_NAME=damucrm
		  - LD_LIBRARY_PATH=:/opt/kalkancrypt/:/opt/kalkancrypt/lib/engines

3. запустить в этой же папке, где файл docker-compose.yaml

.. code-block:: text	

	docker-compose up
