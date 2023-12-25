from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
	ids = dict()
	with open('locators.yaml') as f:
		locators = yaml.safe_load(f)
	for locator in locators['xpath'].keys():
		ids[locator] = (By.XPATH, locators['xpath'][locator])
	for locator in locators['css'].keys():
		ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
	def enter_text_info_field(self, locator, word, description=None):
		if description:
			element_name = description
		else:
			element_name = locator
		field = self.find_element(locator)
		logging.debug(f"Send {word} of element {element_name}")
		if not field:
			logging.error(f'Element {locator} not found')
			return False
		try:
			field.clear()
			field.send_keys(word)
		except:
			logging.exception(f'Exception while operation with {locator}')
			return False
		return True

	# ENTER TEXT
	def enter_login(self, word):
		self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login')

	def enter_pass(self, word):
		self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='pass')

	def enter_contact_name(self, word):
		self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_CONTACT_NAME_FIELD'], word, description='contact name')

	def enter_contact_email(self, word):
		self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_CONTACT_EMAIL_FIELD'], word, description='contact email')

	def enter_contact_content(self, word):
		self.enter_text_info_field(TestSearchLocators.ids['LOCATOR_CONTACT_CONTENT_FIELD'], word,
									   description='contact content')

	# CLICK
	def click_button(self, locator, description=None):
		if description:
			element_name = description
		else:
			element_name = locator
		button = self.find_element(locator)
		if not button:
			return False
		try:
			button.click()
		except:
			logging.exception('Exception with click')
			return False
		logging.debug(f"Click {button} button")
		return True

	def click_login_button(self):
		self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login')

	def click_contact_link(self):
		self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_LINK'], description='contact')

	def click_contact_us_button(self):
		self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'], description='contact us')

	# GET
	def get_text_from_element(self, locator, description=None):
		if description:
			element_name = description
		else:
			element_name = locator
		field = self.find_element(locator, time=3)
		if not field:
			return None
		try:
			text = field.text
		except:
			logging.exception(f'Exception while get test from {element_name}')
			return None
		logging.debug(f"We find text {text} in  field {field}")
		return text

	def get_error_text(self):
		return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='error text')

	def get_success_text(self):
		return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_SUCCESS_FIELD'], description='success text')

	def get_go_to_contact_text(self):
		return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_GO_TO_CONTACT'], description='go to contact')

	def log_in(self, login, password):
		logging.info('Log in to the site')
		self.go_to_site()
		self.enter_login(login)
		self.enter_pass(password)
		self.click_login_button()

	def get_alert_text(self):
		alert = self.driver.switch_to.alert
		try:
			text = alert.text
		except:
			logging.exception(f"Exception with alert")
			return None
		logging.info(f"We find text '{text}' after click contact us button")
		return text