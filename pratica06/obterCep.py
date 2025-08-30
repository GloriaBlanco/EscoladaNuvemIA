"""
Desenvolva um programa que consulte informações de endereço
 a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP.
 O programa deve exibir o logradouro, bairro, cidade e estado 
 correspondentes ao CEP consultado.

 get - recupera dados de um servidor
 post - envia dados para serem processados por um servidor
 put - atualiza dados existentes no servidor
 delete - remove dados no servidor
  
"""

import requests
print("---------  Busca CEP ----------")

def obtercep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        # dados = response.json()['results'][0]
        dados = response.json()
        logradourocep = f"{dados['logradouro']}"
        complementocep = dados['complemento']
        bairro = dados['bairro']
        localidade = dados['localidade']
        uf = dados['uf']
        estado = dados['estado']
        regiao = dados['regiao']
        return f"\nLogradouro: {logradourocep}\nComplemento: {complementocep}\nBairro: {bairro}\nLocalidade: {localidade}\nUF: {uf}\nEstado: {estado}\nRegião: {regiao}"
    except  requests.RequestExcepption as erro:
        return f"Erro ao obter cep: {erro}"
    
cepconsultar= input("Digite o cep que deseja consultar: ")
dadoscep = obtercep(cepconsultar)
print(f"\nCep: {cepconsultar} {dadoscep}\n")