Установка первоначального дампа базы данных DamuCRM с модулем K2 (Картотека обременений №2) на Red Hat Enterprise Linux Server release 7.9 (Maipo)
===============================================================================================================================================================

1. Создадим роль

.. code-block:: postgres

	CREATE ROLE bapps NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT LOGIN PASSWORD '***********';

2. Создадим новую базу

.. code-block:: postgres

	create database bapps owner bapps;


3. Подключимся к базе и включим расширение uuid-ossp

.. code-block:: postgres

	create extension "uuid-ossp";


4. Подключимся к базе и добавим функцию func_updated_at

.. code-block:: postgres

	CREATE OR REPLACE FUNCTION public.func_updated_at()
		RETURNS trigger
		LANGUAGE plpgsql
	AS $function$
		BEGIN
			new.updated_at = now();
			return new;
		END;
	$function$
	;
	
5. Установим дамп	

.. code-block:: bash

	pg_restore.exe -U bapps --verbose --host=localhost --port=5432 --format=t --dbname=bapps dump-bapps-202108160330.sql


