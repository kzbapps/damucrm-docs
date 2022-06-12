Redirect на страницу при End Event
=================================================

Предварительно создадим и заполним переменную redirect_url В Script Task

.. code-block:: lua

	local i,errText,errNum = SqlInsert([[insert into ....]])

	if errNum~=0 then
		var.last_error =errText
		return
	end    

	var.redirect_url = "its_some_entity/"..i

	
В Angular классе в финальном шаге (End Event):

.. code-block:: javascript	


	const vm = this; 
	return class GenClass extends vm.constructor {
		detail = {};
		ngOnInit() {        
			// заголовок
			this.appComponent.user_task_title = data.processTitle;        
			// получение входящих данных
			for(let v of data.vars) {
				this.detail[v.name] = v.value;
			}        
			location.href=this.detail.redirect_url;
			this.appComponent.opened_modal = false;                
		}
	}
