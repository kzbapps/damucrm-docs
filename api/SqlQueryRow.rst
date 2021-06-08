SqlQueryRow - Получить строку из базы данных в глобальные переменные
====================================================================================================

.. code-block:: lua 

       --Пример кода 

     errText , 

     errCode = SqlQueryRow (
 
                            "select x from dual where id = ? " , 
 
                            input.id

                           )
     
     x = 1 