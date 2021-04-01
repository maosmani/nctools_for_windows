import click 
import os
import whois
from ipaddress import ip_address 
import socket
from ipwhois import IPWhois
from pprint import pprint
#THis part is for the working code

def IPAddress(IP: str) -> str: 
    return "Private" if (ip_address(IP).is_private) else "Public"
#os.system('cmd /k netstat')
#This part of the code will create a file and write all connection on the device to it.
def write():
    file = open('empty.txt',"w")
    netstat = os.popen(' netstat -n').read()
    file.write(netstat + "\n")
    file.close()
    # Read lines as a list
    fh = open("empty.txt", "r")
    lines = fh.readlines()
    fh.close()
    # Weed out blank lines with filter
    lines = filter(lambda x: not x.isspace(), lines)
    # Write
    fh = open("out.txt", "w")
    for line in lines:
        if line.strip("\n") != "line1":
        	fh.write("".join(lines))

    fh.close()

    lines = open('out.txt', 'r').readlines() 
    lines =lines[1:] 
    open('out.txt', 'w').writelines(lines) 

def whois():

    logFile = open("out.txt", "r")
    i = 0
    for line  in logFile:

        
        s = line.split()
        x = s[2]
       
        ip = x.split(":")
        ipLook = ip[0]
        port = ip[1]

        ipLook = socket.gethostbyname(ipLook)
        ipType =    IPAddress(ipLook)
        
        if ipType == "Public":
            obj = IPWhois(ipLook)
            results = obj.lookup_whois()
            print(i,results['asn_description'])
            #pprint(obj.lookup_whois())
            #print(socket.getfqdn(ipLook))#This part of the code will get you the domains and ip addresses where your device is connected to

        else:
            print(i,'The ip address : ' + ipLook + "  it is privite ip address!!!")
                
        i=i+1
#This part is for the code that command line use
@click.group()
def main():
  pass


@click.command()
def connections():
    click.echo('just wait and you will get the list of all connections')
    write()
    with open('out.txt') as file:
    	lines = file.readlines()
    	for line in lines:
    		click.echo(line)


@click.command()
def whois():
    click.echo('Welcome this will give you the connections whois')
    whois()


main.add_command(connections)
main.add_command(whois)


if __name__ == '__main__':
    main()