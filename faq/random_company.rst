Установить случайное поле в таблицу postgresql
==================================================================================================

.. code-block:: text

	do
	$$
	declare rec record;
	begin
		for rec in (select id from users) loop
		update users set company_id  = (select id from companies order by random() limit 1) where id=rec.id;
		end loop;
	end;
	$$
