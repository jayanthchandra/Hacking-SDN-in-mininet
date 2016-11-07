import ldap
import ldap.modlist as modlist

def Modifycredentials():
	l = ldap.initialize("ldaps://localhost.localdomain:636/")

	l.simple_bind_s("cn=manager,dc=sdn.authenticate,dc=com","admin")

	dn="cn=replica,dc=sdn.authenticate,dc=com" 

	old = {'description':'User object for replication using slurpd'}
	new = {'description':'Bind object used for replication using slurpd'}

	ldif = modlist.modifyModlist(old,new)

	l.modify_s(dn,ldif)

	l.unbind_s()