
import subprocess
from subprocess import Popen,PIPE
from tempfile import mkstemp
from shutil import move
from os import remove, close
import re


class LDAPInstall:

	def killProcess(self,var):
		processids=[]
		fh, abs_path = mkstemp()
        	#with open(abs_path,'w') as new_file:
			#pout=Popen(["sudo","ps","aux"],stdout=PIPE)
			#abs_path.write(pout.stdout.read())
			#print(pout.stdout.read())
			#pout=Popen(["grep","$var","abs_path"],stdin=PIPE,stdout=PIPE)
			#abs_path.write(pout.stdout.read())'
		#with open(abs_file) as file:
			#for line in file:
				#line=re.sub(r'[.*\t]*', r'\2', line.rstrip())
				#processids.append(line)
				#print(line)
		#close(fh)

	def upgrade(self):
		pout=Popen(["sudo","apt-get","update"],stdin=PIPE,stderr=PIPE)
		pout.wait()		
		#if(stderr!=""):
			#self.killProcess("apt")
	
	def installTkinter(self):
		pout=Popen(["sudo","apt-get","install","python-tk"])
		pout.wait()
		
	def updateLDAPUtils(self,password1,password2):
		pout=Popen(["sudo","apt-get","install","-y","slapd","ldap-utils"],stdin=PIPE)
		pout=Popen(["sudo","echo","$password1"])
		pout=Popen(["sudo","echo","$password2"])
		pout.wait()

	def replaceDomainName(self,file_path, pattern, string_to_add):
    		#Create temp file
    		fh, abs_path = mkstemp()
    		with open(abs_path,'w') as new_file:
        		with open(file_path) as old_file:
            			for line in old_file:
                			substitute=''.join([line.strip(), string_to_add, r' \1'])
                			line = re.sub(r'127\.0\.1\.1\t(.*)', substitute, line.rstrip())
					new_file.write(''.join([line.strip(),"\n"]))
			
    		close(fh)
    		#Remove original file
    		remove(file_path)
    		#Move new file
    		move(abs_path, file_path)
	
	def writeDomainName(self,domainName):
		self.replaceDomainName("/etc/hosts",r'127\.0\.1\.1\t(.*)',''.join([".",domainName]))

	def reconfigSLDAP(self):
		subprocess.call(["sudo","dpkg-reconfigure","slapd"])

	def connectLDAPFirewall(self):
		pout=Popen(["sudo","ufw","allow","OpenLDAP LDAP"],stdin=PIPE)
		pout=Popen(["sudo","ufw","status"],stdout=PIPE,stdin=PIPE,stderr=PIPE)		
		str=pout.stdout.read()
		if(str.rstrip()=="Status: inactive"):
			print("UFW Status: inactive")

	def installphpldapadmin(self):
		pout=Popen(["sudo","apt-get","install","-y","phpldapadmin"],stdin=PIPE)

	def configphpldapadmin(self):
		pout=Popen(["sudo","nano","/etc/phpldapadmin/config.php"],stdin=PIPE)



