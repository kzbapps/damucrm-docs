Хлебные крошки в AngularJS
=================================================

Вариант 1.

Пропишите в детализации вашей сущности новый запрос с кодом path$

Пример:

.. code-block:: bash

	select '/k2/k2req_pay' url,
	'Все платежи' as title,
	'' as prefix
	from dual


	union all

	select '/k2/k2clidetails/'|| cli_id.id url,
	cli_id.title,
	'Клиент' as prefix
	from k2req_pay main
	join k2acc acc_id on acc_id.id = main.acc_id
	join k2cli cli_id on acc_id.cli_id = cli_id.id
	where main.id=?


	union all

	select '/k2/k2accdetails/'|| acc_id.id url,
	acc_id.code as title,
	'Счет' as prefix
	from k2req_pay main
	join k2acc acc_id on acc_id.id = main.acc_id
	where main.id=?


	union all

	select '/k2/k2reqdetails/'|| req_id.code url,
	coalesce(req_id.code,'Id '||req_id.id) as title,
	'Требование' as prefix
	from k2req_pay main
	join k2req req_id on req_id.id = main.req_id
	where main.id=?


Вариант 2.


Добавьте Кастомную вставку в место "Хлебные крошки", например

.. code-block:: html

	<a title="Опубликовать сущность"  ng-if="((detail.id != 0) && (!editing))" ng-click="pubSubPublish('chooseBPMSModal',{callBack:bindCallBack,'processCode':'entity_publish', input: {url:'?code=entities&ids='+detail.id} });">
		<i class="fa fa-cloud-upload  text-primary"></i></a>

	<span ng-repeat="p in details.parent_table_parts">
		<i class="fa fa-angle-right"></i>	
		 <a href="#/settings/entitiesdetails/{[{p.entity_id}}">{[{p._entity_title}}</a>
						
	</span>
	<span ng-if="!editing && detail.id!=0">
		 <i class="fa fa-angle-right"></i>	
		<a href="#/settings/entity_designer/{[{detail.id}}"><i class="fa fa-desktop"></i> Дизайнер</a>
	   
	</span>