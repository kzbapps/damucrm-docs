Установить значение в поле (id) по коду (зная код)
==================================================================

На поле checkbox пропишите параметре on change value:

.. code-block:: javascript

	changeMainApltRes($event.target.checked);


Добавьте логику:

.. code-block:: javascript

	changeMainApltRes(checked) {
		if(checked) {
			let opt = new QueryOptions('countries_select');
			opt.flteq = { code: 'KZ' };
			this.dbQueryService.getQuery(opt).subscribe(resp => {
				if  (resp && resp.items && resp.items.length > 0){
				this.f.main_aplt_country_id.setValue(resp.items[0].id);
				}
			});
			
		}
	}