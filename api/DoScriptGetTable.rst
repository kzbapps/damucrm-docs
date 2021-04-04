Запуск скрипта и получение результата в виде таблицы
====================================================================================================

.. code-block:: lua
        
        output.errText , --Текст ошибки
 
        output.errNum , --Номер ошибки


.. code-block:: lua 
       
        output = {}
        
        output.res,
      
        output.errText,
     
        output.errNum =  DoScriptGetTable(
                                            
                                             [
                                                 
                                                  [ 
                                                   print("x")
                                                   
                                                   result = {}
                                                   
                                                   result.message = "script"
                                                   
                                                   input.message
                                                   
                                                   result.ok = true 
                                                  
                                                   ]
                                             ],
                          { 
                           "message": "scripthello",
                           
                           "ok" : true
                          }
                      )