from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import multiprocessing
import xlwt



def get_pages():
    global url_list
    global data_list
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_path = "E:\\Program Files\\chormedriver\\chromedriver76.exe"
    dr = webdriver.Chrome(executable_path=chrome_path ,options=chrome_options)
    url = "http://index.baidu.com/v2/main/index.html#/trend/B7%E5%B1%B1?words=%B7%E5%B1%B1"
    dr.get(url)
    y = input("[!]Y坐标：")
    first_x = int(input("[!]起始x坐标："))
    fianl_x = int(input("[!]结尾X坐标："))
    move = multiprocessing.Process(target=move_mouse, args=(y,first_x ,fianl_x)) #移动鼠标
    if_ready = input("[#]Are you ready? [Enter]")
    move.start()
    have_item = []
    while True:
        try:
            date_html = dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div[1]/div[1]/div/div[2]/div[1]")
            number_html = dr.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/div[1]/div[3]/div[1]/div[1]/div/div[2]/div[2]/div[2]")
            if not len(have_item) == 365:#抓取的总天数
                if date_html.text and number_html.text:
                    date1 = date_html.text.split(' ')
                    date = date1[0]
                    number = number_html.text.replace('  ','')
                    data_dict = {date:number}
                    if date not in have_item:
                        print(str(data_dict))
                        have_item.append(date)
                        data_list.append(data_dict)
            else:
                print("[*]正在保存中...")
                save_data(data_list)
                xxx = input("[#]直接关闭即可")
        except:
            pass  

def save_data(data_list):     
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('雷锋纪念馆百度指数')
    line_num = 0
    for dict_line in data_list: #提取字典{：}
        date_list = dict_line.keys()
        for date in date_list:
            number = dict_line[date]
            sheet.write(line_num,0,date)
            sheet.write(line_num,1,number)
            line_num = line_num + 1
    wbk.save('已完成.xls')
    print("[!]数据已导出至同目录下")


def move_mouse(y,first_x ,fianl_x):
    for x in range(first_x,fianl_x+1):
        pyautogui.moveTo(x,y)
        time.sleep(0.05)
    time.sleep(5)
    


if __name__ == "__main__":
    global data_list
    data_list = []
    get_pages()
