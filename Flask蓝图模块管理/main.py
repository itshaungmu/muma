from flask import Flask
from index import usr_index
from maps import map_blue
from music import music_blue
app=Flask(__name__)
app.register_blueprint(usr_index)
app.register_blueprint(map_blue)
app.register_blueprint(music_blue)

if __name__ == '__main__':
    print(app.url_map)
    app.run()