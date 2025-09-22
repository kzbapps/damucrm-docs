QRCodeBase64 - Формирование QR Кода из шаблона страницы или lua
=======================================================================================================

Из шаблона

.. code-block:: text

	<p>Подлинность коммерческого предложения: <br />
		<img style="margin:2px" width="100" height="100" src="data:image/png;base64,{{ QRCodeBase64  (print   (GetParamValue "cloud_url")  "restapi/getfile?code="  $last_file_uuid "&attachment=true")  2 500 }}" />
	</p>
	
Из Lua
	
.. code-block:: lua
	
		 base64data,errText,errNum = QRCodeBase64  (GetParamValue ("cloud_url")..  "restapi/getfile?code=" .. last_file_uuid .. "&attachment=true", 2 , 500)
