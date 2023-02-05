from bs4 import BeautifulSoup
import requests
url = 'https://kutsehariduskeskus.ee/ru/api/contact';
r = requests.get(url).text;
pars = BeautifulSoup(r, 'lxml').findAll('div', class_='object-inner');
d = 0;
for i in pars:
    j = 0;
    elem = i.findAll('p');
    if(elem[1].text.find('Õpetaja') != -1 or elem[1].text.find('Grupijuhendaja') != -1 or elem[1].text.find('Juhtõpetaja') != -1 or elem[1].text.find('Keemia laborant') != -1):
        mail = 0;
        try:
            mail = elem[1].find('a').text;
        except:
            mail = 'Почта отсутствует';
            
        print(elem[0].text, mail);
        d += 1;
        
print('Всего преподавателей:', d);