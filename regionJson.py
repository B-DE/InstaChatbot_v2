import json



""""""""""""""""""""""""""""""""""""""""""""""""""""""
# region.txt to list
""""""""""""""""""""""""""""""""""""""""""""""""""""""

def txt_to_list(txt_path, list_name):

    with open(txt_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            list_name.append(line)

    return list_name



""""""""""""""""""""""""""""""""""""""""""""""""""""""
# region.txt to list
""""""""""""""""""""""""""""""""""""""""""""""""""""""

def save_json(json_data, save_path):

    with open(save_path, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)
        ## [document] json 경로 설정시 마지막에 파일 이름까지 넣기!!
        ## 기존 존재 파일이 아니더라도 원하는 이름으로 넣기!!
        ## PermissionError: [Errno 13] Permission denied: 'file_name'





""""""""""""""""""""""""""""""""""""""""""""""""""""""
# execution
""""""""""""""""""""""""""""""""""""""""""""""""""""""

## 제주시 execution
jejusi = []
jejusi_txt = 'C:\Project\InstaChatbot\Insta_Chatbot_v2\제주시.txt'
txt_to_list(jejusi_txt, jejusi)


## 서귀포시 execution
seogwuiposi = []
seogwuiposi_txt = 'C:\Project\InstaChatbot\Insta_Chatbot_v2\서귀포시.txt'
txt_to_list(seogwuiposi_txt, seogwuiposi)


## integrate list for json
region = {'jejusi' : jejusi, 'seogwuiposi' : seogwuiposi}


## save region data as json
json_path = 'C:\Project\InstaChatbot\Insta_Chatbot_v2/region.json'
save_json(region,json_path)

