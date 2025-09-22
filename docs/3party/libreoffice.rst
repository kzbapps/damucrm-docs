Libreoffice
===================================================================================

Установка libreoffice в Ubuntu 20.04
_____________________________________

.. code-block:: bash

	wget https://ftp.gwdg.de/pub/tdf/libreoffice/stable/7.3.4/deb/x86_64/LibreOffice_7.3.4_Linux_x86-64_deb.tar.gz
	tar xfvz LibreOffice_7.3.4_Linux_x86-64_deb.tar.gz
	cd LibreOffice_7.3.4.2_Linux_x86-64_deb/DEBS/
	deb -i *.deb
	apt install libxinerama1
	apt install libnss3
	apt install libcups2
	apt install libaio1 libaio-dev -y
	apt install -y libcairo2
	apt install libsm6
	ln -s /usr/local/bin/libreoffice7.3 /bin/soffice
