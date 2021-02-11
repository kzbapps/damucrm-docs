Поле телефон в AngularJS
=================================================

.. code-block:: html

	<input ng-change="editPhone(contacts.cont)" 
	ui-mask="+9(999) 999 99 99" 
	ui-mask-placeholder ui-mask-placeholder-char=" " 
	ng-model= "contacts.cont" 
	class="form-control"
	placeholder="{{ 'Phone' | translate }}" /> 
	
	
Директива phone с использованием split:

.. code-block:: html	

	<a ng-if="row[col.alias]| split:';':0" href="sip:{{row[col.alias]| split:';':0 | tel}}"><i class="fa fa-phone"></i> {{row[col.alias] | split:';':0 | phone}}</a>