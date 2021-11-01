import json
from json import decoder
# import ipfsapi
import ipfshttpclient
import os
from pathlib import Path
import logging


def upload_image_to_ipfs(image_data,art_name,description):
        try:
            client = ipfshttpclient.connect()
            file_data = client.add(image_data)
            print(file_data)
            file_hash = file_data['Hash']
            print(file_hash)
            image_url = f"localhost:8080/ipfs/{file_hash}"
            values = {"art_name":art_name,
                       "description":description,
                       "image": image_url}
            json_data = json.dumps(values) 
            return json_data       
        except Exception as e:
            print("Error in the uploadin image to ipfs")
            return str(e)

def upload_json_to_ipfs(image_data,art_name,description):
    try:
        json_data = upload_image_to_ipfs(image_data,art_name,description)
        client = ipfshttpclient.connect()
        json_value = client.add(json_data)
        json_hash = json_value['Hash']
        logging.info("uploading json on the ipfs")
        print("uploaded json ipfs hash",json_hash)
        return f"localhost/ipfs/{json_hash}"
    except Exception as e:
        return str(e)


def access_local_file():
    basepath = 'media/'
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            print(entry)


def filepath():    
    # List all files in directory using pathlib
    basepath = Path('media/')
    files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
    for item in files_in_basepath:
        return item
        print(item.name)
# def delete_file():
    