Как получить список (запрос) в Angular 
==================================================================================================
на примере получия информации по кошелькам

.. code-block:: javascript

    getWallets() {
        this.dbQueryService.getQuerySelect('skk_wallet$my', '')
            .subscribe((resp) => {       
				if  (resp && resp.items){
					this.wallets = resp.items;
				}
            });
    }
	

.. end

Добавим в ngAfterViewInit

	
.. code-block:: javascript

    ngAfterViewInit () {        
        this.getWallets();
    }	

В шаблоне добавим:

.. code-block:: text

	<div *ngFor="let wallet of wallets">
		Баланс: {{wallet.balance}}
	</div>

.. end