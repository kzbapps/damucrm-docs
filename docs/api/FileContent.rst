FileContent Получить содержимое файла
====================================================================

.. code-block:: lua

       --Пример кода 

       output = {} 
 
       output.filename ,

       output.contentType , 

       output.data , 

       output.errText , 

       output.errNum = FileContent ( 
    
                                     "4894 " , 

                                      1 

                                    )

.. code-block:: json
  
	{

		"contentType" : "image/png" , 

		"data" : "PNG\r\n\u001a\n\u000\u0000\u0000..." , 

		"errNum" : 0 ,

		"errText" : " " , 

		"filename" : " Для рабочего стола.png"

	}
