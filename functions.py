import re


def filter_query(param: str, data: str) -> list:
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: str) -> list:
    col_number = int(param)
    return list(map(lambda x: x.split(' ')[col_number], data))


def unique_query(data: str, *args: str, **kwargs: str) -> list:
    return list(set(data))


def sort_query(param: str, data: str) -> list:
    reverse = True if param == 'desc' else False
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: str) -> list:
    limit = int(param)
    return list(data)[:limit]


def regex_query(param: str, data: str) -> list:
    regex = re.compile(param)
    return list(filter(lambda x: regex.search(x), data))
