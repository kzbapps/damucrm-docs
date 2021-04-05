Http Get 2
=================================

Параметры

.. code-block:: lua 

          errText ,               --Текст ошибки 

          errNum ,                --Номер ошибки 

.. code-block:: lua

    --Пример:

    local headers = array(
 
                           {
    
                              [ "Content-type" ]  = "application/json" ,

                              ["SoapAction"] = "Create" 
                  
                           }
 
                         )
    
    local data , 

    errText ,

    errNum = HttpGet2( "http://127.0.0.1:9999/restapi/run/test888" ,

                       headers 

                      )


.. code-block:: lua

    --Еще пример:

    local access_token = EntityValueByCode(
 
                                            "remote_cis" ,

                                            "access_token" ,

                                            "crm"
          
                                           )
   
    local url = EntityValueByCode(

                                  "remote_cis" , 

                                  "url" ,

                                  "crm"

                                 )

    local header = array(

                          {
 
                             [ "Authorization"] = "Bearer" ..access_token 

                          }

                        )

Продолжение примера:

.. code-block:: lua    

    local data , errText , errNum = HttpGet2(uri.. "restapi/query/get?code= bi_nomens " , header) 
 
    if errNum ~= 0 then

              print("errText" , errText) 

              output.errText = errText return 
 
              end 
    
    local arr = StringToJson(data)                     
 
