Kalkan Crypt
===================================================================================

Ошибка: PKEY_SET_TYPE:unsupported algorithm
__________________________________________________________________________

.. code-block:: text

	Error: 8f00009:
	ERROR 0x8f0002a: OpenSSL error:
	140209930315440:error:0609E09C:digital envelope routines:PKEY_SET_TYPE:unsupported algorithm:p_lib.c:239:
	ERROR 0x8f00009: Load key store - invalid password.


1. Решение: библиотеки kalkancrypt должны всегда лежать в папке /opt/kalkancrypt (никаких /opt/damu/kalkancrypt)

2. Вам передали не тот pfx файл, например из полученных 1.pfx, 2.pfx и 3.pfx из ПО Vido, подошел только 2.pfx


Ошибка: [signal SIGSEGV: segmentation violation code=0x1 addr=0x18 pc=0x134f58c]
______________________________________________________________________________________________________________

.. code-block:: text

	[signal SIGSEGV: segmentation violation code=0x1 addr=0x18 pc=0x134f58c]
	runtime stack:
	runtime.throw({0x15a7c24, 0x8bae89})
			/usr/local/go/src/runtime/panic.go:1198 +0x71
	runtime.sigpanic()
			/usr/local/go/src/runtime/signal_unix.go:719 +0x396
	goroutine 2497 [syscall]:
	runtime.cgocall(0x134fd00, 0xc0006945f8)
			/usr/local/go/src/runtime/cgocall.go:156 +0x5c fp=0xc0006945d0 sp=0xc000694598 pc=0x88203c
	gitlab.com/kz.bapps/damu/lib/gokalkan._Cfunc_libLoadKey(0x0, 0x7f549c032d00, 0x7f549c0202c0, 0xc000742000, 0xc0004a09ec)

Решение: Установить следующие пакеты:

Centos:

.. code-block:: bash

	yum install pcsc-lite libtool-ltdl

Ubuntu:

.. code-block:: bash

	apt install libpcsclite-dev