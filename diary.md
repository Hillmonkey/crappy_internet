
# Sat Feb 3

* Install Raspian operating system on MicroSD
* Get rid of default passwords on RaspPi
  * Some blogs indicate that existence of user Pi is necessary :(
* Setup new user on RaspPi
* Investigate hosting @ PythonAnywhere
  * Only one scheduled task per day
  * No root, no access to crontab :(

# Sun Feb 4

* Go on a hike at Lands End :)
* Work on printing resumes for Dev Hiring Mixer
* Deal with intermittent internet outages ...
* Complete payment on OVH server
* Follow Guide to secure the server
* Try setting up DigitalOcean server, due to hardship @ OVH

# Mon Feb 5

* Go to Dev Hiring Mixer
* ssh working on DigitalOcean server
* PingPi v1 is now ready to run on DigitalOcean droplet

# Tue Feb 6

* Trying different solutions to run a lightweight python based server on RaspPi
* Help friend with coding in C
* Found a workable python based server
* set and lost my password! used System Rescue CD to change my password

# Wed Feb 7

* determined that I need to set up port forwarding to shell into RPi remotely

# Thur Feb 8

* There is an album by the English Beat.
* It's called Wh'appen?

# Fri Feb 9

* call ATT service because password for router configuration doesn't work
* ATT can't remotely update my router password, but they can send me another router by FedEx!
* work on installing Graphite database on RPi
* Graphite installed
* TODO later: study /etc/carbon/carbon.conf
* http://graphite-api.readthedocs.io/en/latest/deployment.html
* looking for httpd.conf, but it's apache2.conf in Ubuntu
* RaspPi comes default with Great Britain settings - wtf?
* wifi goes down at school?!?

# Sat Feb 10

* new router arrives by FedEx, switch over time set for 2pm PDT
* install router, interact with online help to resolve issues
* NEXT: attempt, once again to set up port forwarding
* working with different stack overflow articles, apparently things have
	changed from Debian Wheezy to Debian Jessie
* one milestone: updated dhcpcd.conf, this successfully sets static IP for
	rasp pi on local network ...
* ATT router does not allow configuration of DDNS at the router, however this looks like a good resource:
* https://help.ubuntu.com/community/DynamicDNS
* TEST: unwind changes to dhcpcd.conf

# Sun Feb 11

* Why /etc/network/interfaces is deprecated for Debian Jessie:
https://raspberrypi.stackexchange.com/questions/39785/dhcpcd-vs-etc-network-interfaces

