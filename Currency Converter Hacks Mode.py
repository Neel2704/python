import requests
from bs4 import BeautifulSoup

print('\nSome Common Currencies\nAustralia Dollar	AUD\nEuro\t\t	EUR\nJapan Yen	\tJPY\nUSA Dollar\t	USD\nAfghanistan Afghani  	AFN\nAustralia Dollar   	AUD\nCanada Dollar    	CAD\nIndia Rupee\t 	INR\nIndonesia Rupiah\tIDR\nMalaysia Ringgit 	MYR\nNepal Rupee \t	NPR')
currency=input('\nPLEASE ENTER THE CURRENCY YOU WANT TO CONVERT(abbreviation): ').upper()
To=input('\nTHE CURRENCY YOU WANT TO COVERT {} TO(abbreviation): '.format(currency)).upper()
amount=input('\nPLEASE ENTER THE AMOUNT: ')
data=requests.get('https://www.xe.com/currencyconverter/convert/?Amount={}&From={}&To={}'.format(amount,currency,To))
if data.status_code>=400:
    print('Please Check the data you have entered')
    raise Exception('SOMETHING WENT WRONG')
content=BeautifulSoup(data.content,'lxml')
finder=content.find('p',class_='result__BigRate-sc-1bsijpp-1 iGrAod')
print(f'\nThe value of {amount} {currency} is {finder.get_text()}')


