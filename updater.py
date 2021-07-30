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
    print('Updated succesfully')
    input('Type Enter to close')
except:
    print("Couldn't download file.")
    print("Probably your device has no internet connection or link is not correct.")
    print(f"Try to download yourself: {link}")
    print(f"If it doesn't work, here is my github: https://github.com/NBomb1")
