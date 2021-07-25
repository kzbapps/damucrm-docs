Kalkan Crypt
===================================================================================

PKEY_SET_TYPE:unsupported algorithm
_____________________________________

.. code-block:: xml

Error: 8f00009:
ERROR 0x8f0002a: OpenSSL error:
 140209930315440:error:0609E09C:digital envelope routines:PKEY_SET_TYPE:unsupported algorithm:p_lib.c:239:

ERROR 0x8f00009: Load key store - invalid password.


Решение: библиотеки kalkancrypt должны всегда лежать в папке /opt/kalkancrypt (никаких /opt/damu/kalkancrypt)
