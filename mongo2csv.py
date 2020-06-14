from pymongo import MongoClient
import os
import json
import time
import logging
import datetime
import requests
import pandas as pd


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

uri = 'mongodb://localhost:27017/'
client = MongoClient(uri)
db = client['2019-nCoV']

collections = {
    'DXYOverall': 'overall',
    'DXYArea': 'area'
}
time_types = ('pubDate', 'createTime', 'modifyTime', 'dataInfoTime', 'crawlTime', 'updateTime')


def dict_parser(document, city_dict=None):
    result = dict()

    try:
        result['continentName'] = document['continentName']
        result['continentEnglishName'] = document['continentEnglishName']
    except KeyError:
        result['continentName'] = None
        result['continentEnglishName'] = None

    result['countryName'] = document['countryName']

    try:
        result['countryEnglishName'] = document['countryEnglishName']
    except KeyError:
        result['countryEnglishName'] = None

    result['provinceName'] = document['provinceName']
    result['provinceEnglishName'] = document.get('provinceEnglishName')
    result['province_zipCode'] = document.get('locationId')
    result['province_confirmedCount'] = document['confirmedCount']
    result['province_suspectedCount'] = document['suspectedCount']
    result['province_curedCount'] = document['curedCount']
    result['province_deadCount'] = document['deadCount']

    result['updateTime'] = datetime.datetime.fromtimestamp(int(document['updateTime'] / 1000))

    if city_dict:
        result['cityName'] = city_dict['cityName']
        result['cityEnglishName'] = city_dict.get('cityEnglishName')
        result['city_zipCode'] = city_dict.get('locationId')
        result['city_confirmedCount'] = city_dict['confirmedCount']
        result['city_suspectedCount'] = city_dict['suspectedCount']
        result['city_curedCount'] = city_dict['curedCount']
        result['city_deadCount'] = city_dict['deadCount']


    return result



class DB:
    def __init__(self):
        self.db = db

    def dump(self, collection):
        return self.db[collection].aggregate(
            pipeline=[
                {
                    '$sort': {
                        'updateTime': -1,
                        'crawlTime': -1
                    }
                }
            ],
            allowDiskUse=True
        )


class Listener:
    def __init__(self):
        self.db = DB()

    def run(self):
        while True:
            self.listener()
            time.sleep(3600)

    def listener(self):
        changed_files = list()
        for collection in collections:
            #打开文件
            json_file = open(
                #路径拼接
                os.path.join(
                    #绝对路径
                    os.path.split(os.path.realpath(__file__))[0], 'json', collection + '.json'),
                'r', encoding='utf-8'
            )
            try:
                static_data = json.load(json_file)
            except (UnicodeDecodeError, FileNotFoundError, json.decoder.JSONDecodeError):
                static_data = None
            json_file.close()
            while True:
                request = requests.get(url='https://lab.isaaclin.cn/nCoV/api/' + collections.get(collection))
                print(request.status_code)
                if request.status_code == 200:
                    current_data = request.json()
                    break
                else:
                    time.sleep(1)
                    continue
            if static_data != current_data:
                self.json_dumper(collection=collection, content=current_data)
                changed_files.append('json/' + collection + '.json')
                cursor = self.db.dump(collection=collection)
                self.csv_dumper(collection=collection, cursor=cursor)
                changed_files.append('csv/' + collection + '.csv')
            logger.info('{collection} checked!'.format(collection=collection))
            # print(os.path.join(
            #     os.path.split(os.path.realpath(__file__))[0], 'json', collection + '.json'))
            # print(os.path.split(os.path.realpath(__file__))[0])

    def json_dumper(self, collection, content=None):
        json_file = open(
            os.path.join(
                os.path.split(
                    os.path.realpath(__file__))[0], 'json', collection + '.json'
            ),
            'w', encoding='utf-8'
        )
        json.dump(content, json_file, ensure_ascii=False, indent=4)
        json_file.close()

    def csv_dumper(self, collection, cursor):
        if collection == 'DXYArea':
            structured_results = list()
            for document in cursor:
                if document.get('cities', None):
                    for city_counter in range(len(document['cities'])):
                        city_dict = document['cities'][city_counter]
                        structured_results.append(dict_parser(document=document, city_dict=city_dict))
                else:
                    structured_results.append(dict_parser(document=document))

            df = pd.DataFrame(structured_results)
            df.to_csv(
                path_or_buf=os.path.join(
                    os.path.split(os.path.realpath(__file__))[0], 'csv', collection + '.csv'),
                index=False, encoding='utf_8_sig', float_format="%i"
            )
        else:
            df = pd.DataFrame(data=cursor)
            for time_type in time_types:
                if time_type in df.columns:
                    df[time_type] = df[time_type].apply(lambda x: datetime.datetime.fromtimestamp(x / 1000) if not pd.isna(x) else '')
            df.to_csv(
                path_or_buf=os.path.join(
                    os.path.split(os.path.realpath(__file__))[0], 'csv', collection + '.csv'),
                index=False, encoding='utf_8_sig', date_format="%Y-%m-%d %H:%M:%S"
            )

if __name__ == '__main__':
    listener = Listener()
    listener.run()

