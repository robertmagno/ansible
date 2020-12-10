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
  os.system("sudo apt-add-repository ppa:ansible/ansible")
  print("Done")	
  
  os.system("sudo apt update -y > /dev/null")  

  print("***Installing pip***")
  os.system("sudo apt install python-pip -y > /dev/null")
  print("Done")

  print("***Installing Ansible***")
  os.system("sudo apt install ansible -y > /dev/null")
  print("Done")
	
  print("***Cloning Citrix ADC Ansible Repository***")
  os.system("git clone https://github.com/citrix/citrix-adc-ansible-modules.git > /dev/null")
  print("Done")
  
  print("***Install Nitro API Python Dependencies***")
  os.system("pip install /home/ubuntu/ansible/citrix-adc-ansible-modules/deps/nitro-python-1.0_kamet.tar.gz")
  print("Done")

  print("***Building ADC Modules and Plugins***")
  os.system("ansible-galaxy collection build /home/ubuntu/ansible/citrix-adc-ansible-modules/ansible-collections/adc")
  print("Done")

  print("***Installing ADC Modules and Plugins***")
  os.system("ansible-galaxy collection install citrix-adc-1.0.0.tar.gz")
  print("Done")

  print("***Building ADM Modules and Plugins***")
  os.system("ansible-galaxy collection build /home/ubuntu/ansible/citrix-adc-ansible-modules/ansible-collections/adm")
  print("Done")

  print("***Installing ADM Modules and Plugins***")
  os.system("ansible-galaxy collection install citrix-adm-1.0.0.tar.gz")
  print("Done")

if __name__ == '__main__':
	main()
