Обнулить значения атрибута
=============================================

.. code-block:: sql

	select 'update '||e.code||' set '||ea.code ||'=null;' from entities e
	join entity_attrs ea on 
	ea.entity_link_id = (select id from entities where code='projects') and ea.entity_id =e.id

