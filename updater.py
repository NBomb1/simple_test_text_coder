from urllib3 import PoolManager, request
from urllib import request as request1, response
print(True)
print('Start downloading\n')
with request1.urlopen('https://raw.githubusercontent.com/NBomb1/simple_test_text_coder/main/coder.py') as response, open('coder.py', 'w') as coder:
    counter = 0
    text1 = response.readlines()
    while True:
        try:
            text = str(text1[counter])
        except IndexError:
            break
        text = text.replace(text[0], '').rstrip("'").lstrip("'").replace(text[len(text) - 3], '').rstrip('n')
        coder.write(f'{text}\n')
        counter += 1
print('Download has ended.')
print(False)
