# version: 1.0 E
from urllib import request, parse, error
from os import remove
link = 'https://www.dropbox.com/s/w5fqdzr7944hchz/cryptor.py?dl=1'
try:
    request.urlopen('https://www.google.com')  # Check connection
    print('Start downloading...')
    try:
        remove('decoder.py')
    except FileNotFoundError:
        pass
    request.urlretrieve(link, 'decoder.py')
    print('Finished download.')
except:
    print("Couldn't download file.\n"
          "Probably your device has no internet connection or link is not correct.\n"
          f"Try to download yourself: {link}\n"
          f"If it doesn't work, here is my github: https://github.com/NBomb1")
