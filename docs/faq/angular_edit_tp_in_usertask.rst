Редактирование табличной части из UserTask
====================================================================================================================================

1. Создать страницу its_tests_01_details_tp_test_02, в который в page_ui_block добавить только нужную табличную часть

2. В шаблоне UI Блока User Task добавить:

.. code-block:: html


	<jit-page
			type="pages"
			[data]="{id:vars.id}"
			code="its_tests_01_details_tp_test_02"
			(getComponent)="startTablePartEdit($event,'its_tests_02','data') "

	></jit-page>

,
где

vars.id - ID записи, входная переменная в usertask

its_tests_01_details_tp_test_02 - страница с табличной частью

its_tests_02 - код табличной части в сущности its_tests_01

data - output переменная в usertask


3. Разработать script task после user Task:

.. code-block:: lua

	local js = StringToJson(var.data)

	for k,v in pairs (js) do
		--...SqlInsert....
	end


4. Пример вызова:

.. code-block:: html

	<div class="col">
		<div class="card" style="height:516px">
			<div class="card-header bg-white">
			<h5>Проверка редактирования табличной части в user task</h5>
		</div>
		<div class="card-body">
	<label *ngIf="detail_id == 0">Для использования функционала сначала сохраните запись</label>
			<button type="button"
	[disabled]="detail_id==0"
	(click)="appComponent.bpRun('its_tests_01_details_tp',{id:detail_id})" class="btn btn-primary">Запустить</button>
		</div>
		</div>
	</div>


