Freeswitch
===================================================================================

Tele2 outbound route
_____________________________________

.. code-block:: xml

	<extension name="tele2">
	  <condition field="destination_number" expression="^(\+77\d{9})$|^(87\d{9})$">
		<action application="set" data="effective_caller_id_number=+77085052463"/>
		<action application="bridge" data="sofia/gateway/tele2/+77${destination_number:-9}"/>
	  </condition>
	</extension>

Tele2 GateWay
_____________________________________

.. code-block:: xml

	<include>
	  <gateway name="tele2">
	  <param name="username" value="user"/>
	  <param name="from-user" value="user"/>
	  <param name="password" value="password"/>
	  <param name="proxy" value="217.76.71.17"/>
	  <param name="expire-seconds" value="60"/>
	  <param name="register" value="true"/>
	  </gateway>
	</include>


MP3 Recording
____________________________________

.. code-block:: text

	download https://centos.pkgs.org/6/okey-x86_64/freeswitch-format-mod-shout-1.6.8-1.el6.x86_64.rpm.html
	extract file mod_shout.so to /usr/local/freeswitch/mod/

	yum install libshout
	yum install lame-libs
	yum install libmpg123
	ln -s /usr/lib64/libpcre.so.1 /usr/lib64/libpcre.so.0

	fs_cli
	> load mod_shout
