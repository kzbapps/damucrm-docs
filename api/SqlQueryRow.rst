Sql Query Row
==============================================================

Параметры

.. code_block:: lua

                errText ,       --Текст ошибки

                errCode ,       --Код ошибки

                Id  ,           --Пользователь

.. code-block:: lua 

       --Пример кода 

     errText , 

     errCode = SqlQueryRow (
 
                            "select x from dual where id = ? " , 
 
                            input.id

                           )
     
     x = 1 