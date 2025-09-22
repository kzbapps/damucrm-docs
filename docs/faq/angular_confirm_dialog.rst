Пример отображения окна подтверждения (confirm)
=======================================================================================================================================================

.. code-block:: javascript

    confirmDeleteChecked() {
        
        this.confirmationService.confirm({
            target: event.target,
            acceptLabel: 'Да',
            rejectLabel: 'Нет',
            message: 'Вы действительно хотите удалить ' + this.checked_rows.length + ' записей?',
            icon: 'pi pi-exclamation-triangle',
            accept: () => {
                this.deleteChecked();
            },
            reject: () => {
                // 
            }
        });
    }