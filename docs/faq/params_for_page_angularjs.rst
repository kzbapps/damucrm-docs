Принять параметры в страницу
==================================================================================================

Например, передать ID процесса, дату начала, дату окончания

.. code-block:: javascript

	if (Metronic.getParameterByName("df_process_id")!=null && Metronic.getParameterByName("df_date1")!=null && Metronic.getParameterByName("df_date2")!=null){
		$scope.process_id = Metronic.getParameterByName("df_process_id");    
		$scope.date1 = Metronic.getParameterByName("df_date1");
		$scope.date2 = moment(Metronic.getParameterByName("df_date2"), "YYYY.MM.DD").add(1,'days').format("YYYY-MM-DD");
	}else{
	$scope.date1 = moment().format("YYYY-MM-DD");
	$scope.date2 = moment().add(1,'days').format("YYYY-MM-DD");
	}