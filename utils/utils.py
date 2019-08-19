import json


def import_file(path):
    try:
        json_file = open(path)
        return json.load(json_file)['cells_list']

    except:
        print('Tem um problema com o arquivo JSON.')
        return None