Работа с Датами
=========================
Функция TimeParseFormat

.. code-block:: lua

	currentDate =TimeParseFormat( DBCurrentDateTime(),"2006-01-02 15:04:05","060102")

Дата по умолчанию в AngularJS шаблоне

.. code-block:: javascript

	$scope.detail.doc_at = moment().format("YYYY-MM-DD H:mm:ss");
	$scope.date1 = moment().format("YYYY-MM-DD");
	$scope.date2 = moment().add(1,'days').format("YYYY-MM-DD");
	
Преобразование в MySQL

.. code-block:: sql

	SELECT DATE_FORMAT("2017-06-15", "%d.%m.%Y");
	>15.06.2017
	SELECT DATE_FORMAT(now(), '%d.%m.%Y %H:%i:%S');
	>10.02.1985 02:00:00
	
Преобразование в PostgreSQL

.. code-block:: sql

	 select to_char(now(), 'dd.MM.YYYY HH24:MI:SS') 
	>19.02.2021 13:02:06
	
	 select to_char(now(), 'YYYY-MM-dd HH24:MI:SS') 
	>2021-03-06 13:12:36	
	
	 select TO_DATE('2021-03-06 00:00:00','YYYY-MM-dd HH24:MI:SS') 
	>2021-03-06	
	
Добавить дни, часы, минуты к текущей дате

.. code-block:: sql

	update table1 set due_date =    
    NOW() + make_interval(days=> coalesce(t2.timer_day,0)::int) 
     + make_interval(hours=> coalesce(t2.timer_hour,0)::int )
     + make_interval(mins => coalesce(t2.timer_min,0)::int )	
	from table2 t2
	
Для вывода строчной даты на русском в postgresql в шаблоне экспорта ,  например, 10 февраля 1985

Перед вызовом нужно установить lc_time

.. code-block:: lua

	if os.getenv("CRM_DB_TYPE")=="pgsql" then
		SqlExec2([[set lc_time to 'ru_RU.utf8']])
	end
	
Формула в поле created_at_fmt:

.. code-block:: sql

	replace( TO_CHAR(main.created_at,'DD  TMmonth YYYY'), 'ь','я')
	
В шаблоне {{(index $item_value.k2extreq_refuse_reg 0 ).created_at_fmt}} г.:

.. code-block:: sql

	replace( TO_CHAR(main.created_at,'DD  TMmonth YYYY'), 'ь','я')
	
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
	
