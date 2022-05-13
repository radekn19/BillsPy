listOfDistinctA = []
listOfDistinctB = []


def add_records(input_value, input_description, person):
    value = float(input_value)
    description = ''
    if input_description != '':
        description = str(input_description)

    if person == "A":
        dictRecordsA = {'value': value, 'description': description}
        listOfDistinctA.append(dictRecordsA)
        return sum_values(listOfDistinctA)
    elif person == "B":
        dictRecordsB = {'value': value, 'description': description}
        listOfDistinctB.append(dictRecordsB)
        return sum_values(listOfDistinctB)


def remove_record(value, person):
    if person == "A":
        listOfDistinctA[:] = [d for d in listOfDistinctA if d.get('value') != value]
        print(sum_values(listOfDistinctA))
        return sum_values(listOfDistinctA)
    elif person == "B":
        listOfDistinctB[:] = [d for d in listOfDistinctB if d.get('value') != value]
        return sum_values(listOfDistinctB)


def sum_values(list_of_dict):
    dict_keys = 0
    for dic in list_of_dict:
        dict_keys += dic.get('value')
    return str(dict_keys)
