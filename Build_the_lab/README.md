# Excercise 1: Build the Lab

# Environment
  I chose to use GNS3 for creating a virtual lab as I am most familiar with how it works. The lab is a simple network consisting of three parts. I wanted to have both layer 2 and layer 3 devices to work with in the lab. I have pre-provisioned connectivity,basic routing, and authentication on the devices so that I can gather information about the network from the network management server. I am using all Cisco based virtual images for the network devices. Thoughts on the simulated PCs - automate vlans, dhcp configuration and test connectivity via/to the PCs. 

 1. Main location - Subnet 10.10.0.0/20
    1. two managed switches
	2. two routers
	3. unmanaged "management" switch
	4. Network management ubuntu based server with tools installed: ansible, napalm, netmiko, pyntc, and git
	5. two simulated pcs
 2. Remote location - Subnet 10.10.1.0/20
    1. one managed switch
	2. one managed router
	3. one simulated pc
 3. Provider routers that interconnect the main location to the remote location.
    1. ISP1 - Subnet 10.42.1.0/24
    2. ISP2 - Subnet 10.42.2.0/24

# Physical Network Diagram
![alt text](images/network-diagram.png "Network Diagram")
# Layer 3 Network Diagram
![alt text](images/network-diagram-l3.png "Layer 3 Network Diagram") 

# GNS3 configuration
I am using GNS3 version 2.1.3 with the separate GNS3 server VM. The GNS3 server VM runs in VMWARE Player 12.5. The network manager server also runs in VMWARE Player 12.5. I had to create a loopback device on my laptop (Windows 10) and bridge that to a VMWARE virtual nic (vmnet2). I then created another nic on the GNS3 VM and attached it to vmnet2. I created a "cloud" object in GNS3 that runs on the GNS3 server VM and the cloud object is connected to the third interface on the VM which bridges a  device running inside the GNS3 server VM to the network manager server VM running in parallel to the GNS3 server VM.

# What I have learned so far. 
One thing I would like to do next time is to connect the network management server to "OOB" on all of the devices and "provision" more of the network with a tool. I spent a lot of time getting the network up and working and I feel that the time could have been better spent getting the automation working. In real life we don't always have OOB everywhere so this lab IS somewhat closer to what I have to deal with in everyday life. I also started to use the "network automation" docker image appliance from the GNS3 marketplace but found it lacking in some respects - it did not come with git! I am not that familiar with docker and did not want to go down the road of reworking the docker image or creating a docker image from scratch so I built an Ubuntu linux VM and put all of the tools there that I would need thus far. I could also add/change easily if desired. Odd issue with IOSv - transport input none is set on vty. I used Ubuntu 16.04 and had issues with getting a simple cli ping to work "ansible ios -c local -m ping". Researching this issue led to many "Answers" from the internet - most of them saying to install Python 2.7. Which I diligently did and then found that was maybe the wrong thing to do as it broke other things. Ubuntu 16.04 has Python 3.5 as standard and Python 2.x is not installed by default. What I found is that if I put a symlink for python to python3.5 then everything worked as it should and I didn't need to install Python 2.7. Also playbooks involving "ios_command" would have errors related to "sshpass" not being installed. This is also incorrect as sshpass is not required. "Connection = local" is required. 

# Ansible
After a lot of trial and error I was able to get a playbook to run properly. I learned how to create a hosts file, ansible.cfg file, playbook file, and then run ansible at the command line with the correct switches to use different modules such as ping, raw, paramiko, and ios_command. Using ansible at the command line was helpful in determining the issues I had with the playbook. A LOT more learning to be done around playbooks, yaml syntax, and ansible commands. I cobbled together a playbook using material I found on ipspace.net, ansible official documentation, and from Roger Perkins blog. The playbook does a "show run" on the devices and then writes the output to separate files named with each device name. Ansible configuration, hosts, playbook, and output files are in the ansible directory. I was able to use ansible to collect the device pre-provisioned configs and write them out to a file for documentation purposes.
