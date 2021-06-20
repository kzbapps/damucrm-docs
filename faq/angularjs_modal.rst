Работа с модальными окнами AngularJS 
==================================================================================================
Вызов диалогового окна с передачей wh_id

.. code-block:: javascript

	$scope.pubSubPublish("openDetailModal", {withoutGo:true,callBack:function(params){ $scope.addNomenCallBack(params) },data: {id:0,wh_id:$scope.detail.wh_id}, page:"erp_nomen_tree_lookup"});
	
CallBack:

.. code-block:: javascript

	$scope.addNomenCallBack = function(params){
		console.log('selectNomen',params);
		$scope.details.ns.push({_inserted:1, id:0,doc_id:$scope.detail.sys$uuid,nomen_id:params.id,_nomen_title:params.title,quantity:1,price:params.price,amount:params.price});
	}

Открытие модального окна с переходом по URL:

.. code-block:: html

	<a  href="#/crm/dealsdetails/0"  ng-click='pubSubPublish("openDetailModal", {data: {id:0}, page:"dealsdetails"});' type="button" class="btn btn-fit-height btn-primary" translate>
		Add<i class="fa fa-angle-down"></i>
	</a>

Еще пример:

.. code-block:: html

	<a ng-if="row.title" href="#/crm/dealsdetails/{{row.id}}" ng-click='pubSubPublish("openDetailModal", {data: row, page:"dealsdetails"});'> 
		{{row[col.alias]}}
	</a>
	
Обработка выбора внутри модального окна

.. code-block:: html

    <td><a  ng-click="parentCallBack($parent,item)"> <translate>Choose</translate></a></td>

.. code-block:: javascript

	$scope.parentCallBack = function(parent,user){
	  parent.closeWithParams(parent.modals[parent.current],user);          
	}

Получение основной детальной информации из модальной страницы
.. code-block:: javascript

	if ($scope.$parent.modals[$scope.$parent.current].detail
	&&
	$scope.$parent.modals[$scope.$parent.current].detail.cat_id$code == "warning_do_3"
	)
	{
		uri = "query/get?code=etg_staff_warning_by_code_title&perpage=100&page=1&param1="+$scope.searchTitle+"&param2="+$scope.searchTitle;
	}
