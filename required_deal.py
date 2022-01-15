import requests
from bs4 import BeautifulSoup
from time import time, sleep
from win10toast import ToastNotifier

def remove_sym(string):
    price=''
    for s in range(len(string)):
        if s==0:
                   pass
        else:
            if string[s]==',':
                pass
            else:
                   price=price+string[s]
    return int(price)

url=input("url: ")
toast = ToastNotifier()
rnge=int(input("Notify me when the price came under: "))
m=int(input("Execution time (in minutes): "))
while True:
    
    response=requests.get(url)
    page_content=response.text
    soup=BeautifulSoup(page_content,'html.parser')

    p_area=soup.find('div',class_='_25b18c')

    current_price=remove_sym(p_area.find('div',class_='_30jeq3 _16Jk6d').text)
    actual_price=remove_sym(p_area.find('div',class_='_3I9_wc _2p6lqe').text)
    discount=p_area.find('div',class_='_3Ay6Sb _31Dcoz').text
    
    if (current_price<rnge):
        print("Current Price -> "+str(current_price))
        print("Actual Price -> "+str(actual_price))
        print("Discount -> "+str(discount))
        toast.show_toast("Grab Your Product","Current Price -> "+str(current_price),duration=20,icon_path="f_icon.ico")
        break    
    sleep(60*m- time() % 60*m)
        
