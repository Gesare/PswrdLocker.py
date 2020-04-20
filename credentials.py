import pyperclip

class Credentials:
    """
    Class that generates new instances of credentials
    """

    Credentials_list = []

    def __init__(self,accountName,siteName,username,email,password):

      #docstring removed for simplicity
    
        self.accountName = accountName
        self.siteName = siteName
        self.username = username
        self.email = email
        self.password = password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into Credentials_list
        '''

        Credentials.Credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the Credentials_list
        '''

        Credentials.Credentials_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in an email and returns the credentials that matches that email.

        Args:
            email: email address to search for 
        Returns:
            Credentials of person that matches the email.
        '''

        for credentials in cls.Credentials_list:
            if credentials.email == email:
                return credentials

    @classmethod
    def credentials_exists(cls,email):
        '''
        Method that checks if the credentials exist from the Credentials list.
        Args:
            email: email address to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exist
        '''
        for credentials in cls.Credentials_list:
            if credentials.email == email:
                return True

        return False

    @classmethod
    def display_credential(cls):
        '''
        method that returns the credentials list
        '''
        return cls.Credentials_list
        


    @classmethod
    def copy_credentials(cls,email_add):
        credentials_found = Credentials.find_by_email(email_add)
        pyperclip.copy(credentials_found.email)
    
   
       