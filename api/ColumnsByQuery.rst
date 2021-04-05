Columns by query - получение поля запроса по SQL
============================================================================================

Параметры

.. code-block:: lua

        errText ,              --Текст ошибки 

        errNum ,               --Номер ошибки

.. code-block:: lua
   
    --Пример:

    output = {} data ,

    output.errText ,

    output.errNum = ColumnsByQuery( 

                                   "select id ,

                                    title from users where 1 = ? "

                                   )
   
    output.data = array (data)

    --Результат:

    {"data" : [
 
               "id" ,

               "title" 

              ] ,

     "errNum" : 0 ,

     "errText": "" 

     }
   
 

 




