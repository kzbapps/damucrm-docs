pkg/strconv - Преобразования строк
================================================================================================

local pkg =require("pkg/strconv")


ParseFloat
------------------

.. code-block:: lua

	local pkg =  require("pkg/strconv")
	
	local a,errText,errNum = pkg.ParseFloat("100000",16)
	
	

