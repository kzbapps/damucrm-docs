Запуск бизнес-процесса из Angular
=================================================
.. code-block:: text

    <button (click)="run()">Регистрация</button>	
	
В контроллере должен быть объявлена функция:

.. code-block:: javascript	

    const vm = this;
	
	return class GenClass extends vm.constructor {
	
	step = 0;
	
    setStep(step){
        this.step = step
    }	
	
    registerCallBack(data){        

        if (data.output && data.output.last_error == ""){
            this.setStep(4);
        }
    }
		
    register(){
        this.appComponent.bpRun("its_eo_register",{ iin : this.f.iin.value, name1: this.f.name1.value, name2: this.f.name2.value, name3: this.f.name3.value, email: this.f.email.value}, (data) => this.registerCallBack(data)); 
    }
	}
