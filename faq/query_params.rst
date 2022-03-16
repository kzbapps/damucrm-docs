Использование параметров (preparam,param) в запросах
====================================================================================================

Пример url:

.. code-block:: text

	https://example.com/restapi/query/get?code=users_preparam_test&perpage=100&page=1&getRowById=3444&selectContains=ad&preparam1=11111&preparam2=11111&param1=1&param2=2

Запрос:

.. code-block:: sql

	with preparam as (select ? as preparam1,? as preparam2)

	select 

	preparam.preparam1,
	preparam.preparam2,

	main.id from users main
	join preparam on 1=1

	%filter%

	and ? = 1 and ? = 2


	%order%
	
Пояснения:

1. Перед %filter% передаются preparam1...preparamN

2. После %filter% передаются param1...paramN

3. Порядок binding ? слева направо.


