import subprocess
from subprocess import Popen,PIPE
from tempfile import mkstemp
from shutil import move
from os import remove, close
import time
import re

class ManageLdapscripts:

	def __init__(self,password,domainName,orgName):
		self.password=password
		self.domainName=domainName
		self.orgName=orgName
		#print "-----------------Installing LDAPSCRIPTS------------------"
		self.checkInstalled(self.password,self.domainName,self.orgName)

	def checkInstalled(self,password,domainName,orgName):
		poutput=Popen(["dpkg-query","-W","-f='${Status}'","ldapscripts"],stdout=PIPE,stderr=PIPE)
		already_install_output=poutput.stdout.read()
		already_install_error=poutput.stderr.read()
		if(already_install_output==''):
        		alreadyInstalled=False
		else:
        		alreadyInstalled=True
		if(not alreadyInstalled):
        		self.installLdapscripts()
			print "-------------------------------LDAPSCRIPTS FINAL SETTING---------------------------------- "
                        time.sleep(20)
			self.assignPassword("/etc/ldapscripts/ldapscripts.passwd",password)
	
	def installLdapscripts(self):
        	pout=Popen(["sudo","apt-get","install","-y","ldapscripts"],stdin=PIPE)
		pout.wait()

	def modifyConfFile(self,file_path,dnName,orgName,homedir):
        	#Create temp file
        	fh, abs_path = mkstemp()
        	with open(abs_path,'w') as new_file:
                	with open(file_path) as old_file:
                        	for line in old_file:
                                	line = re.sub(r'(.)SERVER=\"(.*)\"', r'SERVER="\2"', line.rstrip())
                                	line = re.sub(r'(.*)SUFFIX=\"dc=(.*)\"' , ''.join(["SUFFIX=\"",dnName,"\""]) , line.rstrip())
                                	line = re.sub(r'(.*)GSUFFIX=\"ou=(.*)\"' , ''.join(["GSUFFIX=\"ou=",orgName,"\""]), line.rstrip())
                                	line = re.sub(r'(.*)USUFFIX=\"ou=(.*)\"' , 'USUFFIX="ou=Users"', line.rstrip())
                                	line = re.sub(r'(.*)BINDDN="cn=(.*)\"', ''.join(["BINDDN=\"cn=admin,",dnName,"\""]), line.rstrip())
                                	line = re.sub(r'(.*)BINDPWDFILE=\"/etc/ldapscripts/ldapscripts.passwd\"', 'BINDPWDFILE="/etc/ldapscripts/ldapscripts.conf', line.rstrip())
                                	if(homedir):
                                        	line = re.sub(r'(.*)CREATEHOMES=\"(.*)\"', 'CREATEHOMES="yes"', line.rstrip())
                                	new_file.write(''.join([line.strip(),"\n"]))

        	close(fh)
        	#Remove original file
        	remove(file_path)
        	#Move new file
        	move(abs_path, file_path)
	
	def creatednName(self,domainName):
		dnName=""
		dc=domainName.split('.')
		for x in dc:
			dnName=''.join([dnName,"dc=",x,","])
		return dnName[:-1]

	def modifyLdapscriptConf(self,domainName,orgName,homedir):
		dnName=self.creatednName(domainName)
        	self.modifyConfFile("/etc/ldapscripts/ldapscripts.conf",dnName,orgName,homedir)

	def assignPassword(self,file_path,substr):
		with open(file_path,'w') as new_file:
			new_file.write(substr)



