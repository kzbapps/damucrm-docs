Как сравнить бизнес-процессы
==================================================

Сравнить Результат в Winmerge

Изменения по диаграмме

.. code-block:: sql

	select code,md5(diagram) from bp_processes
	where module_id in (4,6)
	order by code

Изменения по скриптам

.. code-block:: sql

	select id,code, md5(script_txt) script_txt from bp_points
	where is_active = 1
	and process_id  in (select id from bp_processes where module_id in (4,6))
	and script_txt is not null and code like 'ScriptTask%'
	order by code


