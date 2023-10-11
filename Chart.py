import requests
import matplotlib.pyplot as plt


with open('api_key.txt', 'r') as f:
    api_key = f.read().strip()

company = "AAPL"
years = 15  


url = f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}&apikey={api_key}"
response = requests.get(url)


if response.ok:
    data = response.json()

    
    if len(data) >= years:
        revenues = [entry['revenue'] for entry in data[-years:]]  
        profits = [entry['grossProfit'] for entry in data[-years:]]  

       
        years_labels = [str(2023 - i) for i in range(years)]

        plt.plot(revenues, label='Revenues')
        plt.plot(profits, label='Profits')
        plt.xlabel('Year')
        plt.ylabel('Amount')
        plt.title(f'Income Statement for {company}')
        plt.xticks(range(years), labels=years_labels)  
        plt.legend()
        plt.show()
    else:
        print(f"Not enough data available for {years} years.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")



