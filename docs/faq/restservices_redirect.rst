Как сделать редирект(redirect) на вход по временному Auth Token в Rest Services
====================================================================================================

Укажите Content-Type: text/html. 

В output укажите следующий скрипт.

.. code-block:: lua

	output = [[<html><head>
		<meta http-equiv="refresh" content="1;URL=]].. GetParamValue ("cloud_url").. "restapi/loginByToken/" .. token .. [[" />
		</head>
		<body>
		</body>
		</html>
		]]