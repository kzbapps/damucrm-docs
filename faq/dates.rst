Работа с Датами
=========================
Функция TimeParseFormat

.. code-block:: lua

	currentDate =TimeParseFormat( DBCurrentDateTime(),"2006-01-02 15:04:05","060102")

Дата по умолчанию в AngularJS шаблоне

.. code-block:: javascript

	$scope.detail.doc_at = moment().format("YYYY-MM-DD H:mm:ss");
	
Преобразование в MySQL

.. code-block:: sql

	SELECT DATE_FORMAT("2017-06-15", "%d.%m.%Y");
	>15.06.2017
	SELECT DATE_FORMAT(now(), '%d.%m.%Y %H:%i:%S');
	>10.02.1985 02:00:00
	

Преобразование в AngularJS

.. code-block:: html

	<a class="btn">Format Date {{moment |amDateFormat:"MMMM"}}</a>
	
Short Date Time Format AngularJS

.. code-block:: html

	<div ng-switch-when="due_at" >
		{{row[col.alias] | amDateFormat:session_parameters.shortDateTimeFormat}}        
	</div>	
	
	
Long Date Time Format AngularJS

.. code-block:: html

	<div ng-switch-when="due_at" >
		{{row[col.alias] | amDateFormat:session_parameters.longDateTimeFormat}}        
	</div>		
	
	
Short Date Format AngularJS

.. code-block:: html

	<div ng-switch-when="due_at" >
		{{row[col.alias] | amDateFormat:session_parameters.shortDateFormat}}        
	</div>	

Long Date Format AngularJS

.. code-block:: html

	<div ng-switch-when="due_at" >
		{{row[col.alias] | amDateFormat:session_parameters.longDateFormat}}        
	</div>
	
	
Short Time Format AngularJS

.. code-block:: html

	<div ng-switch-when="due_at" >
		{{row[col.alias] | amDateFormat:session_parameters.shortTimeFormat}}        
	</div>
	
