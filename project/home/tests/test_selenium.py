""" All tests with Selenium for the home views application """
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from django.conf import settings
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


class LanguagesTest(StaticLiveServerTestCase):
    """ Class to test the form the button for changing language """

    def setUp(self):
        self.selenium = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        self.wait = WebDriverWait(self.selenium, 1000)
        super(LanguagesTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(LanguagesTest, self).tearDown()

    def test_change_language(self):
        self.selenium.get('%s' % (self.live_server_url))
        button_language = self.selenium.find_element_by_id('dropdownLanguageButton')
        choice_language = self.selenium.find_elements_by_name('language')

        button_language.click()
        self.selenium.implicitly_wait(10)
        ActionChains(self.selenium).click(choice_language[1]).perform()

        time.sleep(2)
        redirection_url = self.selenium.current_url
        self.assertEqual(self.live_server_url + '/', redirection_url)
