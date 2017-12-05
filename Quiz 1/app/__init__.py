import sqlite3
from tweepy import Stream, OAuthHandler, API, Cursor
from tweepy.streaming import StreamListener

cke = "06d4YJf565idwZYQdagl70RPd"
cse = "1jykFa8vBTVO8igaT3vjNkxEzommJO5tXicWmPpbjuaUkXiCX6"
ato = "910233826558976000-99Is9Sd5BA44EDyupwhLqALLJdFXyPv"
ase = "glFnj4Vj6d7Vs4nZaS7FH6Dn1bNI6wrOSxdC4ZAOO1lD0"

auth = OAuthHandler(cke, cse)
auth.set_access_token(ato, ase)

db = sqlite3.connect('data/Quiz1')
cursor = db.cursor()

cursor.execute('''CREATE TABLE Tweets(Usuario TEXT, Tweet TEXT)''')
db.commit()

class TLListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return(True)

    def on_error(self, status_code):
        print(status_code)

twStream = Stream(auth, TLListener())
twStream.filter(track=["#PrayForVegas"])