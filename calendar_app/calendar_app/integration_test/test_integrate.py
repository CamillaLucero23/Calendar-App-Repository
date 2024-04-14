from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'"C:\Users\quest\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe"')

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriver
from selenium.webdriver.common.by import BY
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

browser =webdriver.Firefox(
    service =FirefoService(GeckoDriverManager().install())

)

class integration_tests(StaticLiveServerTestCase):
    
    def setUpClass(self,cls):
        super().setUpClass()
        cls.selenium = WebDriver()


    def tearDownClass(self,cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_registration_happy(self):
        # Navigate to the registration page
        self.selenium.get(self.live_server_url + '/register')

        # Enter registration details
        self.selenium.find_element_by_id('id_username').send_keys('testuser')
        self.selenium.find_element_by_id('id_email').send_keys('test@example.com')
        self.selenium.find_element_by_id('id_password1').send_keys('testpass123')
        self.selenium.find_element_by_id('id_password2').send_keys('testpass123')
        self.selenium.find_element_by_id('register-button').click()

        # Simulate user login
        self.selenium.find_element_by_id('id_username').send_keys('testuser')
        self.selenium.find_element_by_id('id_password').send_keys('testpass123')
        self.selenium.find_element_by_id('login-button').click()

        # Assert user is logged in
        username_displayed = self.selenium.find_element_by_class_name('username-displayed')
        self.assertEqual(username_displayed.text, 'testuser')

    def test_user_registration_sad(self):
        # Navigate to the registration page
        self.selenium.get(self.live_server_url + '/register')

        # Enter registration details
        self.selenium.find_element_by_id('id_username').send_keys('')
        self.selenium.find_element_by_id('id_email').send_keys('test@example.com')
        self.selenium.find_element_by_id('id_password1').send_keys('testpass123')
        self.selenium.find_element_by_id('id_password2').send_keys('testpass123')
        self.selenium.find_element_by_id('register-button').click()

        username_displayed = self.selenium.find_element_by_class_name('username')
        self.assertEqual(username_displayed.text, 'testuser')

    def test_event_creation_happy(self):
        # Navigate to the registration page
        self.selenium.get(self.live_server_url + '/register')

        # Enter registration details
        self.selenium.find_element_by_id('id_username').send_keys('testuser')
        self.selenium.find_element_by_id('id_email').send_keys('test@example.com')
        self.selenium.find_element_by_id('id_password1').send_keys('testpass123')
        self.selenium.find_element_by_id('id_password2').send_keys('testpass123')
        self.selenium.find_element_by_id('submit').click()

        # Simulate user login
        self.selenium.find_element_by_id('id_username').send_keys('testuser')
        self.selenium.find_element_by_id('id_password').send_keys('testpass123')
        self.selenium.find_element_by_id('submit').click()

        # Navigate to profile page
        self.selenium.get(self.live_server_url + '/user')
        self.selenium.find_element_by_id('Add Element').click()

        #Add Element
        self.selenium.find_element_by_id('id_title').send_keys('test event')
        self.selenium.find_element_by_id('id_description').send_keys('This is a test event')
        self.selenium.find_element_by_id('id_date').send_keys('August 10 2024')
        self.selenium.find_element_by_id('id_time').send_keys('11:59:00')
        self.selenium.find_element_by_id('submit').click()

        event_displayed = self.selenium.find_element_by_class_name('event.title')
        self.assertEqual(event_displayed.text, 'test event')
    
    def test_event_creation_sad(self):
        # Navigate to the registration page
        self.selenium.get(self.live_server_url + '/register')

        # Enter registration details
        self.selenium.find_element_by_id('id_username').send_keys('testuser')
        self.selenium.find_element_by_id('id_email').send_keys('test@example.com')
        self.selenium.find_element_by_id('id_password1').send_keys('testpass123')
        self.selenium.find_element_by_id('id_password2').send_keys('testpass123')
        self.selenium.find_element_by_id('submit').click()

        # Simulate user login
        self.selenium.find_element_by_id('id_username').send_keys('testuser')
        self.selenium.find_element_by_id('id_password').send_keys('testpass123')
        self.selenium.find_element_by_id('submit').click()

        # Navigate to profile page
        self.selenium.get(self.live_server_url + '/user')
        self.selenium.find_element_by_id('Add Element').click()

        #Add Element
        self.selenium.find_element_by_id('id_title').send_keys('test event')
        self.selenium.find_element_by_id('id_description').send_keys('This is a test event')
        self.selenium.find_element_by_id('id_date').send_keys(`'')`
        self.selenium.find_element_by_id('id_time').send_keys('11:59:00')
        self.selenium.find_element_by_id('submit').click()

        event_displayed = self.selenium.find_element_by_class_name('event.title')
        self.assertEqual(event_displayed.text, 'test event')







    