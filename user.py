import pyperclip

class User:
    """
    Class that generates new instances of users
    """
    
    user_list = [] 
    '''
    Variables that belong to the entire class and can be accessed by all instances of the class.
    Used to store our created contact objects .
    '''

    def __init__(self,username,email,password):

      #docstring removed for simplicity

        self.username = username
        self.email= email
        self.password= password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in an email and returns an user that matches that email.

        Args:
            email: email address to search for 
        Returns:
            User of person that matches the email.
        '''

        for user in cls.user_list:
            if user.email == email:
                return user

    @classmethod
    def user_exists(cls,email):
        '''
        Method that checks if an user exists from the user list.
        Args:
            email: email address to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.email == email:
                return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    
    
    @classmethod
    def copy_email(cls,email):
        user_found = User.find_by_email(email)
        pyperclip.copy(user_found.email)


    
       