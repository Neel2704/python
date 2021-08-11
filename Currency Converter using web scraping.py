import requests
from tabulate import tabulate
from bs4 import BeautifulSoup

#CREATING OF TABLE OF FEW CURRENCIES
print('\nSome Common Currencies')
table=[{'Australia Dollar','AUD'},{'Euro','EUR'},{'Japan Yen','JPY'},{'USA Dolllar','USD'},{'Afghanistan Afghani','AFN'},{'Canada Dollar','CAD'},{'India Rupee','INR'},{'Indonesia Rupiah','IDR'},{'Malaysia Ringgit','MYR'},{'Nepal Rupee','NPR'}]
head=['CURRENCY','ABBREVATION']
print(tabulate(table,headers=head,tablefmt="grid"))
#TAKING VALUES FROM USER
currency=input('\nPLEASE ENTER THE CURRENCY YOU WANT TO CONVERT(abbreviation): ').upper()
To=input('\nTHE CURRENCY YOU WANT TO COVERT {} TO(abbreviation): '.format(currency)).upper()
amount=input('\nPLEASE ENTER THE AMOUNT: ')
#FETCHING DATA
data=requests.get('https://www.xe.com/currencyconverter/convert/?Amount={}&From={}&To={}'.format(amount,currency,To))
#CHECKING IF THE CONNECTION WAS SUCCESSFUL OR NOT
if data.status_code>=400:
    print('Please Check the data you have entered')
    raise Exception('SOMETHING WENT WRONG')
#FINDIND THE VALUES AND THEN DISPLAYING THEM
content=BeautifulSoup(data.content,'lxml')
finder=content.find('p',class_='result__BigRate-sc-1bsijpp-1 iGrAod')
print(f'\nThe value of {amount} {currency} is {finder.get_text()}')

