import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    #Items up here....

    def setUp(self):
        '''
        Set up method to ru before each test cases.
        '''
        self.new_credentials = Credentials("Gesare","Wattpad","Ges","Gesare@gmail.com","sk3010") 

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.accountName,"Gesare")
        self.assertEqual(self.new_credentials.siteName,"Wattpad")
        self.assertEqual(self.new_credentials.username,"Ges")
        self.assertEqual(self.new_credentials.email,"Gesare@gmail.com")
        self.assertEqual(self.new_credentials.password,"sk3010")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials() #saving the new credentials
        self.assertEqual(len(Credentials.Credentials_list),1)

#setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.Credentials_list = []

#other test cases here

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials objects to our Credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Stephen","Linktin","Gummybear","gummybear@gmail.com","GOA2711") #new credentilas
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exists("gummybear@gmail.com")

        self.assertTrue(credentials_exists)

        found_credentials = Credentials.find_by_email("gummybear@gmail.com")

        self.assertEqual(found_credentials.username,test_credentials.username)

        self.new_credentials.delete_credentials() #deleting credentials object 
        self.assertEqual(len(Credentials.Credentials_list),1)

#more tests above
    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credentials from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Stephen","Linktin","Gummybear","gummybear@gmail.com","GOA2711") #new credentilas
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials() #deleting credentials object 
            self.assertEqual(len(Credentials.Credentials_list),1)

    def test_find_credentials_by_email(self):
            '''
            test to check if we can find the credentials by email and display information
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Stephen","Linktin","Gummybear","gummybear@gmail.com","GOA2711") # new Credentials
            test_credentials.save_credentials()
            found_credentials = Credentials.find_by_email("gummybear@gmail.com")

            self.assertEqual(found_credentials.email,test_credentials.email) 

    def test_credentials_exists(self):
            '''
            test to check if we can return a Boolean if we cannot find the credentials.
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Stephen","Linktin","Gummybear","gummybear@gmail.com","GOA2711") # new Credentials
            test_credentials.save_credentials()

            credentials_exists = Credentials.credentials_exists("gummybear@gmail.com")

            self.assertTrue(credentials_exists)
            
    def test_display_credential(self):
            '''
            method that retuns a list of all credential saved
            '''
            self.assertEqual(Credentials.display_credential(),Credentials.Credentials_list)
            

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found credentials
        '''
        
        self.new_credentials.save_credentials() 
        Credentials.copy_credentials("gesare@gmail.com")
        
        self.assertEqual(self.new_credentials.email,pyperclip.paste())
        

if __name__ == '__main__':
    unittest.main()#provides a command line interface that collects all the tests methods and executes them 
    '''
    we are confirming that anything inside the if block should run only if this is the file that is currently being run.
    '''
