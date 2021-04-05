Получение детальной информации по записи по ID
============================================================================================================

Параметр

.. code-block:: lua 

   errText , --Текст ошибки

   errNum , --Номер ошибки
   
   user_id , --Пользователь

   key , --ключ подключения

.. code-block:: lua

    --Пример

     local arr ,

     errText ,
  
     errNum  = Detail(
 
         var.pk ,
 
         "account" ,
 
         sys.user_id
 
         )
 
      for key ,
 
      value in pairs (arr) do 

          pseudocode arr [key] = array (arr [key] )
 
          end