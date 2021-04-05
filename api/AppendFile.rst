Append file 
==================================

Параметр

.. code-block:: lua

       errText ,                --Текст ошибки
  
       err.Num ,                --Номер ошибки

Дозапишет в файл . А если файла не существует , то создаст : 

.. code-block:: lua 

   errText, errNum = AppendFile ( " C:\\apps\\2.txt", "data3")