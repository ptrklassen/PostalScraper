from bs4 import BeautifulSoup
import requests
import lxml
import time
import csv

html_text = requests.get('https://www.whitepagescanada.ca/ab/edmonton/T5W/').text
soup = BeautifulSoup(html_text, 'lxml')
csv_file = open('postal_test_T5W.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['postal code', 'name', 'address', 'phone number'])


p_codes = soup.find_all('ul', class_ = 'links-list-alt')
count = 0
for code in p_codes:
  a_code = code.a.text
  count += 1
  print(a_code)
  if count <= 1000:
    new_ask = requests.get("https://www.canadapages.com/wp/ab/edmonton/"+a_code+"/").text
    lander = BeautifulSoup(new_ask, 'lxml')
    contacts = lander.find_all('div', class_ = 'listing-desc')
    for contact in contacts:
      name = contact.div.text
      address = contact.find('div', style = 'color:#333333; ').text
      number = contact.find('div', style = 'color:#0066CC; padding-top: 2px !important;').text
      #print(name)
      #print(address)
      #print(number)
      csv_writer.writerow([a_code, name, address, number])


csv_file.close()    
print(count)