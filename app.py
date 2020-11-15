import bs4 
import requests

url = "https://jadwalsholat.pkpu.or.id/?id=216"
content = requests.get(url)

response = bs4.BeautifulSoup(content.text,"html.parser")
data = response.find_all('tr', 'table_highlight')
data = data[0]
# print(data)

sholat = {}
i = 0
for d in data :
    if i == 1 :
        sholat['Imsyak'] = d.get_text()
    elif i == 2 :
        sholat['Subuh'] = d.get_text()    
    elif i == 3 :
        sholat['Terbit'] = d.get_text()    
    elif i == 4 :
        sholat ['Dhuha'] = d.get_text()
    elif i == 5 :
        sholat ['Dzuhur'] = d.get_text()          
    elif i == 6 :
        sholat ['Azhar'] = d.get_text()
    elif i == 7 :
        sholat ['Maghrib'] = d.get_text()        
    elif i == 8 :
        sholat ['Isya'] = d.get_text()
    i+=1    

print('------------------------------')
print('Waktu Sholat (Raha) Hari ini ')
print('-----------------------------')
print('\n'.join("{}: {}".format(k, v) for k, v in sholat.items()))


