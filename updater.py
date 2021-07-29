# version: 1.0 E
from urllib3 import PoolManager, request
from urllib import request as request1, response
print('Start downloading.\n')
with request1.urlopen('https://raw.githubusercontent.com/NBomb1/simple_test_text_coder/main/coder.py') as response, open('coder.txt', 'w') as coder:
    counter = 0
    text1 = response.readlines()
    print(text1)
    while True:
        try:
            text = str(text1[counter])
        except IndexError:
            break
        text = text.replace(text[0], '', 1).replace(text[1], '', 1)
        if len(text.replace(r'\n"', '')) != len(text):
             text = text.rstrip(r'\n"')
        else:
             text = text.replace(r"\n'", '')
        print(text)
        updater.write(f'{text}\n')
        counter += 1
        updater.close()
        print('Download has ended.')
print('Download has ended.')
