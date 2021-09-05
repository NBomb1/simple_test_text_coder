# version: 1.0 E
# updater version: 0.1
from time import sleep
try:
    from urllib import request, parse, error
except ModuleNotFoundError:
    print('Error, you havent installed "urllib3" for auto-updating.')
    print('For install open CMD, and type: ')
    print('    pip3 install urllib3')
    print('You can continue use this script without auto-updating.')
    question = 1
    while True:
        if question == 1:
            print('Also you can install it here, type "Y" to install')
            question = input('Type "N" to continue without installing: ')
        else:
            print('Error, unsupportable operation.')
            print('To install "urllib3" type "Y" to install')
            question = input('Type "N" to continue without installing: ')
        if question == 'Y' or question == 'y':
            for _ in range(0, 250):
                print()
            from subprocess import call
            call('pip install urllib3')
            sleep(1.5)
            from urllib import request, parse, error
            break
        elif question == 'N' or question == 'n':
            break
from os import remove
link = 'https://www.dropbox.com/s/w5fqdzr7944hchz/cryptor.py?dl=1'
try:
    request.urlopen(r'https://www.google.com')  # Check connection
    print('Start downloading...')
    try:
        remove('coder.py')
    except FileNotFoundError:
        pass
    request.urlretrieve(link, 'coder.py')
    print('Finished download.')
    print('Updated succesfully')
    input('Type Enter to close')
except:
    print("Couldn't download file.")
    print("Probably your device has no internet connection or link is not correct.")
    print(f"Try to download yourself: {link}")
    print(f"If it doesn't work, here is my github: https://github.com/NBomb1")
    input('Type Enter to close')
