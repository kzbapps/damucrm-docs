CSV read
======================================================================

Параметры

.. code-block:: lua 

           contentType ,     --Тип контента
 
           errText ,         --Текст ошибки

           errNum ,          --Номер ошибки
          
           Id ,              --Пользователь

.. code-block:: lua 

    --Пример кода 

        filename , 
 
        contentType ,
 
        s ,
 
        errText , 

        errNum = FileContent ( var.file_id ,

                               sys.user_id 
    
                              ) 

        if errNum ~= 0 then 

                 var.last_error = errText return  end values ,

                 errText , 

                 errNum = CSVRead ( s , ";" ) 

                         if errNum ~= 0 then 
 
                                 var.last_error = errText return end map = {} 
 
                                 for k , v in pairs (values ) do 
 
                                 if k == 1 then 
  
                                         for k1 , v1  in pairs (v) do map [v1] = k1 end 

                                         else a = 1 
                    
                                         end
          
                                  end
 
                               