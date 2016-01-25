import re

valueKeys = [
    'Guarapiranga', 
    'Rio Claro',
    'Cantareira',
    'Rio Grande', 
    'Cotia',
    'Alto Tiete'
]

def is_between(val, interval):
    return val >= interval[0] and val <= interval[1]

comp_regex = re.compile(r'\d+\.\d+')

def check(func):
    
    valueKeysSet = set(valueKeys)# use the set because the order doe't matter
    def decored(*args, **kargs):
        data = args[-1]
        match = re.search(r'^(\d{4})-(\d{2})-(\d{2})$', data['date'])
        if match:
            groups = match.groups()
            month = is_between(int(groups[1]), (1, 12))
            day = is_between(int(groups[2]), (1, 31))
            originKeys = set(data['json'].keys())
            keysEqual = valueKeysSet == originKeys
            if month and day:
                if keysEqual:
                    values = data['json'].values()
                    for i in values:
                        floatMatch = comp_regex.search(i)
                        if not floatMatch:
                            raise TypeError("The value shold be a string \
                                             that can be convert to float")
                    return func(*args, **kargs)# call the functon decored
                else:
                    raise TypeError("Invalid keys for json -> {0}".\
                                    format(originKeys))
            else:
                raise TypeError("Invalid month or day")
        else:
            raise TypeError("Invalid date format -> {0}.\
            \nShould be <year>-<month>-<day>".format(data['date']))
    return decored
