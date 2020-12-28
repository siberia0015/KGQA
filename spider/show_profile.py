import codecs
import json
with open('./spider/json/data.json', encoding='utf-8')as f:
    data = json.load(f)
# 要在上面的data.json里添加节点信息才能正常运行
def get_profile(name):
    s=''
    print(name)
    print(data[name])
    for i in data[name]:
        if str(i) != "图片链接":
            st="<dt class = \"basicInfo-item name\" >"+ str(i)+" \
            <dd class = \"basicInfo-item value\" >"+str(data[name][i])+"</dd >"
            s+=st
    return s

