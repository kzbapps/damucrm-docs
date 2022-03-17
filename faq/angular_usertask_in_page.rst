UserTask Бизнес-процесса внутри страницы
=================================================

В шаблоне:

.. code-block:: text

    <ng-container [ngTemplateOutlet]="appComponent.user_task_template"></ng-container>
	
В классе:

.. code-block:: javascript	


    param_sub = this.route.queryParams
        .subscribe(params => {
            if(params.task) {
                this.task = params.task;
                this.appComponent.getUserTaskData({task: this.task}).subscribe(resp => {
                    //Для отладки
					//console.log("SUPER CALLBACK BY PARAM TASK",resp.data);
                    try{
					//Если нужно зачитать переменную
                    //this.step = resp.data.vars.filter(item =>   item.name == 'step').map(item => item.value)[0]
                    }catch(e){
                        alert(e.message);
                    }
                    
                });
            }
        });
		

	ngOnInit() {        
		this.appComponent.use_user_task_template = true;
	}

	ngOnDestroy () {
		this.appComponent.use_user_task_template = false;
	}

Запуск процесса:

.. code-block:: javascript	

    start(xml){
        this.appComponent.bpRun("its_eo_register",{ step : this.step,signxml : xml }).subscribe((resp)=>{        
                this.router.navigate([],{
                    relativeTo: this.route,
                    queryParams: { task: resp.task },
                    queryParamsHandling: 'merge'
                });
            }); 
    }
