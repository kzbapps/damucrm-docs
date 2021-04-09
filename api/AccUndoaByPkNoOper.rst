Отмена проведения документа
====================================================================================





.. code-block:: lua
 
  --Пример

  id = 56 errText , 

  errNum = SqlQueryRow (
                     
           "select id as entity_id from entities where code = 'erp_doc_sales' "
            
            ) 
    
   if errNum ~= 0  then
 
      errText , 
 
      errNum = AccUndoByPkNoOper(
 
                  entity_id ,
 
                  id

                  )
   
      end