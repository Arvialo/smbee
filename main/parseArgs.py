import argparse

class ParseArgs:

    def getArgs(listArgs:tuple)->tuple:

        lhost=listArgs.lhost
        password=listArgs.password
        rhost=listArgs.rhost
        rport=listArgs.rport
        username=listArgs.username
        getContent=listArgs.content
        shares=listArgs.share
        download=listArgs.download

        return (lhost,rhost,rport,username,password,getContent,shares,download)

