Умный поиск
==================================================================================================



.. code-block:: text

	CREATE EXTENSION fuzzystrmatch;


.. code-block:: sql

	select * from (select levenshtein('ручку', title,0,1,1) a,title,length(title) l from skk_good sg) a
	where a.a<2
	order by 1

