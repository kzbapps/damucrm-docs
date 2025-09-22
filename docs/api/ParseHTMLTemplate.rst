ParseHTMLTemplate - Обработка HTML шаблона
==========================================================================



.. code-block:: lua 

   --Пример

   test = {} 
 
   test.text = "test123"

   output = {} output.res , 

   output.errText , 

   output.errNum = ParseHTMLTemplate( "{
                                    
                                     { .text}
                                   
                                    }" ,
                                 
                                 test , request.user_id
                                
                                )
   

Результат

.. code-block:: text
   
   test123
   

Еще пример

.. code-block:: lua 
 

    test = {} test.text = "test123" 
  
    output = {} output.res ,

    output.errText, 
 
    output.errNum = ParseHTMLTemplate ( " { { .text} }    { { lua\"hello_world2\" 111222 }} " ,

                                    test ,
  
                                    request.user_id
 
                                  )                 

Результат

.. code-block:: text
