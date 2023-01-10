class Software():
    #Instance attribute
    def __init__(self):
        self.__version = 1
     
    # Instance method
    def getVersion(self):
        print(self.__version)
 
    def setVersion(self, version):
        self.__version = version
 
# instanstiate objek Software
obj = Software()
obj.getVersion()
obj.setVersion(3)
obj.getVersion()