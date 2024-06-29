import requests
from bs4 import BeautifulSoup

MOVIE_END = "https://www.91mobiles.com/entertainment/best-hindi-bollywood-movies"
SHEET_API_END = "https://api.sheety.co/7dd323f370a1fa5581a130fb15e4a412/movieWatchlist/sheet1"

soup_response = requests.get(MOVIE_END).text
soup = BeautifulSoup(soup_response, "html.parser")

movie_title_span = soup.find_all("span", class_="txt_u_line")
movie_titles = [title.find("a").getText() for title in movie_title_span]

sheet_get_response = requests.get(SHEET_API_END)
my_movies = sheet_get_response.json()
sheet_movie_titles = [item['movieName'] for item in my_movies['sheet1']]

new_movie_titles = [title for title in movie_titles if title not in sheet_movie_titles]



for each_titels in new_movie_titles :
        sheet_param = {
            "sheet1": {
                "movieName": each_titels
            }
        }

        sheet_post_response = requests.post(url=SHEET_API_END, json=sheet_param)

        print(sheet_post_response.json())



