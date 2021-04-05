Получение результата запроса
====================================================================================

Параметры

.. code-block:: lua 

            errText ,        --Текст ошибки

            errCode ,        --Код ошибки

.. code-block:: lua 

   --Пример 

           outputVal ,

           errText , 

           errCode = SqlQueryRows (

                                   "select id ,
 
                                    title from users where id = ? " , 

                                    1 
             
                                   )
      
           output = array (outputVal)