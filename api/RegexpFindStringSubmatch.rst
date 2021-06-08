RegexpFindStringSubmatch - поиск подстроки.
==============================================================================

.. code-block:: lua 

   output.zapros = RegexpFindStringSubmatch(

                                            "Запрос № : 1234567 ;

                                             Регион : Петропавловск ;

                                             Luno :12345678 " ,
                                             
                                             [ [ Запрос №: 123456789\Регион:Петропавловск\Luno:12345678 , 1]  ]
   
.. code-block:: lua 

   output.luno = RegexpFindStringSubmatch (

                                            "Запрос №: 1234567; 

                                             Регион: Петропавловск ;

                                             Luno: 12345678" ,
 
                                             [ [ Запрос №: 123456789\Регион:Петропавловск\Luno:12345678 , 2]  ]

 
.. code-block:: lua 

   output.luno = RegexpFindStringSubmatch (

                                            "Запрос №: 1234567; 

                                             Регион: Петропавловск ;

                                             Luno: 12345678" ,
 
                                             [ [ Запрос №: 123456789\Регион:Петропавловск\Luno:12345678 , 3]  ] 

.. code-block:: lua 

  --Результат:

   [ [ result {
 
               "luno" : "12345678" , 

               "region" : "Петропавловск" , 

               "zapros" : "1234567"
 
              },
     ]
   ]