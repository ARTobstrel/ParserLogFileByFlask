import re
from collections import Counter

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # открываем файл где ключ словаря name='file', имя name указываем в шаблоне html в теге input
        f = request.files['file'].read()

        # файл откроется с типом byte, его необходимо превести к строковому типу
        txt = str(f.decode('utf-8'))

        # создаем переменную с регулярным выражением и производим обработку нашего файла и результат записываем в переменную ips
        pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ips = re.findall(pattern, txt)

        # создаем переменную в которую заносим результат обработки counter`а, который подсчитывает количество повторяющихся имен(ip адресов)
        result = Counter(ips).most_common(6)

        ban = []
        for key, value in result:
            if value > 2:
                ban.append({'ip': key, 'frequency': value})

        return render_template('index.html', ips=ban)

    return render_template('index.html')


# def main():
#     with open('log.txt') as f:
#         logfile = f.read()
#         pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
#         ips = re.findall(pattern, logfile)
#
#         result = Counter(ips).most_common(6)
#
#         for k, v in result:
#             k = str(k)
#             v = str(v)
#
#             print('{} - {}'.format(k, v))


if __name__ == '__main__':
    app.run(debug=True)
