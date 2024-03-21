from datetime import date
import os
import requests
from PIL import Image, ImageFont, ImageDraw
from dotenv import load_dotenv

load_dotenv()



class Match():

   def __init__(self):

      #date format = str(YYYY-MM-DD)
      self.dateToday = str(date.today())

      self.dateToday = "2024-03-22"

      apiKey = os.getenv('CRICAPI_KEY')

      baseLink = "https://api.cricapi.com/v1"
      seriesID = "76ae85e2-88e5-4e99-83e4-5f352108aebc"

      headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.52'
      }

      matchLink = f'{baseLink}/series_info?apikey={apiKey}&id={seriesID}'

      r = requests.get(matchLink, headers = headers)

      self.data = r.json()

   def getData(self) -> list:
         
      matchesToday = []

      for fixture in self.data['data']['matchList']:
         if fixture['date'] == self.dateToday:
            matchesToday.append(fixture)

      return matchesToday

   def createBanner(self, pos, data):

      homeTeam = data['teams'][0]
      awayTeam = data['teams'][1]

      img1 = Image.open(f"./Static/Logo/{homeTeam}.jpg")
      img2 = Image.open(f"./Static/Logo/{awayTeam}.jpg") 


      banner = Image.new("RGB", (1024, 512), "black")

      banner.paste(img1, (0, 0))
      banner.paste(img2, (512, 0))

      font = ImageFont.truetype("./Static/Fonts/Roboto-Bold.ttf", 36)

      draw = ImageDraw.Draw(banner)

      draw.text((480, 250), "V", fill = (255, 255, 255), font = font, anchor = "mm")
      draw.text((540, 250), "S", fill = (255, 255, 255), font = font, anchor = "mm")

      banner.save(f"./Static/Banners/Banner_{pos}.png")