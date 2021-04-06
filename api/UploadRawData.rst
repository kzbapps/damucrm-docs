Upload raw data - загрузка файла в ECM.
===================================================================================

Параметры

.. code-block:: lua

    errText ,                --Текст ошибки
 
    errNum ,                 --Номер ошибки

    output ,                 --Проведение документа


.. code-block:: lua

    --Пример кода

    output.uuid ,

    output.errText ,
 
    output.errNum = UploadRawData(

                                  "COL_AD" ,

                                  "file.pdf" ,

                                   s

                                  )