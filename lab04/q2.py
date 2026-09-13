class PasswordVault:
    def __init__(self, username, vault_status, password):
        self.username = username
        self._vault_status = vault_status
        self.__password = password
    def verify_password(self, verifyPass):
        if verifyPass == self.__password:
            print("access granted")
            return True
        else:
            print("access denied")
            return False
    def change_Password(self, verifyPass):
        if self.verify_password(verifyPass):
            print("Enter New Password: ")
            newPassword = input()
            self.__password = newPassword

    def display_status(self):
        print("status: ", self._vault_status)
user1 = PasswordVault("AaishaMunir","Active","0031")
user1.display_status()
user1.change_Password("0031") #as input ill change it to 25k-0031
user1.verify_password("25k-0031")