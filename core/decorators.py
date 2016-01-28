import re


def is_between(val, interval):
    return val >= interval[0] and val <= interval[1]

comp_regex = re.compile(r'\d+\.\d+')

def check(data):
    
    match = re.search(r'^(\d{4})-(\d{2})-(\d{2})$', data['date'])
    if match:
        groups = match.groups()
        month = is_between(int(groups[1]), (1, 12))
        day = is_between(int(groups[2]), (1, 31))
        if month and day:
            values = data['json'].values()
            for i in values:
                floatMatch = comp_regex.search(i)
                if not floatMatch:
                    raise TypeError("The value shold be a string \
                                     that can be convert to float")
            return True
            
        else:
            raise TypeError("Invalid month or day")
    else:
        raise TypeError("Invalid date format -> {0}.\
        \nShould be <year>-<month>-<day>".format(data['date']))
