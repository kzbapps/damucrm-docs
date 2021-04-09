Check grant of entity - проверка доступа к сущности
=====================================================================================


.. code-block:: lua

      --Пример

        errText , errNum = CheckGrantOfEntity(

                                              sys.user_id ,

                                              "crm_offers" , 

                                              "is_update" , 

                                              var.pk
                                        
                                              )
