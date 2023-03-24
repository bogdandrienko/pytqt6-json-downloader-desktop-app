import datetime
import json
import os
import shutil
import requests


def start(url: str, headers: dict):
    try:
        shutil.rmtree("image_or_json_downloader/data")
    except Exception as error:
        pass
    os.mkdir("image_or_json_downloader/data")

    response = requests.get(url=url, headers=headers).json()

    if not isinstance(response, list):
        response = [response]

    for index, json_obj in enumerate(response, 1):
        with open(
                f'image_or_json_downloader/data/data{json_obj["id"]}_{datetime.datetime.now().strftime("%H_%M")}.json',
                'w') as file:
            json.dump(json_obj, file)


if __name__ == '__main__':
    pass
