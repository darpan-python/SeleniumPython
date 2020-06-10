# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
# import configparser
# import time
# import logging
# from datetime import datetime
# from numpy.ma.core import get_data
#
# logger = logging.getLogger(__name__)
# from _overlapped import NULL
#
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException


from selenium.webdriver.support.ui import Select
from selenium import webdriver
import configparser
import time
import logging
from datetime import datetime
from numpy.ma.core import get_data

logger = logging.getLogger(__name__)
from _overlapped import NULL
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Main_Test():
    ab = configparser.ConfigParser()
    dir = os.path.dirname(__file__)
    ab.read(os.path.join(dir, "conf.properties"))
    # logging.basicConfig(filename='qwertyui.log',level=logging.DEBUG , format='%(asctime)s:%(levelname)s:%(message)s')
    logging.basicConfig(filename='qwertyui.log', level=int(ab.get("setting", "level_trace")),
                        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    print = logger.info
    print("*********************************************************")

    def __init__(self):
        self.getDriver(self.url)
        get_data(self.driver)
        self.getConfig()
        pass

    def getDriver(self, url):
        # var_2={}

        self.driver = webdriver.Chrome.get("setting", "chrome_loc")
        self.driver.maximize_window()

        self.driver.wait = WebDriverWait(self.driver, 5)
        try:
            self.driver.get(url)
            time.sleep(3)
        except Exception as e:
            logger.critical(e)

        return self.driver
        pass

    def getConfig(self):
        self.ab = configparser.ConfigParser()
        self.ab.read(os.path.join(dir, "conf.properties"))
        # self.url = self.ab.get("setting","url")
        pass

    def getElementByName(self, Locator, elementName, KeynameLink, test_result, Scrn_shot=NULL, Title=NULL):
        def getElementForTextBox(elementName, KeynameLink, Scrn_shot):
            try:
                w = self.driver.wait.until(EC.presence_of_element_located((By.NAME, elementName)))
                if isinstance(KeynameLink, datetime.datetime):
                    w.send_keys(str(KeynameLink.strftime('%m/%d/%y')))
                else:
                    w.send_keys(KeynameLink)
                pass
                if (Scrn_shot != NULL):
                    t = time.localtime()
                    current_time = time.strftime("%H-%M-%S", t)
                    w = self.driver.get_screenshot_as_file(
                        self.ab.get("setting", "flocation") + "ScreenShot_" + str(current_time) + ".png")
                    test_result['pass_test'] = test_result['pass_test'] + 1
            except Exception as e:
                test_result['fail_test'] = test_result['fail_test'] + 1
                logger.critical(e)
                pass
            pass

        def ElementForButtonName(elementName):
            try:
                w = self.driver.wait.until(EC.presence_of_element_located((By.NAME, elementName)))
                w.click()
                test_result['pass_test'] = test_result['pass_test'] + 1
            except Exception as e:
                test_result['fail_test'] = test_result['fail_test'] + 1
                logger.critical(e)

        def ElementForDropDownName(elementName, KeynameLink, Scrn_shot):
            try:
                w = Select(self.driver.wait.until(EC.presence_of_element_located((By.NAME, elementName))))
                w.select_by_index(KeynameLink)
                if (Scrn_shot != NULL):
                    t = time.localtime()
                    current_time = time.strftime("%H-%M-%S", t)
                    w = self.driver.get_screenshot_as_file(
                        self.ab.get("setting", "flocation") + "ScreenShot_" + str(current_time) + ".png")
                    test_result['pass_test'] = test_result['pass_test'] + 1

            except Exception as e:
                test_result['fail_test'] = test_result['fail_test'] + 1
                logger.critical(e)

        if Locator == "Text":
            getElementForTextBox(elementName, KeynameLink, Scrn_shot)
            pass
        elif Locator == "Button":
            ElementForButtonName(elementName)
            pass

        elif Title == " ":
            print(" ")
            pass

        elif Locator == "Drop Down":
            ElementForDropDownName(elementName, KeynameLink, Scrn_shot)
            pass

        elif Title == " ":
            print("")
            pass

        elif Locator == "Back":
            self.driver.back()
            self.driver.refresh();
            pass

        elif Locator == "Break":
            if test_result['fail_test'] > 0:
                test_result['fail'] = test_result['fail'] + 1
                pass

            else:
                test_result['pass'] = test_result['pass'] + 1
                pass

            test_result['fail_test'] = 0
            test_result['pass_test'] = 0

            pass

        elif Locator == "URL":
            self.driver.get(elementName)
        pass

    def getElementById(self, Locator, elementName, KeynameLink, test_result, Scrn_shot=NULL, Title=NULL):

        def getElementForTextBoxId(elementName, KeynameLink, Scrn_shot):
            try:
                w = self.driver.wait.until(EC.presence_of_element_located((By.ID, elementName)))
                if isinstance(KeynameLink, datetime.datetime):
                    w.send_keys(str(KeynameLink.strftime('%m/%d/%y')))
                    pass
                else:
                    w.send_keys(KeynameLink)
                    pass
                if (Scrn_shot != NULL):
                    if Locator == "Snap$":
                        t = time.localtime()
                        current_time = time.strftime("%H-%M-%S", t)
                        w = self.driver.get_screenshot_as_file(
                            self.ab.get("setting", "flocation") + "ScreenShot_" + str(current_time) + ".png")
                        test_result['pass_test'] = test_result['pass_test'] + 1
            except Exception as e:
                test_result['fail_test'] = test_result['fail_test'] + 1
                logger.critical(e)
                pass

        def ElementForButtonId(elementName):
            try:
                w = self.driver.wait.until(EC.presence_of_element_located((By.ID, elementName)))
                w.click()
                test_result['pass_test'] = test_result['pass_test'] + 1
            except Exception as e:
                test_result['fail_test'] = test_result['fail_test'] + 1
                logger.critical(e)

        def ElementForDropDownId(elementName, KeynameLink, Scrn_shot):
            try:
                w = Select(self.driver.wait.until(EC.presence_of_element_located((By.ID, elementName))))
                w.select_by_visible_text(KeynameLink)
                if (Scrn_shot != NULL):
                    t = time.localtime()
                    current_time = time.strftime("%H-%M-%S", t)
                    w = self.driver.get_screenshot_as_file(
                        self.ab.get("setting", "flocation") + "ScreenShot_" + str(current_time) + ".png")
                    test_result['pass_test'] = test_result['pass_test'] + 1
            except Exception as e:
                test_result['fail_test'] = test_result['fail_test'] + 1
                logger.critical(e)

        if Locator == "Text":
            getElementForTextBoxId(elementName, KeynameLink, Scrn_shot)
            pass
        elif Locator == "Button":
            ElementForButtonId(elementName)
            pass

        elif Title == " ":
            print(" ")
            pass

        elif Locator == "Drop Down":
            ElementForDropDownId(elementName, KeynameLink, Scrn_shot)
            pass

        elif Locator == "Back":
            self.driver.back()
            self.driver.refresh()
            pass

        # elif (Scrn_shot != NULL):
        #     if Locator == "Snap$":
        #         t = time.localtime()
        #         current_time = time.strftime("%H-%M-%S", t)
        #         w = self.driver.get_screenshot_as_file(
        #             self.ab.get(“setting”, “flocation”) + “ScreenShot_” + str(current_time) + “.png”)

        elif Locator == "Break":
            if test_result['fail_test'] > 0:
                test_result['fail'] = test_result['fail'] + 1
                pass
            else:
                test_result['pass'] = test_result['pass'] + 1
                pass
            test_result['fail_test'] = 0
            test_result['pass_test'] = 0
            pass

        elif Locator == "URL":
            self.driver.get(elementName)
        pass

    def getElementByXpath(self, Locator, elementName, KeynameLink, test_result, Scrn_shot=NULL, Title=NULL):

        def getElementForTextBoxXpath(elementName, KeynameLink, Scrn_shot):
            try:
                w = self.driver.wait.until(EC.presence_of_element_located((By.XPATH, elementName)))
                if isinstance(KeynameLink, datetime.datetime):
                    w.send_keys(str(KeynameLink.strftime('%m/%d/%y')))
                else:
                    w.send_keys(KeynameLink)
                if (Scrn_shot != NULL):
                    t = time.localtime()
                    current_time = time.strftime("%H-%M-%S", t)
                    w = self.driver.get_screenshot_as_file(
                        self.ab.get("setting", "flocation") + "ScreenShot_" + str(current_time) + ".png")
                    test_result['pass_test'] = test_result['pass_test'] + 1
            except Exception as e:
                test_result['fail_test'] = test_result['fail_test'] + 1
                logger.critical(e)
                pass

        def ElementForButtonXpath(elementName):
            try:
                w = self.driver.wait.until(EC.presence_of_element_located((By.XPATH, elementName)))
                w.click()
                test_result['pass_test'] = test_result['pass_test'] + 1
            except Exception as e:
                test_result['fail_test'] = test_result['fail_test'] + 1
                logger.critical(e)

        def ElementForDropDownXpath(elementName, KeynameLink, Scrn_shot):
            try:
                w = Select(self.driver.wait.until(EC.presence_of_element_located((By.XPATH, elementName))))
                w.select_by_visible_text(KeynameLink)
                if (Scrn_shot != NULL):
                    t = time.localtime()
                    current_time = time.strftime("%H-%M-%S", t)
                    w = self.driver.get_screenshot_as_file(
                        self.ab.get("setting", "flocation") + "ScreenShot_" + str(current_time) + ".png")
                    test_result['pass_test'] = test_result['pass_test'] + 1
            except Exception as e:
                test_result['fail_test'] = test_result['fail_test'] + 1
                logger.critical(e)

        if Locator == "Text":
            getElementForTextBoxXpath(elementName, KeynameLink, Scrn_shot)
            pass
        elif Locator == "Button":
            ElementForButtonXpath(elementName)
            pass
        elif Locator == "Drop Down":
            ElementForDropDownXpath(elementName, KeynameLink, Scrn_shot)
            pass

        elif Title == " ":
            print(" ")
            pass

        elif Locator == "Back":
            self.driver.back()
            self.driver.refresh()
            pass

        elif Locator == "Break":
            if test_result['fail_test'] > 0:
                test_result['fail'] = test_result['fail'] + 1
                pass

            else:
                test_result['pass'] = test_result['pass'] + 1
                pass
            test_result['fail_test'] = 0
            test_result['pass_test'] = 0
            pass

        elif Locator == "URL":
            self.driver.get(elementName)
        pass

    pass

    def getLocator(self, Locator, Findby, elementName, KeynameLink, test_result, Scrn_shot=NULL, Title=NULL):
        if Findby == "Name":
            self.getElementByName(Locator, elementName, KeynameLink, test_result, Scrn_shot, Title)
            return test_result
            pass
        elif Findby == "Id":
            self.getElementById(Locator, elementName, KeynameLink, test_result, Scrn_shot, Title)
            return test_result
            pass
        elif Findby == "Xpath":
            self.getElementByXpath(Locator, elementName, KeynameLink, test_result, Scrn_shot, Title)
            return test_result
            pass
        elif Findby == "":
            self.getElementById(Locator, elementName, KeynameLink, test_result, Scrn_shot, Title)
            return test_result

        logger.info('Run Successfully')

    # def getElementByName(self, Locator, elementName, KeynameLink, test_result,fs):
    #     def getElementForTextBox(elementName, KeynameLink, fs):
    #         try:
    #             w = self.driver.wait.until(EC.presence_of_element_located((By.NAME, (elementName))))
    #             w.send_keys(KeynameLink)
    #             if (fs != NULL):
    #                 t = time.localtime()
    #                 current_time = time.strftime("%H-%M-%S", t)
    #                 w = self.driver.get_screenshot_as_file(
    #                     self.ab.get("setting", "flocation") + "ScreenShot_" + str(current_time) + ".png")
    #                 test_result['pass_test'] = test_result['pass_test'] + 1
    #         except Exception as e:
    #             test_result['fail_test'] = test_result['fail_test'] + 1
    #             logger.critical(e)
    #             pass
    #         pass
    #
    #     def ElementForButtonName(elementName):
    #         try:
    #             w = self.driver.wait.until(EC.presence_of_element_located((By.NAME, (elementName))))
    #             w.click()
    #             test_result['pass_test'] = test_result['pass_test'] + 1
    #         except Exception as e:
    #             logger.critical(e)
    #             test_result['fail_test'] = test_result['fail_test'] + 1
    #
    #     if Locator == "Text":
    #         getElementForTextBox(elementName, KeynameLink, fs)
    #         pass
    #     elif Locator == "Button":
    #         ElementForButtonName(elementName)
    #         pass
    #     elif Locator == "Break":
    #         if test_result['fail_test'] > 0 :
    #             test_result['fail'] = test_result['fail'] + 1
    #             pass
    #         else :
    #             test_result['pass'] = test_result['pass'] + 1
    #             pass
    #
    #         test_result['fail_test'] = 0
    #         test_result['pass_test'] = 0
    #
    #         self.driver.back()
    #         self.driver.refresh()
    #         pass
    #
    #     elif Locator == "URL":
    #         self.driver.get(elementName)
    #     pass
    #
    # def getElementById(self, Locator, elementName, KeynameLink, fs):
    #
    #     def getElementForTextBoxId(elementName, KeynameLink, fs):
    #         try:
    #             w = self.driver.wait.until(EC.presence_of_element_located((By.ID, (elementName))))
    #
    #             if isinstance(KeynameLink, datetime):
    #                 dt = KeynameLink.strftime('%m/%d/%Y')
    #                 # dtv=str(dt).split(' ')[0]
    #                 w.send_keys(str(dt))
    #
    #             else:
    #                 w.send_keys(KeynameLink)
    #                 pass
    #             if (fs != NULL):
    #                 t = time.localtime()
    #                 current_time = time.strftime("%H-%M-%S", t)
    #                 w = self.driver.get_screenshot_as_file(
    #                     self.ab.get("setting", "flocation") + "ScreenShot_" + str(current_time) + ".png")
    #         except Exception as e:
    #             logger.critical(e)
    #             pass
    #
    #     def ElementForButtonId(elementName):
    #         try:
    #             w = self.driver.wait.until(EC.presence_of_element_located((By.ID, (elementName))))
    #             w.click()
    #         except Exception as e:
    #             logger.critical(e)
    #
    #     def ElementForDropDownId(elementName, KeynameLink, fs):
    #         try:
    #             w = Select(self.driver.wait.until(EC.presence_of_element_located((By.ID, (elementName)))))
    #             w.select_by_index(KeynameLink)
    #             if (fs != NULL):
    #                 t = time.localtime()
    #                 current_time = time.strftime("%H-%M-%S", t)
    #                 w = self.driver.get_screenshot_as_file(
    #                     self.ab.get("setting", "flocation") + "ScreenShot_" + str(current_time) + ".png")
    #
    #         except Exception as e:
    #             logger.critical(e)
    #
    #     if Locator == "Text":
    #         getElementForTextBoxId(elementName, KeynameLink, fs)
    #
    #         pass
    #     elif Locator == "Button":
    #         ElementForButtonId(elementName)
    #         pass
    #     elif Locator == "Drop Down":
    #         ElementForDropDownId(elementName, KeynameLink, fs)
    #         pass
    #     elif Locator == "Break":
    #         pass
    #
    # def getLocator(self, Locator, Findby, elementName, KeynameLink, test_result,fs=NULL ):
    #     if Findby == "Name":
    #         self.getElementByName(Locator, elementName, KeynameLink, test_result,fs)
    #         return test_result
    #         pass
    #     elif Findby == "Id":
    #         self.getElementById(Locator, elementName, KeynameLink,fs)
    #         return test_result
    #         pass
    #     else:
    #         self.getElementByName(Locator, elementName, KeynameLink, test_result, fs)
    #         return test_result
    #
    #     logger.info('Run Successfully')
    #     # logger.info.append("Pass TestCase: " +str(test2.text['pass']) + '\n' + "Fail TestCases: "+ str(test2.text['fail']))