import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimiter=",") -> list[dict]:
    with open(filename, "r") as source:  # TODO реализовать конвертер из csv в json
        input_data = [line.rstrip().split(delimiter) for line in source]
        names_list = input_data[0]
        json_data = [{names_list[column]: input_data[row][column] for column in range(len(names_list))} for row in
                     range(1, len(input_data))]
        return json_data


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
