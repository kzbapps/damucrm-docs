Способ отобразить список открытых UserTask для документа the_documents в AngularJS
==================================================================================================

Шаблон

.. code-block:: html

	<button ng-if="!editing" 
	ng-repeat="item in details.the_documents$tasks" ng-click="pubSubPublish('resumeBPMSModal',{task:item.task})" 

	class="btn btn-primary red"><i class=" icon-printer"></i>{{item.title}}</button>
	
Создадим Запрос детализации the_documents$tasks

.. code-block:: sql

	SELECT p.title, t.sys$uuid task FROM bp_tasks t,bp_points p,the_documents i where t.point_id=p.id
	  and i.instance_id = t.instance_id and t.is_open =1 and t.id in
		(select task_id from bp_task_actors ta where ta.task_id=t.id and ta.user_id=:user_id)
	and i.id = ? and t.is_open=1


