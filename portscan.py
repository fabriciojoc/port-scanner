# -*- coding: UTF-8 -*-
import argparse

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
def params(ports=None):
    parser = argparse.ArgumentParser()
    # argument ip
    parser.add_argument('ip', help='Server IP or IP ranges separated by "-"')
    # optional argument port
    parser.add_argument('port', nargs='?', help='Port or port ranges separated by "-"')
    params = parser.parse_args()
    # preprocess ip string
    ips = preprocess_ip(params.ip)
    # check if port exists
    if params.port:
        # preprocess port string
        ports = preprocess_range(params.port)
    return ips, ports

# main program
def main():
    # get parameters
    ips, ports = params()
    print ips, ' ', ports


if __name__ == "__main__":
    main()
