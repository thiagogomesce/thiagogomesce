import requests

print('Enter city name:')
cidade = input()

# link do open_weather: https://openweathermap.org/

API_key = "52a28be7172a7c69587521ff141516c1"

unidade = "metric"
linguagem = "pt_br"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&units={unidade}&lang={linguagem}&appid={API_key}"

requisicao = requests.get(link)
requisicao_dic = requisicao.json()
descricao = requisicao_dic['weather'][0]['description']
temperatura = requisicao_dic['main']['temp']
umidade = requisicao_dic['main']['humidity']
city = requisicao_dic['name']
print("clima:",descricao, "| temperatura:",f"{temperatura}ºC"," | humidade", f"{umidade}%" , " | cidade: ",city)
