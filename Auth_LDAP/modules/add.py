import ldap
import ldap.modlist as modlist

def AddElements():

	l = ldap.initialize("ldaps://localhost.localdomain:636/")

	l.simple_bind_s("cn=manager,dc=sdn.authenticate,dc=com","admin")

	dn="cn=replica,dc=sdn.authenticate,dc=com" 

	attrs = {}
	attrs['objectclass'] = ['top','organizationalRole','simpleSecurityObject']
	attrs['cn'] = 'replica'
	attrs['userPassword'] = 'aDifferentSecret'
	attrs['description'] = 'User object for replication using slurpd'

	ldif = modlist.addModlist(attrs)

	l.add_s(dn,ldif)

	l.unbind_s()
	