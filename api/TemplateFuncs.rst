Функции для ParseTemplate
==========================================================================

Iterate
---------------------------------------------

Сгенерировать массив чисел

.. code-block:: html 

	{{- range $val := Iterate 1 10 }}
	  {{ $val }}
	{{- end }}


Результат

.. code-block:: text 

  1
  2
  3
  4
  5
  6
  7
  8
  9
  10


print
---------------------------------------------

Конкатинация строк

.. code-block:: text 

	{{lua "signXml" .param.gost_path .param.gost_password ( print "AAA" "BBBB" ) }}
