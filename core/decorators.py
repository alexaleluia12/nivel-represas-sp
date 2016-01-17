import re

def sanity(val, vtype, interval=None):
    if type(str) != type(vtype):#
        raise TypeError("{0} invalid type 'try: int or str'"\
                       .format(repr(vtype)))
    valBool = type(val) == vtype
    if interval == None:
        return valBool
    assert type(val) == type(interval[0]) == type(interval[1]), "the \
                                    interval need to be the same type"

    intervalBool = val >= interval[0] and val <= interval[1]
    return valBool and intervalBool


def check(func):
    valueKeys = [
        'Guarapiranga', 
        'Rio Claro',
        'Cantareira',
        'Rio Grande', 
        'Cotia',
        'Alto Tiete'
    ]
    valueKeys = set(valueKeys)
    def decored(*args, **kargs):
        data = args[-1]
        match = re.search(r'^(\d{4})-(\d{2})-(\d{2})$', data['date'])
        if match:
            groups = match.groups()
            month = sanity(int(groups[1]), int, (1, 12))
            day = sanity(int(groups[2]), int, (1, 31))
            originKeys = set(data['json'].keys())
            keysEqual = valueKeys == originKeys
            if month and day:
                if keysEqual:
                    values = data['json'].values()
                    for i in values:
                        floatMatch = re.search(r'\d+\.\d+', i)
                        if not floatMatch:
                            raise TypeError("The value shold be a string \
                                             that can be convert to float")
                    return func(*args, **kargs)
                else:
                    raise TypeError("Invalid keys for json -> {0}".\
                                    format(originKeys))
            else:
                raise TypeError("Invalid month or day")
        else:
            raise TypeError("Invalid date format -> {0}".format(data['date']))
    return decored
