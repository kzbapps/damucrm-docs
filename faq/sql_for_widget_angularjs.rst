Пример SQL для виджета с параметрами дат. И сам шаблон виджета
==================================================================================================

SQL Отражает информацию о не переданных документах в ИС

.. code-block:: sql

	select 
	(select count(1) from i$skk_req_to_isez i where json_res is null and created_at between dates.date1 and dates.date2) as error_count
	from users u
	join (select ? as date1,
	date_add(?,interval 1 day)
	as date2 from dual) dates on 1=1
	where u.id=:user_id

Шаблон

.. code-block:: html

	<!DOCTYPE html>
	<section ng-controller="WidgetCustom01Ctrl">
		<div ng-if="!loaded">
			
			<h3>
				<img src="theme/assets/admin/layout/img/loading-spinner-blue.gif">
				Вычисление информации для формирования дэшборда...</h3>
		</div>    
		<div ng-if="loaded">
		<div class="row">
			<div class="col-md-12 text-center">
		
				<div class="btn-group" role="group" aria-label="...">     
					 <a ng-click="setListPeriodFilter('today')" class="btn btn-default {{listPeriodCode == 'today' ? 'blue':''}}">сегодня</a>
					 <a ng-click="setListPeriodFilter('yesterday')" class="btn btn-default {{listPeriodCode == 'yesterday' ? 'blue':''}}">вчера</a>
					 <a ng-click="setListPeriodFilter('this_week')" class="btn btn-default {{listPeriodCode == 'this_week' ? 'blue':''}}">эта неделя</a>
					 <a ng-click="setListPeriodFilter('this_month')" class="btn btn-default {{listPeriodCode == 'this_month' ? 'blue':''}}">этот месяц</a>
				</div> 
			</div>
		
		
			<div class="col-lg-6 col-md-6 col-sm-6">
				<div class="dashboard-stat  {{data.error_count>0?'red-intense':'blue-madison'}}">
					<div class="visual">
						<i class="fa fa-comments"></i>
					</div>
					<div class="details">
						<div class="number">
							 {{data.error_count}}
						</div>
						<div class="desc">
							 Не отправленные сообщения в ИСЭЗ <a style="color:#fff" href="#/bpms/view_vars_bp_instances?df_process_id=1045&df_date1={{begin_at}}&df_date2={{end_at}}"><i class="icon-arrow-right"></i></a>
						</div>
					</div>
					<!--<a href="#/mfo/mfo_reqs/" class="more">
					Все заявки <i class="m-icon-swapright m-icon-white"></i>
					</a>-->
				</div>
			</div>
			
		

		</div>
		
		</div>	
		
		
			
	</section>

Контроллер


.. code-block:: javascript

    function WidgetCustom01Ctrl($scope,$http,RestApiService,$filter){        
		$scope.listOwnerCode="my";    
		
		$scope.percent = 65;
		$scope.options = {
		animate:{		
		duration:0,
		enabled:false},			
		barColor:'red',			
		scaleColor:'black',			
		lineWidth:3,			
		lineCap:'circle'
		};
			


		$scope.setListOwnerFilter = function(code){
			$scope.listOwnerCode=code;  
			
			$scope.bind();
			
		}
		
		$scope.setListPeriodFilter = function(code){
			$scope.listPeriodCode=code;   
			var x= Metronic.getIntervalByPeriodCode(code);
			console.log(x);
			$scope.begin_at = $filter('date')(x[0], "yyyy-MM-dd");
			$scope.end_at = $filter('date')(x[1], "yyyy-MM-dd");
			$scope.bind();
			 
		}    
		
		
		
		$scope.bind = function runWidget(config){
			
			//Metronic.startPageLoading();
			$scope.loaded = false;
			
			
			RestApiService.get("query/get?code=skk_dashboard&param1="+$scope.begin_at+"&param2="+$scope.end_at).
				success(function (data) {
					if (data.items) {
						$scope.data = data.items[0];
						
					}

					$scope.loaded = true;
					
				});

		}

		$scope.setListPeriodFilter("today");

    }
