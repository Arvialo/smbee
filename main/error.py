class Error:
    def CredsError()->str:

        return """
        Error, authentication failed !
        """
    
    def HostError(rh,rp)->str:

        return """
        This host doesn't exist or is down ! (RHOST:\t%s\t\t|\t\tRPORT:\t%s)
        """.expandtabs(3)%(rh,rp)