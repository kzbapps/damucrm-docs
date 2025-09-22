Запуск бизнес-процесса из AngularJS
=================================================
.. code-block:: html

	<button class="btn btn-primary"
	ng-click="pubSubPublish('chooseBPMSModal',{callBack:bindCallBack,'processCode':'realty_ap_daily_state_change', input: {ap_id:selected_apartment_id,day_at : formatDate(selected_date,'YYYY-MM-DD')  } })"
	><i class="{{action.action_icon}}"></i>Изменить статус</button>   
	
	
В контроллере должен быть объявлена функция:

.. code-block:: javascript	

	$scope.pubSubPublish = function(a,b){
		PubSub.publish(a,b);
	}