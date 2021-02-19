Пример восстановления документов из Аудита:
=========================

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