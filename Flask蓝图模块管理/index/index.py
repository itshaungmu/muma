from . import usr_index

@usr_index.route('/')
def index():
    return 'index'