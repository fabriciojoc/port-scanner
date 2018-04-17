# Port Scanner

This port scanner is implemented in Python. It was presented as work of the "Introduction to Computer Security" course at the Federal University of Paraná (UFPR), Department of Informatics,
taught by [André Grégio](https://sites.google.com/site/argregio/) in 2018-1. This port scanner uses Python multiprocessing module, which allows a faster scan thought all ports. If available, it also
prints the application banner.

## Parameters
You can execute this program as follows:

> python portscan.py \<ip\> [ports] [--verbose]

The parameters listed above are the following:

 - **IP:** IP to be scanned (mandatory parameter). It can be a range of IPs with changes in sufix, only. For example "192.168.0.7-10" will scan all IPs between "192.168.0.7" and "192.168.0.10".
 - **Ports:** ports that are going to be scanned (optional parameter). It also can be a range. For example "10-100" will scan all ports between "10" and "100".
 - **\-\-verbose:** every action of the scan is printed in the screen.
