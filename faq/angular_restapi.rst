Пример вызова Rest Service
==================================================================================================

.. code-block:: javascript

	this.dbQueryService.restapiPost("wa_chat_send",{msg : this.f.text.value , chat_id : this.currentChat.id})
				.pipe(first())
				.subscribe(items => {
					this.f.text.setValue('');
					setTimeout(() => document.getElementById("bottom").scrollIntoView(), 100);
				});
	

.. end

