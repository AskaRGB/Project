def filter_by_currency(transactions, currency=""):
    for i in transactions:
        if i["operationAmount"]["currency"]["name"] == currency:
            yield i



def transaction_descriptions(list_of_transaction_dictionaries):
    description_operation = []
    for descriptions in list_of_transaction_dictionaries:
        description_operation.append(descriptions.get("description"))
        break
    yield "".join(description_operation)


def card_number_generator(start_value, stop_value):
    for number in range(start_value, stop_value + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[8:12] + " " + f"{number:016d}"[12:16]








