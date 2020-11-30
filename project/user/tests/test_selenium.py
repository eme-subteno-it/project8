from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from user.models import User
from django.conf import settings
import time


class RegisterTests(StaticLiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(executable_path=settings.SELENIUM_DRIVER_PATH)
        self.wait = WebDriverWait(self.selenium, 1000)
        super(RegisterTests, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(RegisterTests, self).tearDown()
        return

    def define_elements(self):
        username_input = self.selenium.find_element_by_id('id_username')
        email_input = self.selenium.find_element_by_id('id_email')
        first_name_input = self.selenium.find_element_by_id('id_first_name')
        last_name_input = self.selenium.find_element_by_id('id_last_name')
        password1_input = self.selenium.find_element_by_id('id_password1')
        password2_input = self.selenium.find_element_by_id('id_password2')
        subscribed_input = self.selenium.find_element_by_id('id_subscribed')

        username_input.send_keys('test_username')
        email_input.send_keys('email@test.com')
        first_name_input.send_keys('test_first_name')
        last_name_input.send_keys('test_last_name')
        password1_input.send_keys('test_password_61')
        password2_input.send_keys('test_password_61')
        subscribed_input.click()

    def test_register_click(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        subscribed_input = self.selenium.find_element_by_id('id_subscribed')
        submission_button = self.selenium.find_element_by_id("id_signup")
        self.define_elements()

        # Wait until the response is received
        self.wait.until(lambda driver: subscribed_input.is_selected())
        ActionChains(self.selenium).click(submission_button).perform()

        time.sleep(2)
        redirection_url = self.selenium.current_url
        self.assertEqual(self.live_server_url + '/my/account/', redirection_url)

    def test_register_keyboard(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/register/'))
        password2_input = self.selenium.find_element_by_id('id_password2')
        self.define_elements()

        password2_input.send_keys(Keys.ENTER)
        time.sleep(2)
        redirection_url = self.selenium.current_url
        self.assertEqual(self.live_server_url + '/my/account/', redirection_url)


class LoginTests(StaticLiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(executable_path=settings.SELENIUM_DRIVER_PATH)
        self.wait = WebDriverWait(self.selenium, 1000)
        User.objects.create_user(
            username='test_username',
            first_name='test_first_name',
            last_name='test_last_name',
            email='email@test.com',
            password='test_password_61',
            subscribed=True
        )
        super(LoginTests, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LoginTests, self).tearDown()
        return

    def define_elements(self):
        username_input = self.selenium.find_element_by_id("id_username")
        password_input = self.selenium.find_element_by_id("id_password")
        username_input.send_keys('test_username')
        password_input.send_keys('test_password_61')

    def test_login_click(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        submission_button = self.selenium.find_element_by_id("id_login")
        self.define_elements()

        # Wait until the response is received
        self.wait.until(lambda driver: self.selenium.find_element_by_tag_name('body'))
        ActionChains(self.selenium).click(submission_button).perform()

        time.sleep(2)
        redirection_url = self.selenium.current_url
        self.assertEqual(self.live_server_url + '/my/account/', redirection_url)

    def test_login_keyboard(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        self.define_elements()
        password_input = self.selenium.find_element_by_id("id_password")

        password_input.send_keys(Keys.ENTER)
        time.sleep(2)
        redirection_url = self.selenium.current_url
        self.assertEqual(self.live_server_url + '/my/account/', redirection_url)
