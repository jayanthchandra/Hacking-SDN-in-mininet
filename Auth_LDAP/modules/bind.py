import ldap

def FuckLDAPandControllr(ipaddr):
	try :
		l = ldap.open(ipaddr)
		username="cn=Manager,o=sdn.authenticate"
		password="admin"
	except ldap.LDAPError, e:
		print e
