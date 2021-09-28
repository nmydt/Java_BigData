import base64
import requests as req
from io import BytesIO

def urltobase64(url):
    # 图片保存在内存
    response = req.get(url)
    # 得到图片的base64编码
    ls_f=base64.b64encode(BytesIO(response.content).read())
    # 将base64编码进行解码
    imgdata=base64.b64decode(ls_f)
    return imgdata



def phtot_base64(address):#将地址为address的图片转为base64字符串
    with open(address,"rb") as photo:
        pb=base64.b64encode(photo.read())
        return str(pb)[2:-1]
target=input("请输入目标markdown文件地址");#例如:"D:\Markdown\Note\Machine learning\误差与噪音.md"(两侧有引号,这也就是你选中md文件,然后shift+右键,复制路径得到的结果)
target=target.replace("\\","/")
target=target[1:-1]
with open(target,"r",encoding="utf-8") as md:#打开目标文件
    transformed=open(target[0:-3]+"_transformed.md","w",encoding="utf-8")#在目标文件同一文件夹地址下产生转换后文件
    for a in md:
        if(re.search("!\[[^]]*\].*",a)):#匹配到图片格式
            address=re.search("(?<=\()[^\)]*",a).group().replace("\\","/")#提取图片地址并且将反斜杠转换为斜杠
            if not(re.match("data",address) or not re.match("http",address)):#确定是本地图片
                temp="![avatar](data:image/png;base64,"+phtot_base64(address)+")"#将图片格式转为base64格式
                a=re.sub("!\[[^]]*\]\([^)]*\)",temp,a)#替换base64格式图片到源字符串
            elif not(re.match("data",address) and re.match("http",address)): #如果是网络图片
                urltobase64()
                
        transformed.write(a)#写入一行
    transformed.close()