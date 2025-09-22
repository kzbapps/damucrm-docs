Выводить вызовы print в результат Рест сервиса:
==================================================

.. code-block:: lua

	output = {}

	function createPrint()
		local r = {}
		r.log=array({})
		function print(...)
			local m={...}
			if #m ==1 then
				table.insert(r.log,m[1])
				return
			end
			table.insert(r.log,m)
		end
		return r
	end
	output.log=createPrint()
	
