LUA Удаление BOM
=========================


.. code-block:: lua

	v1 = StrReplace(v1,string.char(239,187,191),"",-1)