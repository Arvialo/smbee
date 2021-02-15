from main.init import smbConn
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-rh","--rhost", help="specifies remote host", required=True)
    parser.add_argument("-rp", "--rport", help="specifies remote port", required=False,default=445)
    parser.add_argument("-lh","--lhost", help="specifies local host", required=False,default="tun0")
    parser.add_argument("-u","--username",help="set username",required=False,default="anonymous")
    parser.add_argument("-p","--password",help="set password ",required=False,default="anonymous")
    parser.add_argument("-c","--content",action="store_true",help="print all share content",required=False,default=False)
    parser.add_argument("-s","--share",action="store_true",help="print all shares and if it's writeable or readable",required=False,default=False)
    parser.add_argument("-d","--download",action="store_true",help="download all files",required=False)
    args = parser.parse_args()
    smbConn.init(args)
    
    