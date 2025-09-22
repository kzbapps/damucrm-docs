SmartBridge
===================================================================================

Установите минимум strongswan-5.9.6 из исходных кодов.

/usr/local/etc/ipsec.conf
_____________________________________


XX.XX.XX.XX - ваш белый IP

.. code-block:: text

	config setup
			# strictcrlpolicy=yes
			# uniqueids = no

	# Add connections here.

	# Sample VPN connections

	#conn sample-self-signed
	#      leftsubnet=10.1.0.0/16
	#      leftcert=selfCert.der
	#      leftsendcert=never
	#      right=192.168.0.2
	#      rightsubnet=10.2.0.0/16
	#      rightcert=peerCert.der
	#      auto=start

	#conn sample-with-ca-cert
	#      leftsubnet=10.1.0.0/16
	#      leftcert=myCert.pem
	#      right=192.168.0.2
	#      rightsubnet=10.2.0.0/16
	#      rightid="C=CH, O=Linux strongSwan CN=peer name"
	#      auto=start


	conn NIT1
			type=tunnel
			auto=start
			keyexchange=ikev2
			authby=secret
			left=XX.XX.XX.XX
			leftid=XX.XX.XX.XX
			right=195.12.122.44
			rightsubnet=195.12.113.29/32
			ike=aes256-sha256-modp2048
			esp=aes256-sha256-modp2048
			aggressive=no
			keyingtries=1
			ikelifetime=86400s
			lifetime=28800s
			dpdaction=restart

	conn NIT2
			also=NIT1
			rightsubnet=195.12.113.79/32

	conn NIT_TEST
			also=NIT1
			rightsubnet=195.12.113.7/32

	

/usr/local/etc/ipsec.secrets
_____________________________________

.. code-block:: text

	XX.XX.XX.XX 195.12.122.44 : PSK ******************
	

Перезапуск:
_____________________________________

.. code-block:: text

	systemctl restart ipsec
	
Переподключение:
_____________________________________

.. code-block:: text

	ipsec up NIT1

Тест соединения:
_____________________________________

.. code-block:: text

	ping 195.12.113.7
	ping 195.12.113.29
	ping 195.12.113.79
