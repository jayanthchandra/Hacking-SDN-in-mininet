import ldap

def HookORLookup():
	try:
		l = ldap.open("127.0.0.1")
		l.protocol_version = ldap.VERSION3	
	except ldap.LDAPError, e:
		print e
		
	baseDN = "ou=Manager, o=sdn.authenticate"
	searchScope = ldap.SCOPE_SUBTREE

	retrieveAttributes = None 
	searchFilter = "cn=*Node3*"

	try:
		ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
		result_set = []
		while 1:
			result_type, result_data = l.result(ldap_result_id, 0)
			if (result_data == []):
				break
			else:
				if result_type == ldap.RES_SEARCH_ENTRY:
					result_set.append(result_data)
		print result_set
	except ldap.LDAPError, e:
		print e
