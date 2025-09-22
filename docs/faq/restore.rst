Пример восстановления документов из Аудита
==================================================

В MariaDB

.. code-block:: sql

	select
	concat('insert into qol_docs (id,',group_concat(col order by tld.id),') values (',tl.pk,',',group_concat(
	case when val is null then
	'null' else concat('''',coalesce(val,''),'''')  end
	order by tld.id),');')  from table_log_dtls tld
	join table_logs tl on tl.id=tld.log_id
	where tl.pk in
	(
	select tl.pk from table_logs tl
	where table_name='qol_docs' and id in
	(select log_id from table_log_dtls where
	col='ext_account_id' and val in ('27213','28097','29050','29060'
	) )
	)
	and tl.table_name ='qol_docs'
	order by tl.id desc
	group by tl.pk,tl.id
	
	
В PostgreSQL пример восстановления удаленных шаблонов:

.. code-block:: sql

	select 
	concat( 'insert into ', tl.table_name, ' (id,',
	(select string_agg (col,',' order by d.id) from table_log_dtls d where d.log_id=tl.id and d.col<>'its_contract_tpl_id' and d.col not like '%$%'),')',
	'values (',tl.pk,',',
	(select string_agg (concat(case when val  is null then 'NULL' else ''''||val||'''' end),','  order by d.id) from table_log_dtls d where d.log_id=tl.id and d.col<>'its_contract_tpl_id' and d.col not like '%$%')
	,');')
	 from table_logs tl where user_id=38919 and table_name='its_contract_tpl_var'
	and not exists(select 1 from its_contract_tpl_var where id=tl.pk)

	and tl.id = (select max(id) from table_logs tl2 where tl2.pk = tl.pk and tl2.table_name  = tl.table_name)
