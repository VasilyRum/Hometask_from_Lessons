"""
Есть два списка разной длины, в одном ключи, в другом значения.
Составить словарь. Для ключей, для которых нет значений использовать None в качестве значения.
Значения, для которых нет ключей игнорировать.
"""


def get_dictionary(lst1, lst2):
    """

    :param lst1: list number one
    :param lst2: list number two
    :return: dictionary: keys from list one, values from list two
                        For keys that have no values, use None as the value.
                        Values for which there are no keys to ignore.
    """
    dictionary = {}
    value_list = iter(lst2)
    for i in lst1:
        try:
            value = next(value_list)
            dictionary.update({i: value})
        except StopIteration:
            dictionary.update({i: None})
    return dictionary


print(get_dictionary([1, 2, 3, 4], [5, 8]))
print(get_dictionary([1, 2, 3, 4], [5, 6, 7, 8, 9]))
