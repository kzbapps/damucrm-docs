Скрыть user task при запуске его из страницы, чтобы можно было продолжить таск, например, через вызов рест сервиса
===================================================================================================================================================

Пример: Процесс регистрации пользователя

User Task

.. code-block:: javascript

    ngOnInit() {
        this.appComponent.opened_modal = false;
        this.appComponent.bp_callback({output:{"last_error":""}});
    }

На странице:

.. code-block:: javascript	

    registerCallBack(data){
        if (data.output && data.output.last_error == ""){
            this.setStep(4);
            
        }
    }
    
    register(){
        this.appComponent.bpRun("its_eo_register",{ iin : this.f.iin.value, name1: this.f.name1.value, name2: this.f.name2.value, name3: this.f.name3.value, email: this.f.email.value}, (data) => this.registerCallBack(data)); 
    }


Рест сервис, который продолжает процесс:


.. code-block:: lua	


	output = {}
	--todo

	local found,errText,errNum = SqlQueryRow2([[select t.sys$uuid task from i$its_eo_register i join bp_tasks t on t.instance_id=i.id$ where i.token = ?]],request.input.token)

	if errNum~=0 then
		output.error_code = errNum
		output.eror_text = errText
		return
	end

	local task_uuid,errText,errNum = BPMSRunManualTask(found.task,1,{user_token = request.input.token})

	if errNum~=0 then
		output.error_code = errNum
		if StrContains(errText,"CLOSED") then
			output.error_text = "Вы уже зарегистрированы"
			output.error_code = 0
		else
			output.error_text = "Внутренняя ошибка"
		end    
		return
	end

	output.error_text = "Спасибо за регистрацию"
	output.error_code = 0

