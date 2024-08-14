import re

data = 'かなり昔のRX-7で東京駅まで送ってもらい、成田空港からBoening787で高松空港まで行き、帰りはN799系で岡山から戻りました。'

print(re.findall(r'[a-zA-Z-]+\d+', data))

print(re.findall(r'\D+\d+', data))
