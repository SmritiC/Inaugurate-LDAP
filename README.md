# Inaugurate LDAP

	This Project provides you with many automated scripts to install LDAP in your linux server. 
	When these Python scripts are run, it installs all necessary LDAP packages, LDAP utilities and LDAPSCRIPTS 
	in your linux server and connects to the firewall.

## Installation

	To install LDAP server, execute the installLDAP.py file in your linux server with root privileges. 
	Make sure that you login as root user before executing the script. 
	To login as root user use any of the following commands:
	$ sudo -s  
	$ sudo su
	and enter your password.

## Usage
	
	The automated installation of LDAP server upgrades all the packages and installs ldap-utils (if not 
	previously installed), adds your domain name and organization name into LDAP and installs ldapscripts with 
	which you can manage LDAP users.
	During LDAP installation, a window appears for you to enter password to be set for LDAP server.
	Then a window appears for entering your domain name and organization name.
	By default, Home directory will be created for all the users being added up in the LDAP server.
	After installation of ldapscripts, you will be authenticated to use the following commands to manage 
	the users in LDAP, with the LDAP server password itself.
	All ldap error codes and messages which are quite inconvenient to track are handled within the script code,
	for all ldap installation operations.

### Add Group 

	Using the following command, you can add a group:
	$ sudo ldapaddgroup group_name

### Add User

	Using the following command, you can add a user and specify which group he belongs to. 
	By default a home directory will be created for this user.
	$ sudo ldapadduser user_name group_name
	The password for the user's home directory can be changed using the following command:
	$ sudo ldapsetpassword user_name

### Delete User or Group

	Using the delete command, a user of a group can be deleted.
	$ sudo ldapdeleteuser user_name
	$ sudo ldapdeletegroup group_name

### Modify User
	
	Using modify command, you can modify any user's information
	$ sudo ldapmodifyuser user_name
	enter the modifications to be done
 


