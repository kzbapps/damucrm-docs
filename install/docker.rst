Установка Приложения DamuBPM через docker
================================================================================================================================================

1. Создать файл docker-compose.yaml с содержимым:

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



2. запустить в этой же папке, где файл docker-compose.yaml

.. code-block:: text	

	docker-compose up

	

