from UserProfile import UserProfile

class AuthenticationManager:
    def __init__(self):
        #Constructor, pass all necessary values
        self.userProfile = None
        self.password = ""
        self.statusList = ["USER_ALREADY_EXISTS", "SUCCESS", "UNKNOWN_ERROR"]
        self.registrationStatus = ""
        pass

    def validateUsername(username: str) -> bool:
        #Ensures the username input meets all quidelines.
        return
        
    def validatePassword(password: str) -> bool:
        #The password input must follow the password rules.
        return
    
    def hashPassword():
        #Hashes the stored password
        return
    
    def validateEmail(email: str) -> bool:
        #Makes sure the email input is a valid email
        return
    
    def saveNewUser(userProfile: UserProfile, password: str):
        #Stores the user profile
        return