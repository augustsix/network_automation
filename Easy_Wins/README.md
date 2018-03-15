# Excercise 2: Easy Wins

# Overview
  Collect information from the network and create a summary report from the collected information.

# What I have learned so far.
 Read the docs! I made a simple napalm-ansible playbook using napalm_get_facts and could not get it to work. After reading the napalm-ansible documentation I found out that my problem was easily solved by running napalm-ansible at the cli before trying to write any playbooks. I had some missing defaults in my ansible.cfg file. 
