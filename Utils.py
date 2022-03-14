def parse_date(date:str):
    """

    :param date: String with format YYYY-MM-DD
    :return: year,month,day
    """
    parsed_date=date.split("-")
    return parsed_date[0],parsed_date[1],parsed_date[2]