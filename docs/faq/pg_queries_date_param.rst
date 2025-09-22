SQL в queries для PostgreSQL для поиска по интервалу дат
===========================================================================

.. code-block:: text

	with params as (select  TO_DATE(?,'YYYY-MM-DD') as par1,TO_DATE(?,'YYYY-MM-DD')+interval '1' day as par2,1 as rn )
	select ... from user_session main
	...
	join params on 1=1
	%filter%
	and main.created_at between params.par1 and params.par2
