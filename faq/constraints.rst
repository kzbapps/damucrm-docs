Поиск составных индексов
==================================================

.. code-block:: sql

	SELECT 

	#(select 1 from information_schema.TABLE_CONSTRAINTS tc where tc.CONSTRAINT_SCHEMA  = kcu .CONSTRAINT_SCHEMA and tc.constraint_type = 'UNIQUE'  
	#and tc.TABLE_NAME =kcu.table_name and tc.TABLE_SCHEMA=kcu.TABLE_SCHEMA and tc.constraint_name=kcu.CONSTRAINT_NAME limit 1) uniq,
	tc.CONSTRAINT_NAME ,
	kcu.table_name, count(1), tc.constraint_type
	FROM information_schema.KEY_COLUMN_USAGE kcu 
	join information_schema.TABLE_CONSTRAINTS tc on tc.CONSTRAINT_NAME = kcu .CONSTRAINT_NAME  and tc.TABLE_SCHEMA  = kcu .TABLE_SCHEMA  and tc.CONSTRAINT_TYPE ='UNIQUE'
	where
	#kcu.TABLE_NAME  = 'detail_queries'
	#and 
	kcu.table_schema=database()
	group by kcu.table_name,kcu.CONSTRAINT_NAME
	having count(1)>1