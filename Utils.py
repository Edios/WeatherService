from DataModel import Holiday


def parse_date(date:str):
    """

    :param date: String with format YYYY-MM-DD
    :return: year,month,day
    """
    parsed_date=date.split("-")
    return parsed_date[0],parsed_date[1],parsed_date[2]


def get_item_index_in_list(item:str, item_list:list[Holiday])->int:
    """
    Get index of item in list
    Workaround for Tkinker ComboBox
    :param item: str Given Holiday.name
    :param item_list: List of Holiday items
    :return: Index of found item
    """
    for list_item in item_list:
        if list_item.name == item:
            return item_list.index(list_item)