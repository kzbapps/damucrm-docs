Parse template - обрабатывание шаблона
==========================================================================

Параметры

.. code-block:: lua

   errText ,              --Текст ошибки

   errNum  ,              --Номер ошибки

   {} ,            --Проведение документа

.. code-block:: lua 

   --Пример

   test = {} test.text = "test123"

   output = {} output.res , 

   output.errText , 

   output.errNum = ParseTemplate( "{
                                    
                                     { .text}
                                   
                                    }" ,
                                 
                                 test , request.user_id
                                
                                )
   
   output.res = "test123"

.. code-block:: lua 
 
    --------------------------------Пример вызова lua-------------------------------

    test = {} test.text = "test123" 
  
    output = {} output.res ,

    output.errText, 
 
    output.errNum = ParseTemplate ( " { { .text} }    { { lua\"hello_world2\" 111222 }} " ,

                                    test ,
  
                                    request.user_id
 
                                  )                 --output.res = "test123"                                   