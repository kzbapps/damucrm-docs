DMLI - изменение информации без проверок на доступы.
=======================================================================================================

.. code-block:: lua 

    --Пример кода 

    output = {} , 

    vals = {} ,

    vals.manager_id = 1 ,
 
    vals.due_at = "2017-05-10  18:00:00" ,

    vals.title = "FROM LUA" ,      --Изменение информаций без проверок на доступы. Проверяются валидации.

    
.. code-block:: lua 

     output.id , output.errText , output.errNum = DMLI ("insert" ,"tasks" , 1 ,vals)