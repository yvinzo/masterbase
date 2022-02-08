import requests
#
# Script para hacer requests a un sitio.
# y escribir el resultado a un archivo.
if __name__ == '__main__':
    url = "https://www.google.com.mx"
    response = requests.get(url)

    if response.status_code == 200:
        content = response.content
        file = open('google.html','wb')
        file.write(content)
        file.close()
