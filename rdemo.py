import json

in_file_path='one_req.json' # Change me!

with open(in_file_path,'r') as in_json_file:

    # Read the file and convert it to a dictionary
    json_obj_list = json.load(in_json_file)
    print(json_obj_list)
    for json_obj in json_obj_list:
        filename=json_obj['api']+'.json'
        print(json.dumps(json_obj))