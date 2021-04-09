Вызов Sql блока с поддержкой in/out параметров
=========================================================================================


.. code-block:: lua

     --Пример кода 

    output = {} ,

    output.i ,

    output.errText ,

    output.errNum = SqlCall (

                                [

                                     [ begin select created_at into : id from  users where id = 1 ;

                                       end;
  
                                     ]

                                ] ,
        
                                { id = {  input = false ,

                                          output = true , 
 
                                          value = "99" ,

                                          clob = false 

                                        }

                                 }

                              )

.. code-block:: lua 

     [  [  result  { 

                     "errNum" : 0 , 

                     "errText": " " ,

                     "i" : {
 
                             "id": "2017-03-21  20:01:13"

                           }
                   
                   }

        ]

     ]

