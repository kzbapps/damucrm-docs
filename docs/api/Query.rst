Query - получение данных по запросу с входными параметрами.
================================================================================================



.. code-block:: lua

      --Пример
 
      arr , errText ,errNum = Query (
                                     "?code = bp_processes&infit $main.module_id = (0.1)&" ,
                                     request.user_id
                                    )
      

.. code-block:: lua
      
      --Результат

      output = array(arr) [
                             [
                                {"output" : [ 
                                               {"code":"happyBirthDayVoice" ,
                                                "id" : "24" ,
                                                "module_title": "CRM" ,
                                                "title":"С днем рождения" 
                                                },
                                                
                                                {"code": "processData",
                                                 "id": "33" ,
                                                 "module_title": "CRM" ,
                                                 "title": "Обработка массововй информации"
                                                 }
                                              ] ,
                                  
                                  "resultText": "Service Ok" ,
                                  "resultCode": "0" , 
                                  "hasError" : false
                                 }
                             ] 
                        ]
 
                                                 
 
                                                 
