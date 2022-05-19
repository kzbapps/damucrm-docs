Очистка базы
==================================================================================================

.. code-block:: sql

	truncate table k2extreq_refuse cascade;
	truncate table k2acc_lock cascade;
	truncate table k2inforeq_rzap cascade;
	truncate table k2rzap_check cascade;
	truncate table k2inforeq cascade;
	truncate table k2mtfile cascade;
	truncate table k2extreq cascade;
	truncate table k2extacc cascade;
	truncate table k2extaccreqdtl cascade;
	truncate table k2extaccreq_plan cascade;
	truncate table k2extaccreq cascade;
	truncate table k2loan_accmov_r;
	truncate table k2loan_accmov;
	truncate table k2loan_pay;
	truncate table k2req cascade;
	truncate table k2loan_out;
	truncate table k2loan cascade;
	truncate table k2ignore cascade;
	truncate table k2anl_income cascade;
	truncate table k2acc cascade;
	truncate table k2file cascade;
	update k2bank set cli_id =null;
	alter table K2BANK   disable constraint FK_K2BANK_CLI_ID;
	truncate table k2cli cascade;
	alter table K2BANK   enable constraint FK_K2BANK_CLI_ID;
	insert into k2cli (code,title) (select bin,title from k2bank where bin is not null);
	update k2bank b set cli_id=(select id from k2cli where code=b.bin);