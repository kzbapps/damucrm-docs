Как получить несколько списков в Angular одной итерацией
==================================================================================================

.. code-block:: javascript

        const {forkJoin} = rx;
		
		//....

        forkJoin(
        this.dbQueryService.getQuerySelect('c_cli_act_dashboard_by_reason&param1='+intervalCode, ''),
        this.dbQueryService.getQuerySelect('c_cli_act_dashboard_by_stat&param1='+intervalCode, ''),
        this.dbQueryService.getQuerySelect('agents_dashboard_by_status', ''),
        )
        .subscribe((resp) => {
            console.log("resp1",resp[0]);
            console.log("resp2",resp[1]);
            console.log("resp3",resp[2]);
        })
		
