SqlQueryRows - Получение результата запроса
====================================================================================

.. code-block:: lua 

   --Пример 

           outputVal ,

           errText , 

           errCode = SqlQueryRows (

                                   "select id ,
 
                                    title from users where id = ? " , 

                                    1 
             
                                   )
      
           