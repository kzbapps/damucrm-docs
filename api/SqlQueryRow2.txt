Sql query row  2 
================================================

Параметры 

.. code-block:: lua 

    errText ,          --Текст ошибки

    errCode ,          --Код ошибки

    Id ,               --Пользователь

.. code-block:: lua 

    --Пример 

     local found ,

     errText ,

     errCode = SqlQueryRow2 ( 
 
                             "select title from users where id =?" , 

                             var.id 

                             )

     "HTMLEscapeString (
                 
                         (
        
                            found.title or "" 
 
                          )

                        ) "
 

    