Как ограничить вывод списка DuSelect по значению какого-либо атрибута
====================================================================================================

На примере ограничения вывода атрибутов в фильтре (filter_sets)

Создадим новый SQL запрос (queries), назовем entity_atts_select_by_set_id, в котором пропишем условие

.. code-block:: sql

	entity_id.id =( select entity_id from filter_sets where id=?)

? означает, что сюда нужно передать значение param1.

Если ? несколько, то нужно в таком же порядке передать param2,param3 и т.п.

Полный запрос:

.. code-block:: sql

	select concat(main.code, ' - ',main.title) as name,
	main.sys$uuid as "sys$uuid", entity_id.code as entity_id$code,entity_link_id.code as entity_link_id$code,
	 
	main.data_type_id as data_type_id,
	main.entity_id as entity_id,
	main.entity_link_id as entity_link_id,
	main.id as id, concat(entity_id.code,' ',entity_id.title) as "entity_id$",data_type_id.title  as "data_type_id$",concat(entity_link_id.code,' ',entity_link_id.title) as "entity_link_id$" from entity_attrs main
	  
	left join entities entity_id on entity_id.id=main.entity_id 
	left join data_types data_type_id on data_type_id.id=main.data_type_id 
	left join entities entity_link_id on entity_link_id.id=main.entity_link_id   

	  %filter% 
	  
	  and
	  
	  entity_id.id =( select entity_id from filter_sets where id=?)
	  %order% 
  

В настройках сущности filter_sets, в атрибут attr_id добавьте параметр компонента query_code со значением, в котором передается param1:

.. code-block:: javascript

	entity_attrs_select_by_filter_set_id&param1={{detail.set_id || detail.id}}
	
	
Почему прописано именно detail.set_id || detail.id?


В случае, если открыта страница Фильтра (filter_sets), то доступна переменная detail.set_id, а если открыта страница детализации фильтра filter_set_dtls, то detail.set_id уже не существует,
 но есть основной detail.id
 
 