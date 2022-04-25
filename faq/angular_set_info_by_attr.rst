При изменении поля БИН (input label) установить атрибуты другим полям через БП
========================================================================================

1. В атрибуте БИН в параметре on change value прописать:

.. code-block:: text

    binCustomChanged($event)

2. В логике БИН в параметре on change value прописать поля attr_code,entity_code :
	
.. code-block:: javascript	


	binCustomChanged(event) {
	this.save( () => this.binCustomChangedCallBack(event));
	}

	binCustomChangedCallBack(event) {
	this.appComponent.bpRun("update_by_attr",{ 
	attr_code : "bin",
	entity_code: "its_tests_01",
	id: this.detail_id}, (data) => this.bindCallBack(data));
	}
		
3. Доработать БП update_by_attr по своему усмотрению