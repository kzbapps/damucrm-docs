QueryEscape  - экранирует строку
================================================================================================================================================================================================

QueryEscape экранирует строку, чтобы ее можно было безопасно разместить

внутри URL-запроса.


.. code-block:: lua

      --Пример
 
      output = QueryEscape (" ")
      

.. code-block:: lua
      
      --Результат

      output = "%20"

