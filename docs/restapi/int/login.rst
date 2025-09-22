login - Вход в систему
=============================================================================

Вход в систему с получением токена входа
-----------------------------------------------

Запрос:

POST /restapi/login

.. code-block:: json

	{
	"login": "admin",
	"password": "123456789",
	"system": "browser",
	"getToken": true
	}

Ответ:


.. code-block:: json

	{
	   "Result": "ok",
	   "RedirectURL": "",
	   "AuthToken": "0e75b741-c17f-41c2-b86d-e6a3bddc45f6"
	}
	
Токен выдается на  45 дней

