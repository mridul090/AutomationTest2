# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
PATH = "C:\Program Files (x86)\chromedriver.exe"

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://nmed-c.zssbd.com/auth/user/login/?next=/alerts/list/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("testdoc")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("Test123456")
        driver.find_element_by_id("clinicianLogin").click()
        driver.find_element_by_link_text("Patients").click()
        driver.find_element_by_id("add-btn").click()
        driver.find_element_by_name("clinic_patient_ref").clear()
        driver.find_element_by_name("clinic_patient_ref").send_keys("101020305332")
        driver.find_element_by_xpath("//input[@value='CHECK']").click()
        driver.find_element_by_link_text("ADD PATIENT").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("KKKKK")
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("KKKKK")
        driver.find_element_by_id("id_surname").clear()
        driver.find_element_by_id("id_surname").send_keys("KKKKK")
        # driver.find_element_by_id("datepicker").click()
        # driver.find_element_by_link_text("1").click()
        driver.find_element_by_xpath("//input[@id='datepicker']").clear()
        driver.find_element_by_xpath("//input[@id='datepicker']").send_keys("9-03-1997")
        driver.find_element_by_xpath("//input[@id='datepicker']").send_keys(Keys.ENTER)
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').click()
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').clear()
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys("KKKKK@gmail.com")
        driver.find_element_by_xpath("//input[@id='id_mobile']").click()
        driver.find_element_by_xpath("//input[@id='id_mobile']").clear()
        driver.find_element_by_xpath("//input[@id='id_mobile']").send_keys("0155155114")
        driver.find_element(By.CSS_SELECTOR, 'button#confirmPatientForm').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//button[@id="proceedCreatePatient"]').click()
        driver.find_element(By.XPATH, "//a[@id='ok_button']").click()


        for td in driver.find_elements_by_xpath('//table[@id="DataTables_Table_0"]'):
            if 'KKKKK' in td.text:
                print('OK')

        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Alert Summary'])[1]/following::span[3]").click()
        driver.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

