import requests

stock_0 = input('What Stock would u like to compare: ')
stock_1 = input('what stock would you like to compare against: ')

URL = 'https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary'
PARAM_0 = {"symbol":stock_0,"region":"US"}
HEADER = {
    'X-RapidAPI-Key': 'fe58562bb5mshe69cd0663f5adefp138695jsn2771629b35f8'
}

response = requests.get(URL, headers=HEADER, params=PARAM_0)

stock_data = response.json()
print(stock_data['earnings']['earningsChart']['quarterly'][0]['actual']['raw'])