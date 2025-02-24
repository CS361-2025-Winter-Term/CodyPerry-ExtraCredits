from UserProfile import UserProfile

class UserStorageManager:
    def __init__(self):
        #Constructor, pass all necessary values
        self.__userProfiles = []
        pass

    def findUserByUsername(username: str):
        #Seraches the userProfiles list for a spefific username.
        #Set AuthenticationManager's registration status to "USER_ALREADY_EXISTS and 
        # call a username already exists error if it exists
        #Call saveUserToDatabase() if it does not exist
        return
    
    def __saveUserToDatabase(userProfile: UserProfile):
        #Saves the user to the database
        #If it's successful, set AuthenticationManager's registration to "SUCCESS", call transitionToHomeView()
        #Otherwise, set it to "UNKNOWN_ERROR", call displayError()
        return