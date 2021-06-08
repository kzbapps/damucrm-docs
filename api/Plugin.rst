Plugin - Выполнение функции, разработанной на языке golang в виде Plugin
========================================================================================================

Пример файла плагина на языке golang

plugin1.go

.. code-block:: go

	package main

	import "fmt"

	var IN map[string]interface{}
	var OUT = make(map[string]interface{})

	func FUNC_TEST() {

	OUT["text"] = fmt.Sprintf("Hello from Plugin %s",IN["text"])
	OUT["nds_amount"] = 12 * IN["price"].(float64)
	}


Скомпилируем его:

.. code-block:: bash

	go build --buildmode=plugin plugin1.go

Скрипт запуска

.. code-block:: lua

	output = {}
	output.res,output.errText,output.errNum = Plugin("/opt/go/src/gitlab.com/com.ibcb/plugins/plugin1.so", "FUNC_TEST", { text = "123", price = 1000 })


При изменении плагина необходимо перезагрузить приклад

.. code-block:: bash

	systemctl restart damu

