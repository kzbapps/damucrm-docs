pkg/fmt - Форматирование строк
================================================================================================

local pkg =require("pkg/fmt")


Sprintf
------------------

.. code-block:: lua

	local pkg =require("pkg/fmt")
	output.c = pkg.Sprintf ("%.2f %.2f %.2f",10000, 22, 44)

Результат

.. code-block:: json

	{
		"c": "10000.00 22.00 44.00"
	}
		
		

