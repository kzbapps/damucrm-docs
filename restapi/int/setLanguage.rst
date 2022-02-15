setLanguage - Установить язык в сессии
=============================================================================

Запрос:

.. code-block:: text


	POST /restapi/setLanguage

	Cookie: BAPPSSessionId=MTY0NDkw....

.. code-block:: json

	{"lang": "ru"}

Ответ:


.. code-block:: text

	Set-cookie: BAPPSSessionId=MTY0NDkwMjI4M...

.. code-block:: json

	{"result":true,"lang":"ru"}

