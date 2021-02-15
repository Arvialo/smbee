import smb
from smb.SMBConnection import SMBConnection
from main.parseArgs import ParseArgs
from main.error import *
from shares.shares import sharesFunction


class smbConn:
    LHOST=""
    RPORT=445
    RHOST=""
    USERNAME=""
    PASSWORD=""
    GETCONTENT = False
    showShares = False
    DOWNLOAD=False


    def init(args):

        global LHOST,RPORT,RHOST,USERNAME,PASSWORD,dicShares,GETCONTENT,showShares,DOWNLOAD
        LHOST,RHOST,RPORT,USERNAME,PASSWORD,GETCONTENT,showShares,DOWNLOAD = ParseArgs.getArgs(args)

        sharesInfo = {}
        conn = smbConn.connection()
        shares = sharesFunction.getShares(conn)
        for share in shares:
            key,value = sharesFunction.isreadble(conn,share)
            key,value2 = sharesFunction.iswriteable(conn,share)
            sharesInfo[key] = (value,value2)

        """
            if '-s / --share' option
        """
        if showShares:
            print("\n\n\t\t\033[1m\033[4mList of Shares : \33[0m")
            for key,value in sharesInfo.items():
                print("%s"%(key).ljust(30),value[0],value[1])
        print('\033[0m')


        if DOWNLOAD:
            folder = input("put a folder to put all files : ")
        else:
            folder = ""

        """
            if '-c / --content' option
        """
        if GETCONTENT or DOWNLOAD:
            for key,values in sharesInfo.items():
                if "readable" in values[0]:
                    key = key.replace('\33[0m','')
                    if GETCONTENT:
                        print("\n\n\t\033[1m\033[4m ".ljust(30)+key.ljust(30)+"\33[0m")
                    sharesFunction.shareContent(conn,key,"/",[],1,DOWNLOAD,folder,GETCONTENT)


        conn.close()
        


    def connection():
        conn = SMBConnection(USERNAME, PASSWORD, LHOST,"server_name",use_ntlm_v2=True,is_direct_tcp=True)
        try:
            conn.connect(RHOST, RPORT)
        except:
            print(Error.HostError(RHOST,RPORT))
            exit()
        return conn
