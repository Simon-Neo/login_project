import json

# JSON ----------------------------------------
# def json file import
def file_open(file_address):
        try:
            with open(file_address, 'r') as json_file:
                return json.loads(json_file.read())
        except FileNotFoundError as not_found_error:
            print(not_found_error)
            return -1
        else:
            print("File Open is succeed!")

# def json file save
def file_save(file_address, data):
    with open(file_address, 'w') as json_file:
        json_file.write(json.dumps(data, indent='\t'))
