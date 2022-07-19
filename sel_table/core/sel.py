from selenium import webdriver
import os

dirname = os.path.dirname(__file__)
filename_driver = os.path.join(dirname, '../drivers/geckodriver')

def extract_results(_list, _tag, _tag_value, _index):
    _result = []
    _dict = {}
    if _list is None or len(_list) < 1:
        return None
    for row in _list:
        col_list = row.find_elements("xpath", "*")
        if col_list[_index].get_attribute(_tag) == _tag_value:
            _dict["name"] = col_list[_index].text
            _result.append(_dict)
    return _result


def test1_get_row_col_info_(url, xpath, _tag, _tag_value, _col_index):
    driver = webdriver.Firefox(executable_path=filename_driver)
    driver.maximize_window()

    driver.get(url)
    rows = driver.find_elements("xpath", xpath)
    x = extract_results(rows, _tag, _tag_value, _col_index)
    print(x)
    # driver.close()


