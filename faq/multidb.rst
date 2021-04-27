Поддержка разных СУБД. Примеры универсальных SQL
==================================================================================================

Агрегация строк

.. code-block:: text

	{{if .Oracle}}LISTAGG(o.title,', '){{else}}GROUP_CONCAT(o.title SEPARATOR ', '){{end}}

rownum, limit

.. code-block:: text

	{{if .Oracle}}and rownum = 1{{else}}limit 1{{end}}
	
	
decode, nvl

.. code-block:: sql

	case when coalesce(ip_fl,'0')='1' then 'ИСТИНА' when coalesce(ip_fl,'0')='0' then 'ЛОЖЬ' else 'НЕКОРРЕКТНО' end
	
	