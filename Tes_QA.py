import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSimpleTest():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_python(self):
        self.driver.get("https://www.python.org")
        print()
        print()
        print(self.driver.title)
        # search_bar = self.driver.find_element(By.NAME, value="q")
        search_bar = self.driver.find_element(By.ID, value="id-search-field")
        search_bar.clear()
        search_bar.send_keys("getting started")
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)

        self.driver.find_element(By.LINK_TEXT, value="PyTraining: Getting Started with API Design using Python").click()
        exact_date = self.driver.find_element(By.CLASS_NAME, value="single-date").text
        assert exact_date == "16 Sept."

        time.sleep(3)

    def test_QAsite(self):
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, value="//button[@aria-label='Consent']").click()
        firstName = "Tamas"
        lastName = "Hak-Kovacs"
        userEmail = "tamas.hak.kovacs@gmail.com"
        gender = "Male"
        userNumber = "0123456789"
        dateOfBirthInput = "26 Dec 1970"
        currentAddress1 = "Petofi ut 61"
        currentAddress2 = "Bukkzserc"

        self.driver.find_element(By.ID, value="firstName").send_keys(firstName)
        self.driver.find_element(By.ID, value="lastName").send_keys(lastName)
        self.driver.find_element(By.ID, value="userEmail").send_keys(userEmail)
        self.driver.find_element(By.XPATH, value=f"// label[normalize-space()='{gender}']").click()
        self.driver.find_element(By.ID, value="userNumber").send_keys(userNumber)
        # self.driver.find_element(By.ID, value="dateOfBirthInput").send_keys(Keys.LEFT_CONTROL, "A")

        self.driver.find_element(By.ID, value="dateOfBirthInput").click()

        select_element_year = self.driver.find_element(By.XPATH,
                                                       value="//select[@class='react-datepicker__year-select']")
        select_year = Select(select_element_year)
        select_year.select_by_visible_text("1970")

        select_element_month = self.driver.find_element(By.XPATH,
                                                        value="//select[@class='react-datepicker__month-select']")
        select_month = Select(select_element_month)
        select_month.select_by_visible_text("December")

        self.driver.find_element(By.CLASS_NAME, value="react-datepicker__day--026").click()

        self.driver.find_element(By.ID, value="subjectsInput").send_keys("ma")
        self.driver.find_element(By.ID, value="subjectsInput").send_keys(Keys.ENTER)

        elements_sport = (WebDriverWait(self.driver, timeout=5).
                          until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Sports']"))))

        elements_sport.click()

        # self.driver.find_element(By.XPATH, value="//label[@for='hobbies-checkbox-1']").click()
        # self.driver.find_element(By.XPATH, value="//label[@for='hobbies-checkbox-2']").click()

        self.driver.find_element(By.TAG_NAME, value="html").send_keys(Keys.END)

        self.driver.find_element(By.ID, value="currentAddress").send_keys(
            f"{currentAddress1}{Keys.ENTER}{currentAddress2}")

        self.driver.find_element(By.TAG_NAME, value="html").send_keys(Keys.END)

        # self.driver.find_element(By.XPATH, value="//div[contains(text(),'Select State')]").click()
        # self.driver.find_element(By.ID, value="react-select-3-input").send_keys("NCR")
        # self.driver.find_element(By.ID, value="react-select-3-input").send_keys(Keys.ENTER)

        self.driver.find_element(By.TAG_NAME, value="html").send_keys(Keys.END)

        # self.driver.find_element(By.XPATH, value="//div[contains(text(),'Select City')]").click()
        # self.driver.find_element(By.ID, value="react-select-4-input").send_keys("Delhi")
        # self.driver.find_element(By.ID, value="react-select-4-input").send_keys(Keys.ENTER)

        self.driver.find_element(By.ID, value="submit").click()

        time.sleep(2)

        name_element = self.driver.find_element(By.XPATH,
                                                value="//td[normalize-space()='Student Name']//following-sibling::td")
        assert name_element.text == f"{firstName} {lastName}"

        email_element = self.driver.find_element(By.XPATH,
                                                 value="//td[normalize-space()='Student Email']//following-sibling::td")
        assert email_element.text == f"{userEmail}"

        time.sleep(3)

    # Navigate to Simpe Form Demo. In "Two Input Fields" enter value A and B and click the "Get Total" button. Validate that the answer is correct.
    # Does your test works even when you enter very large numbers?

    def test_twofieldandoutput(self):
        self.driver.get(
            "https://web.archive.org/web/20180926132852/http://www.seleniumeasy.com/test/basic-first-form-demo.html")
        self.driver.maximize_window()

        test_value1 = 11111111111111
        test_value2 = 22222222222222
        output = test_value2 + test_value1

        self.driver.find_element(By.ID, value="sum1").send_keys(test_value1)
        self.driver.find_element(By.ID, value="sum2").send_keys(test_value2)
        self.driver.find_element(By.XPATH, value="//button[normalize-space()='Get Total']").click()

        result_element = self.driver.find_element(By.ID, value="displayvalue")
        result_text = result_element.text
        result = int(result_text)

        assert result == output

        time.sleep(5)

        print("\nResult:", result)
        print("Expected Output:", output)


