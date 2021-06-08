Plugin - Выполнение функции, разработанной на языке golang в виде Plugin
========================================================================================================

Пример файла плагина на языке golang

plugin1.go

.. code-block:: go

	package main

	import "fmt"

	func FUNC_TEST(in map[string]interface{}, out *map[string]interface{} ) {
		*out = make(map[string]interface{})
		(*out)["text"] = fmt.Sprintf("Hello from Plugin %s",in["text"])
		(*out)["nds_amount"] = 12 * in["price"].(float64)
	}

Скомпилируем его:

.. code-block:: bash

	go build --buildmode=plugin plugin1.go

Скрипт запуска

.. code-block:: lua

	output = {}
	output.res,output.errText,output.errNum = Plugin("/opt/go/src/gitlab.com/com.ibcb/plugins/plugin1.so", "FUNC_TEST", { text = "123", price = 2000 })

Результат 

.. code-block:: json

	{
		"errNum": 0,
		"errText": "",
		"res": {
			"nds_amount": 24000,
			"text": "Hello from Plugin 123"
		}
	}

При изменении плагина необходимо перезагрузить приклад

.. code-block:: bash

	systemctl restart damu

