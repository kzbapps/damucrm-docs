RegexpFindAllStringsAndJoin - найти подстроки и склеить
==============================================================================

Пример поиска телефонов

.. code-block:: lua 

	v[phone_f] = RegexpFindAllStringsAndJoin("[0-9|,]+",v[phone_f],-1,"")