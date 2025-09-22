Работа с JSON в lua
=========================

Чтение значений из JSON строки

.. code-block:: lua

	local jsonpath=require("pkg/jsonpath")    
	local accReqs,ers,ern=jsonpath.Read(resJson,'$.Envelope.Body.SendMessageResponse.response.responseData.data.R01.items')
