import requests
import re
from pytube import YouTube
import time 
import csv 

# texteUtilisateur = input("Nom de la musique : ")

with open('test.csv', mode='r') as file:
    reader = csv.reader(file)

    for row in reader:

        col1 = row[0]
        texteUtilisateur = (col1.replace(' ', '+')).lower()

        requestUrl = "https://www.youtube.com/results?search_query=" + texteUtilisateur
        response = requests.get(requestUrl).text

        result = re.findall("\/watch\?v=[A-Za-z0-9_]+.+?", response)

        urlYoutube = "https://www.youtube.com" + str(result[0])
        print(urlYoutube)
        yt = YouTube(urlYoutube) 


        #Paramètre pour télécharger dans la section dossier
        project_path = '/home/andraaz/ecole/B3/python-expert/scrapYoutube/musique'

        #Téléchargement de la musique
        while True:
            try:
                stream = yt.streams.filter(only_audio=True).first()
                stream.download(output_path=project_path)
                break
            except:
                time.sleep(1)