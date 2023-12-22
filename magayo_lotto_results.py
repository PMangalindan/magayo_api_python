import requests

api_key = 'jhxYdhfHPKdFyhJteV' #https://www.magayo.com/api-area/account/
game = 'ph_lotto649'           # find your game codes here https://www.magayo.com/lottery-docs/api/supported-games/
draw_date = '2023-12-21'       # this can be blank

BASE_URL = f'https://www.magayo.com/api/results.php?api_key={api_key}&game={game}&draw={draw_date}'

response = requests.get(BASE_URL)
print(response.json())





