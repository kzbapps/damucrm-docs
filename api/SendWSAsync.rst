Отправка асинхронного WebSocket сообщения через Backend
================================================================================================

.. code-block:: lua
      
    output.errText , --Текст ошибка
         
    output.errNum , --Номер ошибки

.. code-block:: lua
    
    output = {}
 
    output.errText,output.errNum = SendWSAsync (
          
          request.host,
 
          "/ws/ServeMsqToUser",
       
               [
 
                   [  
     
                       { 
                          "data":
                                  {
                                    "ok": true,
 
                                    "accounTitle": "Саумбаев Ельдар Карияевич" ,
 
                                    "phone": "+77772825520",
 
                                    "accountId": 222
                                   }
                           
                           "room" : "9999",
          
                           "type" : "crmIncomingCall",
 
                           "receiver" : 1 
                        }
                  ]
             ]
         )

.. code-block:: lua
  
    output.errText2,
 
    output.errNum2 = SendWSAsync (
    
        GetHTTPListenHostPort (),
 
        "/ws/ServeMsgToUser" ,
 
        JsonToString (
              
              {
 
                 data = {
 
                          ok = true ,

                          title = v.title,
 
                          dscr = v.dscr , 
 
                          task_id = v.id
          
                         } ,

                 room = "9999" ,
 
                 type = "notification" ,
 
                 receiver = v.manager_id*1
        
               } 
           
          )

    )


            
                         
 
                                          
       
           
  
         