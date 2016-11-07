import modules.bind
import modules.add
import modules.delete
import modules.modify
import modules.search

def LDAPOp():
	s=""" 
		1.Bind Controller and LDAP Server\n
		2.Adding Network nodes\n
		3.Modifying credentials in Network ids\n
		4.Hook-up the server\n
		5.Deleting credentials in LDAP\n
	"""
	#lookup!
	c=int(raw_input())
	if c == 1 :
		FuckLDAPandControllr()
	if c == 2 :
		AddElements()
	if c == 3:
		Modifycredentials()
	if c == 4:
		HookORLookup()
	if c == 5:
		DieFuckers()



if __name__ == '__main__':
    LDAPOp()