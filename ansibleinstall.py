import os
from time import sleep 
import logging

class SSH:
    def __init__(self):
        pass
        
def main():
  print("***Installing software dependencies***")
  os.system("sudo apt-get install software-properties-common -y > /dev/null")
  print("Done")
	
  print("***Adding Ansible Repository***")
  os.system("sudo apt-add-repository ppa:ansible/ansible > /dev/null")
  print("Done")	
  
  os.system("sudo apt-get update -y > /dev/null")  
  
  print("***Installing Ansible***")
  os.system("$ sudo apt install ansible -y > /dev/null")
  print("Done")
	
  print("***Installing pip***")
  os.system("sudo apt install python-pip -y > /dev/null")
  print("Done")
	
  print("***Cloning Citrix ADC Ansible Repository***")
  os.system("git clone https://github.com/citrix/citrix-adc-ansible-modules.git > /dev/null")
  print("Done")
  
  print("***Install Nitro API Python Dependencies***")
  os.system("pip install /home/ubuntu/ansible/citrix-adc-ansible-modules/deps/nitro-python-1.0_kamet.tar.gz")
  print("Done")


#
#	print("***Adding Kubernetes Repository***")
#	os.system("echo 'deb http://apt.kubernetes.io/ kubernetes-xenial main' | sudo tee /etc/apt/sources.list.d/kubernetes.list > /dev/null")
#	print("Done")
#	
#	print("***Updating package lists***")
#	os.system("sudo apt-get update > /dev/null")
#	print("Done")
