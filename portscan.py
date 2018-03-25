# -*- coding: UTF-8 -*-
import argparse
import socket
import select

# constants
MAX_PORT = 65535
SOCK_TIMEOUT = 1
VERBOSE = False

# given a string of range or single number, return a list of sufix(es)
def preprocess_range(r):
    # convert strings to integer numbers
    rg = [int(n) for n in r.split("-")]
    # check length of rg array
    if len(rg) > 1:
        # list of sufixes range
        range_list = range(rg[0], rg[1]+1)
    else:
        # single sufix
        range_list = [rg[0]]
    # check if interval is valid
    if len(range_list) > 0:
        # valid, return range list
        return range_list
    else:
        # throw exception
        raise ValueError('Invalid range.')

# receive an ip range or single ip as input and return a list of ips
# example: 192.168.0.1 returns ["192.168.0.1"]
#          192.168.0.1-3 returns ["192.168.0.1", "192.168.0.2", "192.168.0.3"]
def preprocess_ip(ip):
    # split ip by "."
    split_ip = ip.split(".")
    # get last ip number
    ip_range = split_ip.pop()
    # build ip prefix
    prefix = '.'.join(split_ip)
    # check if it is a range or single number
    sufixes = preprocess_range(ip_range)
    # build ip list
    ips = []
    # iterate over sufixes
    for s in sufixes:
        # build ip
        ips.append(prefix + "." + str(s))
    # return ips list
    return ips

# params parsing method, including strings preprocessing
def params(ports=range(1,MAX_PORT+1)):
    parser = argparse.ArgumentParser()
    # argument ip
    parser.add_argument('ip', help='Server IP or IP ranges separated by "-"')
    # optional argument port
    parser.add_argument('port', nargs='?', help='Port or port ranges separated by "-"')
    # optional argument port
    parser.add_argument('--verbose', help='Enable verbose scanning', action='store_true')
    params = parser.parse_args()
    VERBOSE = params.verbose
    # preprocess ip string
    ips = preprocess_ip(params.ip)
    # check if port exists
    if params.port:
        # preprocess port string
        ports = preprocess_range(params.port)
    return ips, ports

# check if verbose is enabled and print the string
def print_verb(str):
    if VERBOSE:
        print str

# connect to an ip and port and return its socket
def connect(ip,port):
    # print port info
    print_verb("Connecting to ip " + ip + " on port " + str(port) + ".")
    try:
        # set default timeout
        socket.setdefaulttimeout(SOCK_TIMEOUT)
        # create socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to ip on port
        s.connect((ip,port))
        # if not exeption, port is open
        print "Port", str(port), "is open."
        # get service name
        service = socket.getservbyport(port)
        # print service name
        print "Service:", service
        # return socket
        return s
    except:
        # port closed
        print_verb("Port " + str(port) + "is closed.")
        # close socket
        s.close()
        # return None
        return None

# print banner given a socket
def banner(s):
    try:
        # send a message
        s.send('I want your banner\r\n')
        # receive banner
        ban = s.recv(4096)
        # print baner
        print str(ban)
    except:
        # exeption: banner error
        print "Unable to get any banner."
    # close socket
    s.close()

# main program
def main():
    # get parameters
    ips, ports = params()
    # iterate over ips
    for ip in ips:
        print "Scanning ip", ip + "..."
        # iterate over ports
        for port in ports:
            # connect to ip on port
            s = connect(ip,port)
            # check if socket is valid
            if s:
                # print banner
                banner(s)

if __name__ == "__main__":
    main()
