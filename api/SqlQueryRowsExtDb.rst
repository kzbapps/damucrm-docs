Sql query rows extdb - получить выборку данных из внешней базы данных
==========================================================================================================================

Параметры

.. code-block:: lua

    output = {} ,        --1 параметр: указываем код внешней базы данных из таблицы

    extbd ,              --2 параметр: указываем на SQL запрос

    ..N ,                --3 параметр: указывает значения , которые биндим

.. code-block:: lua

     --Пример кода
 
     arr , output.error_text ,

     output.error_code = SqlQueryRowsExtDb(
 
                                           "mssql" ,

                                           "Select * from users where id = ? and id =?" ,

                                           1,
 
                                           2
 
                                          )

     output.arr = array(arr)  