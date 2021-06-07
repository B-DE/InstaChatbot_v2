
import json

jejusi = []
seogwuiposi = []

# 1. 제주시 데이터 리스트 형식 저장

with open('C:\Project\InstaChatbot\Insta_Chatbot_v2\제주시.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip()
        jejusi.append(line)

# 2. 서귀포시 데이터 리스트 형식 저장

with open('C:\Project\InstaChatbot\Insta_Chatbot_v2\서귀포시.txt', encoding = 'UTF8') as f:
    for line in f:
        line = line.strip()
        seogwuiposi.append(line)


# 3. json 형식으로 저장
region = {'jejusi' : jejusi, 'seogwuiposi' : seogwuiposi}

# print(region)

print(json.dumps(region, indent = 4))
# json = json.dump(region, indent = 4)
# print(json)

# print(jejusi)
# print(seogwuiposi)

