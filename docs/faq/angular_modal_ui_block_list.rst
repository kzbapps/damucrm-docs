Как добавить вызов стандартной списочной страницы в виде модального окна через Page UI Block (Логика + Html) в DamuBPM и получить ответ.
=======================================================================================================================================================

Добавьте html элемент в ваш page ui block в страницу <Кодвашейсущности>details:

.. code-block:: text

	<div class="d-flex">
		<button type="button" (click)="openModal_regulations()" class="btn btn-primary">Добавить</button>
	</div>

Добавьте Логику page ui block в ваш в страницу <Кодвашейсущности>details :

Поле Angular Template

.. code-block:: javascript

	openModal_regulations(){
		// код списочной страницы
		
		//новая глобальная переменная в Детали для модального окна - modal_page_header - тайтл модального окна
		this.modal_page_header = 'тайтл модального окна';

		this.modal_page_code = 'its_r_tech_reg';
		// данные в data для jit-page (не обязательно к заполнению)
		this.modal_page_data = {
			limit: 5,
			static_filters: [{
				alias: 'reg_type', value: '', title: 'Тип', _data_type_code: 'string', fixed: true, from: null, to: null
			}, {
				alias: 'reg_code', value: '', title: 'Код', _data_type_code: 'string', fixed: true, from: null, to: null
			}, {
				alias: 'title', value: '', title: 'Наименование', _data_type_code: 'string', fixed: true, from: null, to: null
			}]
		};
		
		// обработка события при получении getComponent

		this.getJitComponent = (jit_page) => {
			
			//Перебиваем метод goToDetail на свой:
			jit_page.goToDetail = (info) => {			
			
				this.opened_modal = false;
				//Заполняем табличную часть:
				this.tablePartAdd("its_d_stm_teh_reg_union", {
				   its_d_stm_id: this.detail_id || this.detail.sys$uuid,
				   code_id: info.reg_code,
				   name : info.title,
				});
			}
		}		
	
		// открытие модалки
		this.opened_modal = true;
	}
