from UserProfile import UserProfile
from NotificationFrequency import NotificationFrequency
from NotificationPreferences import NotificationPreferences


class LoginView:
    def __init__(self):
        #Constructor, pass all necessary values
        self.username = ""
        self.password = ""
        self.email = ""
        self.frequency = None
        self.notificationPreferences = None

        pass

    def readUsernameTextbox():
        #Read a username and store it to self.username
        return
    
    def readPasswordTextbox():
        #Read a password and store it to self.password
        return
        
    def readEmailTextbox():
        #Read an email and store it to self.email
        return
    
    def readNotificationPreferences():
        #Read the user's notification preferences and create a notification preferences object. 
        #Also, update self.frequency and add it to the parameters

        #Then, create a userProfile object, using the notification preferences object as a parameter
        return
    
    def registerUser(userProfile: UserProfile, password: str):
        #Create an AuthenticationManager object, use its functions to validate the username, password, and email.
        #If any return false, return an error with a message corresponding to the invalid input
        return
    
    def displayError(message: str):
        #Displays an error message to the user
        return
        
