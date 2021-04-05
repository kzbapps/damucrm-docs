Получение хеша пароля 
============================================================================

.. code-block:: lua

   --Пример кода 

    result = GetPasswordHash ( 
 
                              request.input.pwd 
 
                             )
 
     SqlExec ( 
 
             " update userus set password = ? where  email = ? " ,

             result ,
 
             request.input.send_to

            )