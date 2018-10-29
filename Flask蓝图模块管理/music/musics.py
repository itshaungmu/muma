from . import music_blue

@music_blue.route('/music')
def music():
    return "music"