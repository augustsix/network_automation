# Excercise 2: Easy Wins

# Overview
  Collect information from the network and create a summary report from the collected information.

Example:

ansible-playbook generic-reporting.yml --extra-vars "src=napalm_bgp_facts" --extra-vars "output=napalm_bgp_report.log" --extra-vars "report=napalm_bgp" --extra-vars "fmt=text"

  src = task that gathers data

  output = output file name

  report = the template to apply - must be able to use the data from the src task

  fmt = type i.e. text, html, etc

# What I have learned so far.
Read the docs!

I made a simple napalm-ansible playbook using napalm_get_facts and could not get it to work. After reading the napalm-ansible documentation I found out that my problem was easily solved by running napalm-ansible at the cli before trying to write any playbooks. I had some missing defaults in my ansible.cfg file. 

I started with examples from https://github.com/ipspace/ansible-examples. One goal was to add the cisco snmp string to all of my devices. I wanted to do it from a template as some time back I had been testing python with jinja2 templates. I thought I could incorporate some of that work into this project. 

Initially, I ran Ivan's code to "deploy" a basic snmp community string. Running the uptime report using snmp worked. 

I then tried using my jinja2 template and my variable file as input to Ivan's deployConfig.yml file. I had some issues with passing variables to the jinja2 template and learned about debugging variables from this excercise. 

I was eventually able to pass the variables required by using "--extra-vars" twice in the ansible-playbook command line by passing the template in and then passing the variable file in. 

Example: --extra-vars "src=snmp.j2" --extra-vars "@snmp.yml". 

This method does not work: --extra-vars "src=snmp.j2 @snmp.yml". The playbook cannot find the variables needed. 

Most of the examples on the net do not show mixing "including" a file and passing a key/value pair together. 

I ran into some issues traversing a dictionary in a jinja template. Also, I figured out how to "set" an ansible fact using conditionals.

