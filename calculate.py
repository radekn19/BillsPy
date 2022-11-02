listOfDictionaryA = []
listOfDictionaryB = []


def add_records(input_value, input_description, person):
    value = float(input_value)
    description = ''
    if input_description != '':
        description = str(input_description)

    if person == "A":
        dictRecordsA = {'value': value, 'description': description}
        listOfDictionaryA.append(dictRecordsA)
        return sum_values(listOfDictionaryA)
    elif person == "B":
        dictRecordsB = {'value': value, 'description': description}
        listOfDictionaryB.append(dictRecordsB)
        return sum_values(listOfDictionaryB)


def remove_record(value, person):
    if person == "A":
        for lod in listOfDictionaryA:
            if lod.get('value') == float(value[0]) and lod.get('description') == value[1]:
                listOfDictionaryA.remove(lod)
                break
        return sum_values(listOfDictionaryA)
    elif person == "B":
        for lod in listOfDictionaryB:
            if lod.get('value') == float(value[0]) and lod.get('description') == value[1]:
                listOfDictionaryB.remove(lod)
                break
        return sum_values(listOfDictionaryB)


def sum_values(list_of_dict):
    dict_keys = 0
    for dic in list_of_dict:
        dict_keys += dic.get('value')
    return str(dict_keys)
