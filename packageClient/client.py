class Client:
    def __init__(self, companyName, clientName, clientPhone, clientStatus):
        self.companyName = companyName
        self.clientName = clientName
        self.clientPhone = clientPhone
        self.__clientStatus = clientStatus

    def __str__(self):
        return f"The client {self.clientName} belongs to {self.companyName} company. His contact is {self.clientPhone}" 

    def updatePhone(self, newPhone):
        self.clientPhone = newPhone
        print(f"Client Phone has been updated succesfully")

    def seeClientStatus(self):
        return self.__clientStatus