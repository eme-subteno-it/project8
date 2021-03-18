""" All tests with Selenium for the product views application """
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


class SubstitutesTests(StaticLiveServerTestCase):
    """ Class to test the form register account """

    fixtures = ['substitutes.json']

    def setUp(self):
        self.selenium = webdriver.Chrome(
            ChromeDriverManager().install(),
            chrome_options=chrome_options
        )
        self.wait = WebDriverWait(self.selenium, 1000)

        super(SubstitutesTests, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(SubstitutesTests, self).tearDown()

    def test_click_number_substitutes_list(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/search/substitutes/1/'))

        number_btn = self.selenium.find_element_by_class_name('btn-nb')
        number_btn.click()

        self.wait.until(lambda driver: number_btn.get_attribute('class') == 'btn btn-nb active')

        form_save_substitute = self.selenium.find_elements_by_class_name('form-substitute-save')
        redirection_url = self.selenium.current_url
        self.assertEqual(self.live_server_url + '/search/substitutes/1/', redirection_url)
        self.assertEqual(len(form_save_substitute), int(number_btn.text))
