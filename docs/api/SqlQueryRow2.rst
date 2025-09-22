SqlQueryRow2 - Получить строку из базы данных в переменную
================================================================================================


.. code-block:: lua 

    --Пример 

     local found ,

     errText ,

     errCode = SqlQueryRow2 ( 
 
                             "select title from users where id =?" , 

                             var.id 

                             )