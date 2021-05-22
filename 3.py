import schedule
from bs4 import BeautifulSoup
import requests
import schedule

website_req = requests.get("https://www.kufar.by/listings?ot=1&query=%D0%BF%D0%BE%D0%B4%D0%B3%D1%83%D0%B7%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%B4%D0%BB%D1%8F%20%D0%B2%D0%B7%D1%80%D0%BE%D1%81%D0%BB%D1%8B%D1%85&rgn=7", timeout=5)
website_cont = BeautifulSoup(website_req.content, "html.parser")
b = website_cont.find(class_ = "kf-YFgn-56bed").find(class_ = "kf-hkFb-ef933").find('span').text
# b - это переменная в которой при первом заходе бота на куфар должны сохраняться данные самого последнего выставленного объявления (например: b = "Сегодня в 16:15")

def crawling(website_link, link_class):

    website_link = "https://www.kufar.by/listings?ot=1&query=%D0%BF%D0%BE%D0%B4%D0%B3%D1%83%D0%B7%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%B4%D0%BB%D1%8F%20%D0%B2%D0%B7%D1%80%D0%BE%D1%81%D0%BB%D1%8B%D1%85&rgn=7"
    link_class = "kf-YFgn-56bed"

    website_request = requests.get(website_link, timeout=5)
    website_content = BeautifulSoup(website_request.content, "html.parser")

    a = website_content.find(class_ = link_class).find(class_ = "kf-hkFb-ef933").find('span').text
    # a - это переменная в которой при повторном заходе бота на куфар должны сохраняться данные самого последнего выставленного объявления (например: a = "Сегодня в 16:15")
        

    if (b == a):
        # если с последнего захода бота на куфар нового объявления нет - оставь всё как и было
           return a
    else:
        # если что-то поменялось - отправь уведомление в телеграм
        send_message()
    


def send_message(chat_id, a):
    '''
    Takes the chat id of a telegram bot and the text that was  crawled from the
    website and sends it to the bot
    Args: chat_id = string; chat id of the telegram bot, 
          text = string; crawled text to be sent
    Returns: None
    '''
    chat_id = 475686192
    parameters = {"chat_id": chat_id, "text": a}
    message = requests.post("https://api.telegram.org/bot1679714653:AAGVCqz_yHJzQ8Giwt5Gmubdp-HZ8S7LgY4/sendMessage?chat_id=475686192&text=новоеобновление!", data=a)


# bot and chat ids
bot = "1679714653:AAGVCqz_yHJzQ8Giwt5Gmubdp-HZ8S7LgY4"
chat_id = "475686192"

# schedule crawler:
schedule.every(30).seconds.do(crawling, "https://www.kufar.by/listings?ot=1&query=%D0%BF%D0%BE%D0%B4%D0%B3%D1%83%D0%B7%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%B4%D0%BB%D1%8F%20%D0%B2%D0%B7%D1%80%D0%BE%D1%81%D0%BB%D1%8B%D1%85&rgn=7","kf-SeyN-89cf1")
# run script infinitely
while True:
    schedule.run_pending()





