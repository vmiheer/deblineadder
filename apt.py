#!/usr/bin/env python
"""TODO:
1.please check if the local lines are already present
  if so just remove previous line and add new
"""
import os
import shutil
import datetime
IP="172.21.10.100"
BASEURL=""
available_archs=['x86_64','i386','i486','i586','i686']
available_distros=['lucid','natty','oneiric']
import re
def main():

#	re.compile(r"^[#]*deb[ ]+http[s]{1}://([\d]{1,3}[.]{1}){4}")
#	not working it is required to remove existing apt lines with
#	old ip addresses of repository
	"""get required information"""
	output=os.popen2("lsb_release -a")
	lines=output[1].readlines()
	for line in lines:
		if line.find("Codename") > 0:
			break
	codename=line.split('\t')[1].strip()
	arch=os.uname()[-1]
	if (arch not in available_archs) and (codename not in available_distros) :
		print("\nPlease install 62 bit Ubuntu version\n")
		return -1
	
	shutil.copy('/etc/apt/sources.list', '/etc/apt/sources.list.'+str(datetime.date.today()))
	"""backup exiting source file"""
	
	f1=open('/etc/apt/sources.list',"r")
	lines=f1.readlines()
	f1.close()
	f1=open('/etc/apt/sources.list',"w")
	for line in lines:
		if line[0] == '#':		#the line is already commented
			f1.write(line)
		else:
			f1.write('#'+line)	#comment line
	f1.write("\ndeb "+"http://"+IP+"/ubuntu/ "+codename+" main restricted universe multiverse\n")
	f1.write("\ndeb "+"http://"+IP+"/ubuntu/ "+codename+"-updates main restricted universe multiverse\n")
	f1.write("\ndeb "+"http://"+IP+"/ubuntu/ "+codename+"-backports main restricted universe multiverse\n")
	f1.write("\ndeb "+"http://"+IP+"/ubuntu/ "+codename+"-security main restricted universe multiverse\n")
	f1.write("\ndeb "+"http://"+IP+"/ubuntu/ "+codename+"-proposed main restricted universe multiverse\n")
	f1.close()
if __name__=='__main__':
	main()
