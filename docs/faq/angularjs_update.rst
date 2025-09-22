Сохранение записей
=================================================

.. code-block:: javascript

	DMLService.update(  [ {table_name:$scope.table_name,action:$scope.action, values: [$scope.detail]}  ]).
		success(function (data) {
			if (data.error!="0") {
				$scope.error_code = data.error_code;
				$scope.error_text = data.error_text;
				Metronic.stopPageLoading();
				return;
			}
			if ($scope.detail.id == 0) {
				data.items.forEach(function (item, i, arr) {
					if (item.table_name==$scope.table_name){
						location.href = "#\/erp\/erp_doc_invoicesdetails/" +item.last_insert_id;
						Metronic.stopPageLoading();
						$scope.closeEdit();
					}
				});
			}else{
				Metronic.stopPageLoading();
				$scope.bind();
			}
		});
		
В качестве action может выступать:
	1)"update"
	2)"insert"
	3)"delete"
	4)"upsert" (нужно передавать upsert_attrs (Ключи обновления), например "upsert_attrs":["code","email"])
