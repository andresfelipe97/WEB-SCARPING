import requests
from bs4 import BeautifulSoup


url = "https://listado.mercadolibre.com.co/video-juegos#D[A:video%20juegos]"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    productos = soup.find_all('div', class_='ui-search-result__wrapper')
    
    
    for producto in productos:
        titulo = producto.find('h2', class_ ='poly-box poly-component__title')
        marca = producto.find('span', class_ ='poly-component__brand')
        precio = producto.find('div', class_ = 'poly-content__column')
        if titulo:
            print(titulo.text.strip())
        if marca:
            print(marca.text.strip())
        if precio:
            print(precio.text.strip())
            
else: 
    print("Error al cargar la web, codigo: ", response.status_code)