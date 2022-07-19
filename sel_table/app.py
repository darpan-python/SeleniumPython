from core.sel import test1_get_row_col_info_


def main():

    path = r'//*[@id="TAB6"]/tbody/tr'
    url = r"https://itwebtutorials.mga.edu/html/chp8/table-colors-and-backgrounds.aspx"
    tag = "id"
    tag_value = "CELL9"
    col_index = 2

    test1_get_row_col_info_(url, path, tag, tag_value, col_index)


if __name__ == "__main__":
    main()