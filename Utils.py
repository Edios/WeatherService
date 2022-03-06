def parse_date(date:str):
    parsed_date=date.split("-")
    return parsed_date[0],parsed_date[1],parsed_date[2]