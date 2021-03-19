RateLimiter - Ограничение частоты вызова по интервалу
==================================================================================================

Параметры

.. code-block:: lua

	output.errText, --Текст ошибки 
	
	output.errNum = --Номер ошибки. 0 -успех
	
	RateLimiter(
	
		"TEST", --Уникальный код проверки  (Параметр 1)
		
		ip, --Айпи адрес или пользователь. Органичитель (Параметр 2)
		
		"5s", --Интервал в формате golang (Параметр 3)
		
		3 -- Лимит (Параметр 4)
		
		)

Пример для Rest Services ограничить по IP адресу до максимум 3 запуска в 5 секунд
	
.. code-block:: lua

	--Пример по IP адресу в Rest Service
	output = {}

	local ip = request.header["X-Real-Ip"]
	if ip == "" or ip == nil then
		ip =Split(request.RemoteAddr,":")[1]
	end
	output.errText,output.errNum = RateLimiter("TEST",ip,"5s",3)


Пример для Rest Services ограничить по пользователю адресу до максимум 3 запуска в 5 секунд

.. code-block:: lua

	--Пример по IP адресу в Rest Service
	output = {}


	output.errText,output.errNum = RateLimiter("TEST",request.user_id,"5s",3)