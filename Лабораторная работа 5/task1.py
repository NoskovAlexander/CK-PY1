from pprint import pprint# TODO решить с помощью list comprehension и распечатать его


list_ = [{'bin': bin(d), 'dec': d, 'hex': hex(d), 'oct': oct(d)} for d in range(16)]

pprint(list_)