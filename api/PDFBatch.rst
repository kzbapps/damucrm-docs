PDFBatch - обработка PDF файла
=============================================================================

.. code-block:: lua 

       --Пример кода
 
       output - {} 

       left = 8

       Top = 4
  
       Right = 2 

       Bottom = 1

       Center = 16 
 
       Middle = 32

       t = {} 

       output.errText , 

       output.errNum = PDFBatch ( 

                                 [ [ h:\project\pdft-master\test\pdf\pdf_from_docx.pdf ] ]  ,

                                      (
               
                                          {

                                              { action = "AddFont" , 

                                                param1 = " arial" ,

                                                param2 = [ [ h:\project\pdft-master\test\ttf\arial.ttf ] ] 
 
                                              } , 
              
                                              { action = "SetFont" ,

                                                param1  = "Arial" , 
   
                                                param2 = " " , 

                                                param3 = 14 
 
                                              },

                                              { action = "Insert",

                                                param1 = "Привет!!!"

                                                param2 = 1 ,

                                                param3 = 40 ,
  
                                                param4 = 10 ,

                                                param5 = 100 ,

                                                param6 = 100 , 

                                                param7 = Right + Center 
           
                                              },

                                              { action = "InsertImg" , 

                                                param1 = [ [ h:\projects\pdft-master\test\img\gopher.png ] ] ,

                                                param2 = 1 ,

                                                param3 = 400 , 
 
                                                param4 = 100 , 

                                                param5 = 200 , 

                                                param6 = 200
 
                                              } ,

                                              { acion = "Save" , 
 
                                                param1 = "c:\\temp\\222.pdf" 
                   
                                              },

                                       }  

                             )
  
               )
                                
     