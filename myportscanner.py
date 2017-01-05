import argparse
from socket import *
from threading import *
 
screenLock = Semaphore(value=1)
<a name="more"></a>

def connectTest(tHost, tPort):
    try:
        conn = socket(AF_INET, SOCK_STREAM)
        conn.connect((tHost, tPort))
        conn.send('Hello guys\n')
        results = conn.recv(80)
        screenLock.acquire()
        print '[+] %d tcp open' % tPort
        print '[+] banners : '+str(results)+'\n'
        conn.close()
    except:
        screenLock.acquire()
        print '[-] %d tcp closed' % tPort
    finally:
        screenLock.release()
        conn.close()
 
def scanningPort(tHost, tPorts):
    try:
        tIP = gethostbyname(tHost)
    except :
        print "[-] Cannot resolve '%s' : Unknown host"+tIP
        return
 
    try:
        tName = gethostbyaddr(tHost)
        print '[+] Scan Results : '+tName[0]+'\n'
    except:
        print '[-] Scan Results : '+tIP+'\n'
     
    setdefaulttimeout(1)
     
    for tPort in tPorts:
        get = Thread(target=connectTest, args=(tHost, int(tPort)))
        get.start()
 
def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-H', action='store', dest='tHost', help='specify target host')
    parser.add_argument('-p', action='store', dest='tPort', help='specify target ports (separated by comma)')
     
    arguments = parser.parse_args()
 
    tHost = arguments.tHost
    tPorts = str(arguments.tPort).split(',')
 
    if (tHost == None) | (tPorts == None):
        print "Please specify your target host and ports !!\nTry 'portscan.py --help' for more information"
        exit(0)
 
    scanningPort(tHost, tPorts)
 
if __name__ == '__main__':
    main()

    # contact me ©Thariq Alfa.
    # www.zrav420.rf.gd.
    # open source.
    # zravproject.
    # how to run this code for scan port  site?.
    # open your terminal and run "python myportscanner.py -H www.site.com -p 21,22,25,80,110,443".
    # "21,22,25,80,110,443" this is port, you can add more port.