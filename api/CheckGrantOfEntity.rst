Check grant of entity - проверка доступа к сущности
=====================================================================================

Параметры

.. code-block:: lua

       errText ,             --Текст ошибки

       errNum ,              --Номер ошибки

.. code-block:: lua

      --Пример

        errText , errNum = CheckGrantOfEntity(

                                              sys.user_id ,

                                              "crm_offers" , 

                                              "is_update" , 

                                              var.pk
                                        
                                              )
