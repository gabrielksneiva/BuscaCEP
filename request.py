import requests
import os


cep = input("Digite o CEP: ")
r=requests.get(f'https://viacep.com.br/ws/{cep}/json/')

data = r.json()

print('Dados do CEP em questão, abaixo: \n')
print(f"CEP: {data['cep']}")
print(f"Logradouro: {data['logradouro']}")
print(f"Bairro: {data['bairro']}")
print(f"Localidade: {data['localidade']}")
print(f"UF: {data['uf']}")