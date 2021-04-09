Sql Query Row  2 
================================================


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
 

    