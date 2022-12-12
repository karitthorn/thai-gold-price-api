import requests
from bs4 import BeautifulSoup

url = "https://www.goldtraders.or.th/" #ขอขอบคุณทางเว็ปไซต์ครับ
pricelist = [] #list ราคาชื้อขาย
day = 0 #วันที่อัพเดต
time = 0 #เวลาที่อัพเดต
web_data = requests.get(url)

#ดึงข้อมูลมาจากเว็ปไซต์ https://www.goldtraders.or.th/
soup = BeautifulSoup(web_data.text,'html.parser')
find_time = soup.find_all("font",{"size":"3"})

for i in find_time:
    i = str(i).split('<font size="3">')[1]
    i = str(i).split('</font>')[0]
    day = i

for i in find_time:
    i = str(i).split('<font size="3">')[1]
    i = str(i).split('</font>')[0]
    time = i
    break;

time = str(time).split('เวลา')[1]
time = time[1:6]

find_price = soup.find_all("font",{"color":"Red"})


for i in find_price:
    pricelist.append(i)


pricelist[0] = str(pricelist[0]).split('<font color="Red">')[1]
pricelist[0] = str(pricelist[0]).split('</font>')[0]
pricelist[1] = str(pricelist[1]).split('<font color="Red">')[1]
pricelist[1] = str(pricelist[1]).split('</font>')[0]
pricelist[2] = str(pricelist[2]).split('<font color="Red">')[1]
pricelist[2] = str(pricelist[2]).split('</font>')[0]
pricelist[3] = str(pricelist[3]).split('<font color="Red">')[1]
pricelist[3] = str(pricelist[3]).split('</font>')[0]

gold_bar_sell = pricelist[0]
gold_bar_buy = pricelist[1]
gold_jewelry_sell = pricelist[2]
gold_jewelry_buy = pricelist[3]

#api part ---------------------------
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "date": day ,
        "time": time,
        "gold_bar_sell":gold_bar_sell,
        "gold_bar_buy":gold_bar_buy,
        'gold_jewelry_sell':gold_jewelry_sell,
        'gold_jewelry_buy':gold_jewelry_buy

        }

@app.get("/date")
async def root():
    return { 
        day
        }

@app.get("/time")
async def root():
    return {
time

        }

@app.get("/gold_bar_sell")
async def root():
    return {
        gold_bar_sell
        }

@app.get("/gold_bar_buy")
async def root():
    return {
        gold_bar_buy
        }

@app.get("/gold_jewelry_sell")
async def root():
    return {
        gold_jewelry_sell
        }

@app.get("/gold_jewelry_buy")
async def root():
    return {
        gold_jewelry_buy
        }