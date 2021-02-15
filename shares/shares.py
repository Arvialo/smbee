import smb
from smb.SMBConnection import *
import os
from main.error import Error

class sharesFunction:

    def getShares(conn):
        listOfShare = []
        try:
            shares = conn.listShares()
        except smb.base.NotReadyError:
            print(Error.CredsError())
            exit()
        for share in shares:
            listOfShare.append(share.name)
        return listOfShare



    def shareContent(conn,share,path,returnedContent,i,DOWNLOAD,folder,GETCONTENT):  
        try:
            contents = conn.listPath(share,path)
            for content in contents:
                returnedContent.append(content.filename)
                if content.isDirectory and content.filename not in ['.','..']:
                    if GETCONTENT:
                        print("\t\t"+"\t"*i+content.filename)
                    if path == "/":
                        sharesFunction.shareContent(conn,share,"/"+content.filename,returnedContent,i+1,DOWNLOAD,folder,GETCONTENT)
                    else:
                        sharesFunction.shareContent(conn,share,path+"/"+content.filename,returnedContent,i+1,DOWNLOAD,folder,GETCONTENT)
                elif content.filename not in ['.','..']:
                    if DOWNLOAD:
                        sharesFunction.download(conn,share,path,content.filename,folder,i,GETCONTENT)
                    else:
                        print("\t\t"+"\t"*i+"\33[31m"+content.filename+"\33[0m")
                        
        except smb.smb_structs.OperationFailure:
            returnedContent = []
        return returnedContent



    def download(conn,share,path,filename,folder,i,GETCONTENT):
        if not os.path.exists(folder+"/"+path):
            os.makedirs(folder+"/"+path+"/")
        file_obj = open(folder+"/"+path+"/"+filename,"wb")
        if path == "/":
            conn.retrieveFile(share,path+filename,file_obj)
        else:
            conn.retrieveFile(share,path+"/"+filename,file_obj)
        file_obj.close()
        if not GETCONTENT:
            print("\33[34m[+] UPLOADED !\33[0m\t\t"+"\t"+"\33[31m"+folder+path+"/"+filename+"\33[0m")
        else:
            print("\33[34m[+] UPLOADED !\33[0m\t\t"+"\t"*i+"\33[31m"+filename+"\33[0m")


    """
    check if share is readable
    """
    def isreadble(conn,share):
        BLUE = "\33[34m"
        RED = "\33[31m"
        GREEN = "\33[32m"
        WHITE = "\33[0m"

        dicShares = {}
        returnedContent = []
        try:
            shared = conn.listPath(share,'/')
        except smb.smb_structs.OperationFailure:
            dicShares[share] = ""
            return WHITE+share,dicShares[share]
        dicShares[share] = GREEN+"readable"
        return WHITE+share,dicShares[share]


    """
    check if share is writeable
    """
    def iswriteable(conn,share):
        BLUE = "\33[34m"
        RED = "\33[31m"
        GREEN = "\33[32m"
        WHITE = "\33[0m"

        dicShares = {}
        returnedContent = []
        try:
            uploads = conn.createDirectory(share,"/poc")
            dicShares[share] = GREEN+"writeable"
        except smb.smb_structs.OperationFailure:
            dicShares[share] = ""
        return WHITE+share,dicShares[share]