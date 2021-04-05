Send email - отправка Email
==================================================================

Параметр

.. code-block:: lua

  errText ,     --Текст ошибки

  errNum ,      --Номер ошибки
  
  "___"  ,      --Данные 

.. code-block:: lua 
 
  --Пример

  errText ,

  errNum = SendEmail ( 
 
                      "zvanda" ,  --Code of distribution channel 

                      "Ельдар Саумбаев" , --To text 
 
                      "yeldar@bk.ru" , --To Mail 
 
                      "Изменен пароль в CallBack" , --Subject 

                      "HTML test! Регистрация в callback" , --Body 

                      true  --Wait
        
                     )

        