Открыть модальное окно в AngularJS
=================================================

Шаблон:

.. code-block:: html

	<section  ng-controller="DetailFormCtrl6854_poisk">
	<div ng-if="modal_id" class="modal" id="{[{modal_id}}" tabindex="-1" role="dialog">
		  <div class="modal-dialog modal-lg" style="margin-right:0px; margin: 0px !important;width:1000;padding-left:100px">
			<div class="modal-content">
				<div class="modal-header" style="position: relative !important">
					
				</div>    
				<h1>Салем!!!</h1>
			</div>
		   </div>    
	</div>

	<button ng-click="show()">Show Modal</button>


	</section>
	
	
Контроллер:

.. code-block:: javascript

	MetronicApp.cp.register('DetailFormCtrl6854_poisk',function($scope,$rootScope, $http,$log,$stateParams,DMLService,RestApiService,UIService,PubSub,$location)  {

		$scope.modal_id=Metronic.getUUID();
		
		$scope.show = function(){
			$("#"+$scope.modal_id).modal();
		}
		
		
	})