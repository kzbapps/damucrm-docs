Drag and Drop в AngularJS
=================================================

Шаблон:

.. code-block:: html

	<div class="row"
			ng-mousemove="onMouseMove($event)"
			ng-mouseup="onMouseUp($event)" 
			ng-touchmove="onMouseMove($event)"
			ng-touchend="onMouseUp($event)">

		
		<div class="col-md-2 col-sm-4 col-xs-6" ng-repeat="status in statuses">
			
			<div class="panel panel-primary drag_item" 
				id="{{ status.id }}"
				ng-style="nextStatus === status.id ? hover_style : {}">
				
				<div class="panel-heading text-center">
					<strong>{{status.id}}</strong>
				</div>
				
				<div class="panel-body">
					  
					<ul class="list-group">
						<li 
							ng-mousedown="onMouseDown(item.id,status.id,$event)"
							ng-touchstart="onMouseDown(item.id,status.id,$event)" 
							ng-style="item.id === dragging ? dragging_style : {}"
							ng-repeat="item in status.items" 
							class="list-group-item"><span class="badge badge-primary">{{item.quantity}}</span> {{item.id}}</li>
						
					</ul>    		
					
				</div>
			</div>  
		</div>

	</div>
	
	
Контроллер:

.. code-block:: javascript

    // идентификатор элемента, который перетаскивается
    $scope.dragging = null;
    
    // идентификатор группы, которой пренадлежит переносимый элемент
    $scope.currentStatus = null;
    
    // стиль при наведении на блок, куда надо перетащить
    $scope.hover_style = {'border': '2px solid #FF0000'};
    
    // стиль при перетаскивании, не указан только TOP и LEFT
    // TOP и LEFT присваиваются при переносе
    $scope.dragging_style = {
        'position': 'fixed', 
        'display' : 'block', 
        'z-index': '9999', 
        'opacity': .7, 
        'cursor': 'pointer',
        'border': '1px dashed #ff5555', 
        'background-color': 'rgba(125,255,0,.5)'
        
    }
    
    // координаты внутри элемента
    $scope.drag_offset = { x : 0, y : 0}
    
    // примерные данные о блоках и элементах
    $scope.statuses = [
        {
            id:"Литье",
            items:[
                {id:'Кольцо'},
                {id:'Серьги'},
            ]
            
        },
        {
            id:"Брак",
            items:[
                {id:'Браслет'}
            ]
            
        },
    ];


    
    $scope.onMouseMove = function(event){

        // массив, список блоков для переноса
        // Класс drag_item можно заменить, не забудьте заменить его в блоке
        $scope.dragItemElements = angular.element(document.querySelectorAll('.drag_item'));
        $scope.nextStatus = null;
        
        event.preventDefault();
        var touch = event;
        
        if(!!event.originalEvent) {
            if(!!event.originalEvent.changedTouches && event.originalEvent.changedTouches.length > 0){
                touch = event.originalEvent.changedTouches[0];
            } else if(!!event.originalEvent.touches && event.originalEvent.touches.length > 0) {
                touch = event.originalEvent.touches[0];
            } 
        } else if(!!event.touches && event.touches.length > 0) {
            touch = event.touches[0];
        } else if(!!event.changedTouches && event.changedTouches.length > 0) {
            touch = event.changedTouches[0];
        }
        
        var target = event.currentTarget || event.target;
        
        // условие, если элемент перетаскивается
        if(!!$scope.dragging) {
            
            // определение координат элемента через стиль
            $scope.dragging_style.left = touch.pageX - $scope.drag_offset.x;
            $scope.dragging_style.top = touch.pageY - $scope.drag_offset.y;
    
            // цикл, перебираем все блоки для переноса, чтобы 
            // вычислить блок, на который наведен элемент при перетаскивании
	        angular.forEach($scope.dragItemElements,function(elem,num) {
	            
	            // размеры блока
	            var bounds = elem.getBoundingClientRect();
	            
	            // условие, если курсор направлен на этот блок 
	            if(touch.pageX >= bounds.left
    	                && touch.pageX <= bounds.left + bounds.width 
    	                && touch.pageY >= bounds.top
    	                && touch.pageY <= bounds.bottom + bounds.height){
                    // назначение следующего блока, куда перетащится
                    // элемент при завершении перетаскивания
    	            $scope.nextStatus = elem.attributes.id.value;
                }
    	        
	        });
    
            /* ====================================================*/
            // этот блок чтобы при перетаскивании не выделялся текст
            if (event.stopPropagation) event.stopPropagation();
            if (event.preventDefault) event.preventDefault();
            event.cancelBubble = true;
            event.returnValue = false;
            return false;
            /* ====================================================*/
        }
        
    }
    
    $scope.onMouseDown = function(itemid,statusid,event){
        
        // перетираем старые данные о местоположении элемента
        delete $scope.dragging_style.left;
        delete $scope.dragging_style.top;
    
        // определение переменных координат внутри элемента
        $scope.drag_offset.x = event.offsetX || 0;
        $scope.drag_offset.y = event.offsetY || 0;
        
        // маленькая задержка. timeuot НЕОБЯЗАТЕЛЬНО. Можно в принципе убрать.
        $scope.timeoutMouseDown = setTimeout(function() {
	        
	        // определение перетаскиваемого элемента
	        $scope.currentStatus = statusid
	        // определение блока, откуда перетаскиваемый элемент
	        $scope.dragging = itemid;
	        
        },100); 
    }
    
    $scope.onMouseUp = function(event) {
        
        // отключение задержки при нажатии НЕОБЯЗАТЕЛЬНО, ЕСЛИ ЕЕ НЕТ!
        clearTimeout($scope.timeoutMouseDown); 
        
        if(!!$scope.nextStatus && !!$scope.currentStatus && !!$scope.dragging ) {
            
            $scope.statuses.forEach(function(status,num1) {
                // ЗДЕСЬ БУДЕТ ВЫЗОВ ЛОГИКИ
                
                // ЛОГИКА ДЛЯ ТЕКУЩЕГО ПРИМЕРА
                
                // условие на очистку фрейма откуда стащил элемент
                if($scope.currentStatus == status.id) {
                    status.items = status.items.filter(function(item){ return item.id !== $scope.dragging });
                }
                
                // условие на добавление во фрейм куда перетащил элемент
                if($scope.nextStatus == status.id) {
                    if(!("items" in status)) status.items = [];
                    status.items.push({'id' : $scope.dragging});
                }
            });
        }
        
        // обнуляем переменные
        $scope.currentStatus = null;
        $scope.dragging = null;
        $scope.nextStatus = null;
    }
