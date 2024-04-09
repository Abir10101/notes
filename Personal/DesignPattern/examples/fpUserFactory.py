class UserCreator:
    @abstractmethod
    def createUser():
        pass

    def getUserDetails(self) -> User:
        user = self.createUser()
        user.toJson()
        user.getPrivileges()
        return user

class AdminUserCreator(UserCreator):
    def createUser() -> User:
        return AdminUser()

class NormalUserCreator(UserCreator):
    def createUser() -> User:
        return NormalUser()

class User():
    @abstractmethod
    def toJson():
        pass

    @abstractmethod
    def getPrivileges():
        pass

class AdminUser(User):
    def toJson():
        user = db.connect.query(sql)
        return jsonEncode(user)

    def getPrivileges():
        privilges = db.connect.query(sql)
        return privilges

class NormalUser(User):
    def toJson():
        user = db.connect.query(sql)
        return jsonEncode(user)

    def getPrivileges():
        privilges = db.connect.query(sql)
        return privilges

class Driver():
    def main():
        adminUser = AdminUserCreator()
        normalUser = NormalUserCreator()
        print(adminUser.getUserDetails())
        print(normalUser.getUserDetails())
