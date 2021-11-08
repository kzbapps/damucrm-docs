SmartBridge
===================================================================================


/etc/ipsec.conf
_____________________________________


XX.XX.XX.XX - ваш белый IP

.. code-block:: text

	config setup
		charondebug="all"
		uniqueids=no

	conn %default
		ikelifetime=1440m
		keylife=60m
		rekeymargin=3m
		keyingtries=1
		keyexchange=ikev2
		authby=secret

	conn sb
		type=tunnel
		auto=start
		keyexchange=ikev2
		authby=secret
		left=%defaultroute
		leftid=XX.XX.XX.XX
		leftsubnet=XX.XX.XX.XX/32
		right=195.12.122.44
		rightsubnet=195.12.113.7/32

		ike=aes256-sha256-modp1536
		esp=aes256-sha256

		keyingtries=0
		ikelifetime=1h
		lifetime=8h
		dpddelay=30
		dpdtimeout=120
		dpdaction=restart
		auto=start

/etc/ipsec.secrets
_____________________________________

.. code-block:: text

	XX.XX.XX.XX 195.12.122.44 : PSK ******************
	

Переподключение:
_____________________________________

.. code-block:: text

	ipsec up sb

Тест соединения:
_____________________________________

.. code-block:: text

	195.12.113.7
