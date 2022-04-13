Открыть модальное окно со страницей в DamuBPM и получить ответ.
==================================================================

Шаблон страницы вызова модального окна:

.. code-block:: html


	<p-dialog *ngIf="modal_page" [(visible)]="modal_show">
		<jit-page
			type="pages"
			[data]="{}"
			[code]="modal_page"
			(getComponent)="openModalForFileUploader($event)"
		></jit-page>

		<button class="btn btn-primary" (click)="modal_show = false">Закрыть</button>
	</p-dialog>


	<div class="col">
		<div class="card" style="height:516px">
			<div class="card-header bg-white">
			<h5>Проверка модалки</h5>
			<h5>Modal info {{modal_info | json}}</h5>
		</div>
		<div class="card-body">
			<button type="button" (click)="openModal()" class="btn btn-primary">Открыть модалку</button>
		</div>
		</div>
	</div>

Шаблон класса вызова модального окна:


.. code-block:: javascript


	const vm = this;
	return class GenClass extends vm.constructor {
		error_code;
		error_text;
		search_text = "";
		modal_info = {};
		opened_modal = false;
		modal_page = "users_lookup";

		openModalForFileUploader(jit_page) {
			let vm = this;
			jit_page.chooseCallBack = (file) => {
				this.modal_info = file;
				vm.modal_show = false;
			}
		}
		openModal(){
			this.modal_show = true;
		}
	}

В странице users_lookup должно быть прописано chooseCallBack:

.. code-block:: html

	<tr *ngFor="let i of users.items"  [routerLink]="i.url" (click)="chooseCallBack(i)" >
		..
	</tr>