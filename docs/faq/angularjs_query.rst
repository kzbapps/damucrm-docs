AngularJS Query, получение информации по запросам
=================================================

.. code-block:: javascript

	RestApiService.get('query/get?code=entity_attrs_by_code&param1='+$scope.table_name).
	then(function(data) { 
		$scope.fields = data.data.items;
	});
	
	
Описание полного пути к запросу:

.. code-block:: text

	/restapi/query/get?code=entity_ui_blocks_select&flt$entity_id$eq=38	
	entity_ui_blocks_select - Код запроса
	flt$ использование фильтра
	entity_id - код поля
	eq - равно

		
