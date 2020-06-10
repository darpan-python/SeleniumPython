import logging
import pandas as pd
from Unit_Test.Main_Test import Main_Test
#import sys
#sys.path.insert(1, r"C:\Users\rishabh bhardwaj\PycharmProjects\Selenium\Unit_Test")
# from Main_Test import Main_Test
logger = logging.getLogger(__name__)


class prac_test(Main_Test):
    def __init__(self, url, path, selection):

        self.excelPath = path
        self.ab = ""
        self.url = url
        super().__init__()
        # time.sleep(3)
        self.ExcelParser(selection)
        pass

    def RunSuccessfull(self, test_result):
        self.text = test_result
        pass

    def ExecutionFailed(self):
        self.text = "ExecutionFailed"
        pass

    def ExcelParser(self, selection):
        try:

            # Test Case Counter
            test_result = {}
            test_result['pass_test'] = 0
            test_result['fail_test'] = 0
            test_result['pass'] = 0
            test_result['fail'] = 0

            data = pd.read_excel(self.excelPath)
            df = pd.DataFrame(data, columns=['Locator', 'FindBy', 'ElementName', 'Input'])
            df = df.fillna('')
            # iterate through each row and select
            # 'Name' and 'Stream' column respectively.

            for ind in df.index:

                if selection == '1':
                    # time.sleep(3)
                    # self.getLocator("Name", "email", "link")

                    test_result = self.getLocator(df['Locator'][ind], df['FindBy'][ind], df['ElementName'][ind],
                                                  df['Input'][ind], test_result, selection)
                    pass

                else:
                    # time.sleep(3)
                    test_result = self.getLocator(df['Locator'][ind], df['FindBy'][ind], df['ElementName'][ind],
                                                  df['Input'][ind], test_result)
                    pass
            # time.sleep(3)

            result = "Pass TestCase: " + str(test_result['pass']) + '\n' + "Fail TestCases: " + str(test_result['fail'])
            logger.info(result)

            self.RunSuccessfull(test_result)

        except Exception as e:
            logger.critical(e)
            self.ExecutionFailed()

    # def __init__(self, url, path, selection):
    #
    #     self.excelPath = path
    #     self.ab = ""
    #     self.url = url
    #     super().__init__()
    #     # time.sleep(5)
    #     self.ExcelParser(selection)
    #     pass
    #
    # def RunSuccessfull(self, test_result):
    #     self.text = test_result
    #     pass
    #
    # def ExecutionFailed(self):
    #     self.text = "ExecutionFailed"
    #     pass
    #
    # def ExcelParser(self, selection):
    #     try:
    #         #Test Case Counter
    #         test_result = {}
    #         test_result['pass_test'] = 0
    #         test_result['fail_test'] = 0
    #         test_result['pass'] = 0
    #         test_result['fail'] = 0
    #
    #         data = pd.read_excel(self.excelPath)
    #         df = pd.DataFrame(data, columns=['Locator', 'FindBy', 'ElementName', 'Input'])
    #
    #         # iterate through each row and select
    #         # 'Name' and 'Stream' column respectively.
    #         for ind in df.index:
    #             if selection == '1':
    #                 # self.getLocator("Name", "email", "link")
    #                 test_result = self.getLocator(df['Locator'][ind], df['FindBy'][ind], df['ElementName'][ind], df['Input'][ind],
    #                                  test_result, selection)
    #
    #                 pass
    #             else:
    #                 test_result = self.getLocator(df['Locator'][ind], df['FindBy'][ind], df['ElementName'][ind], df['Input'][ind], test_result)
    #                 pass
    #         # time.sleep(3)
    #         result = "Pass TestCase: " + str(test_result['pass']) + '\n' + "Fail TestCases: " + str(test_result['fail'])
    #         logger.info(result)
    #         self.RunSuccessfull(test_result)
    #
    #     except Exception as e:
    #         logger.critical(e)
    #         self.ExecutionFailed()
