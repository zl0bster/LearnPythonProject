import os
import json

def get_env():
    for envVar, val in os.environ.items():
        print(envVar, val)

# print(os.path)
# print(os.path.dirname('C:\\Program Files\\Python39\\lib\\ntpath.py'))
# print("-" * 15)
# print(os.path.dirname('.\\..'))
# print("-" * 15)
# projPath = os.getcwd()
#
# result = sorted(os.listdir(projPath))
# for n, item in enumerate(result):
#     print(n + 1, item)
# print("-" * 15)
# fileName = os.path.join(projPath, result[6])
# print(fileName)
#
# # separator = "</trkpt>"
# sFile = open(fileName, 'rt')
# data = sFile.readlines()
# sFile.close()
#
# print(len(data))
# for i, line in enumerate(data):
#     print(i+1, line.strip())
#
# print("-" * 15)
# # for i, line in enumerate(data):
# #     jdata = json.dumps(line)
# #     # jdata = json.loads(line)
# #     print(jdata)
# jdata=json.dumps(fileName)
# print(jdata)

get_env()



