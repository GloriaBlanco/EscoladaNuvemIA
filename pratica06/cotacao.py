"""
Crie um programa que consulte a cotação atual de uma
 moeda estrangeira em relação ao Real Brasileiro (BRL).
 O usuário deve informar o código da moeda desejada 
 (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
 máximo e mínimo da cotação, além da data e hora da última 
 atualização. Utilize a API da AwesomeAPI para obter 
os dados de cotação.

"""

import requests
print("------------  Cotação moeda ----------")

def cotacao(moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        # dados = response.json()['results'][0]
        dados = response.json()
        valorconversao = float(dados[f'{moeda}BRL']['high'])
        return valorconversao
    
    except  requests.RequestExcepption as erro:
        return f"Erro ao obter cep: {erro}"
    
try:

    valorreais = float(input("Digite o valor que deseja converter em R$ "))
    moedaconverter = input("Para qual moeda deseja converter USD, EUR, GBP, JPY : ")
    moedaconverter = moedaconverter.upper()
    valormoeda = cotacao(moedaconverter)
    valorfinal = valorreais/valormoeda

    print(f"\nO valor de R$ {valorreais:.2f} = {moedaconverter} {valorfinal:.2f}\nValor da Cotaçao = {moedaconverter} {valormoeda:.2F}")

except ValueError:
    print(f"\nValor inválido!! digite um valor numérico")
