import requests
import json
import pandas as pd

num_of_rows = 100 # maximum : 100
Type = 'json'
# use your key
service_key = "Use Your Key"

base_url = f"https://apis.data.go.kr/1471000/DURPrdlstInfoService02/getDurPrdlstInfoList2?serviceKey={service_key}&pageNo=1&type={Type}"
response = requests.get(base_url)
data = response
total_counts = data["body"]['totalCount']

Iter = total_counts // num_of_rows + 1
result = pd.DataFrame()

for i in range(1,Iter+1):
    print(i)
    url = f"https://apis.data.go.kr/1471000/DURPrdlstInfoService02/getDurPrdlstInfoList2?serviceKey={service_key}&pageNo={i}&numOfRows={num_of_rows}&type={Type}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data["body"]["items"])
        result = pd.concat([result, df], axis=0)
    else : 
        print(f"{i}th page not loaded")
        continue

result.to_csv("DUR_preduct_info.csv", index=False)