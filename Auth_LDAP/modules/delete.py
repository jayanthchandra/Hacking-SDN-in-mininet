import ldap


def DieFuckers():
	try:
		l = ldap.open("127.0.0.1")
	
		l.protocol_version = ldap.VERSION3	
	
		username = "cn=Manager, o=sdn.authenticate"
		password  = "admin"
	
		l.simple_bind(username, password)
	except ldap.LDAPError, e:
		print e
	

	deleteDN = "uid=Node3, ou=Manager,o=sdn.authenticate"
	try:
	
		l.delete_s(deleteDN)
	except ldap.LDAPError, e:
		print e
	
						