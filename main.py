import webbrowser
import pyautogui
import time
import pytesseract
import cv2
import csv
import random
from itertools import groupby

# Парсинг данных с https://wordstat.yandex.ru
# Данный код не подходит для полноценного парсинга с wordstat.yandex из-за очень медленной работы
# Но хорошо демонстрирует использование распознование текста (OpenCV) в парсинге


#num это цифра из цикла для списка
def skrin(num, x):
    sek = random.randrange(5, 10)
    r = f'https://wordstat.yandex.ru/#!/?words={x[num]}'
    webbrowser.open(r, new=0)
    name = f'img/1.jpg'
    time.sleep(sek)
    sc = pyautogui.screenshot(name)

def opencv():
    img = cv2.imread('img/1.jpg')
    print(img.shape)
    hei, wid = 600, 590
    x, y = 310, 350
    img = img[y:y + hei, x:x + wid]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("img/55.jpg", img)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\tesseract.exe'
    img = cv2.imread('img/55.jpg')
    string = pytesseract.image_to_string(img, lang='rus')
    print(string)
    with open('book.txt', 'w') as f:
        f.write(string)

def job():
    x = []
    with open('book.txt', 'r') as f:
        for i in f:
            i = i.replace('\n', '')
            x.append(i)

    new_x = []
    for i in x:
        new = i.split(' ')
        word = ''
        number = ''
        s = []
        for a in new:
            if a.isdigit() == True:
                number += str(a) + ' '

            else:
                word += a + ' '
        s.append(word)
        s.append(number)
        new_x.append(s)

    for i in new_x:
        with open('data.csv', 'a', encoding='cp1251') as f:
            writer = csv.writer(f)
            writer.writerow(i)

def test():
    spis = []
    new_spis = []
    with open('book.txt', 'r') as e:
        for i in e:
            spis.append(i)
        g = []
        for i in spis:
            x = i.replace('\n', '')
            new_spis.append(x)
        for i in new_spis:
            if i not in g:
                g.append(i)

    words = []
    num = []
    for i in g:
        print(type(i))
        if i.isdigit() == False:
            num.append(i)
        else:
            words.append(i)


    for i in range(1):
        d = {}
        d[words[i]] = num[i]
        with open('data.csv', 'a', encoding='cp1251') as f:
            writer = csv.writer(f)
            writer.writerow(d)






if __name__ == '__main__':
    x = ['знак']
    for i in range(len(x)):
        skrin(i, x)
        opencv()
        test()


