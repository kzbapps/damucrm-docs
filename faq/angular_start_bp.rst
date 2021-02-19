Запуск бизнес-процесса из Angular
=================================================
.. code-block:: text

    <button (click)="run()">Запустить процесс</button>	
	
В контроллере должен быть объявлена функция:

.. code-block:: javascript	

	const vm = this; 

	return class GenClass extends vm.constructor {
		
		run() {
			this.appComponent.bpRun("tests_five",{});
		}
	}
