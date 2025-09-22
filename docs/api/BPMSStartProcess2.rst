BPMSStartProcess2 - Запуск процесса и связывание его с основным процессом
============================================================================================================

-Внимание!Вызываемый процесс не должен содержать ManualTasks (usertasks,timer), т.к. будет разрыв цепочки  подпроцесса.

.. code-block:: lua

     inputVars = {}
     
     inputVars.var = "7777"
     
     output = {}
     
     output = {}

.. code-block:: lua

     output.output , 
     
     output.instanceId , 
     
     output.taskId , 
     
     output.errText ,  
     
     output.errNum = BPMSStartProcess2 ( 
             
                                       "test_new" ,
                                      
                                       1,
                          
                                       inputVars,
              
                                       sys.instance_id
             
                                       )

.. code-block:: lua
     
     response [
                 
                  [
                      {
                       
                        "output": {
                                 
                                  "errNum": 0, 
                                 
                                  "errText": "" ,
                                 
                                  "instanceId": 5669,
                                 
                                  "output" : {
                                                
                                             "var2": "test4444477777"
                                              
                                             } ,
                                  
                                  "taskId": "XXX-XXX" 
                                 
                                   },
                       
                       "resultText": "Service OK",
                       
                       "resultCode": "0",
                       
                       "hasError": false 
                       
                       }
                  
                   ]
              ]
                                 