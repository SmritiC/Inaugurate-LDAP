
import sys
import subprocess 
import time
from subprocess import Popen,PIPE
from scripts.installation import LDAPInstall
from scripts.manageLDAP import ManageLdapscripts 
from interface.passwdWin import passwordWin 
from interface.dnWin import dnWin
from interface.progressBarWin import progressBar

class installproc:
	def __init__(self):
        	ldapInstallObj=LDAPInstall()
        	print "-----------------------------upgrading packages----------------------------------------------"
        	ldapInstallObj.upgrade()
        	ldapInstallObj.installTkinter()
        	print "-------------------------------installing LDAP---------------------------------------------"
        	password=passwordWin()
        	if(password==""):
                	#root.destroy()
                	sys.exit()

        	else:
                	dn=dnWin()
                	domainName=dn[0]
			print(domainName)
                	orgName=dn[1]
                	if(domainName==""):
                        	#root.destroy()
                        	sys.exit()
                	else:
				time.sleep(5)
                        	ldapInstallObj.updateLDAPUtils(password,password)
                        	ldapInstallObj.writeDomainName(domainName)
                        	time.sleep(25)
                        	print "--------------------------------------Installing ldapscripts---------------------------------------------"
                        	manageldapscriptsObj= ManageLdapscripts(password,domainName,orgName)
        	#root.destroy()


#install LDAP 
#check if ldap is already installed
notInstalled=1 
poutput=Popen(["dpkg-query","-W","-f='${Status}'","ldap-utils"],stdout=PIPE,stderr=PIPE)
already_install_output=poutput.stdout.read()
already_install_error=poutput.stderr.read()
if(already_install_output=="'unknown ok not-installed'"):
	notInstalled=1
else:
	notInstalled=0
if(notInstalled):
	#progressBar()
	obj=installproc()
else:
	print("LDAP server is already installed!!!")

