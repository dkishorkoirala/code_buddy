class User:
    def __init__(self, password):
        # TODO: Store the password as a private attribute using double underscore (__)
        self.__password = password
        #       This makes it harder to access from outside the class

    def check_password(self, input_password):
        # TODO: Return True if input_password matches the stored private password
        if input_password == self.__password:
            return True
        #       Return False otherwise
        return False

    def change_password(self, old_password, new_password):
        # TODO: Check if old_password is correct using the check_password method
        if self.check_password(old_password):
            self.__password = new_password
            # TODO: If old_password is correct, update the private password to new_password and return True
            # TODO: If old_password is incorrect, return False without changing the password
            return True
        return False
