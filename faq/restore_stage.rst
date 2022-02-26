Пример восстановления Stage Базы из google диска
==================================================

Запускаем psql

.. code-block:: bash

	psql -U postgres

Создаем базу

.. code-block:: bash

	drop database stage_eokno2;
	CREATE USER stage_eokno2 WITH password '*******';
	create database stage_eokno2 owner stage_eokno2;
	exit;

Заходим в базу под пользователем

.. code-block:: bash

	psql -U stage_eokno2 -d stage_eokno2

Создаем extension

.. code-block:: bash

	create extension "uuid-ossp";
	exit;

Восстанавливаем базу 

.. code-block:: bash

	pg_restore.exe -U stage_eokno2 --verbose --host=localhost --port=5432 --format=c --dbname=stage_eokno2 f:\Media\drive.google.com\****\****\eokno2\eokno2_2022-02-27-00-11-43

