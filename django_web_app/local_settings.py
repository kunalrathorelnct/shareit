# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@5&-q%nasnnmb@=@egb9yz^b#l-2)w&_s0ick#=wy3kw36$z($g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['http://easyshare.ml/','*','http://13.127.177.145/']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}