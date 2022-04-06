# Копипаст туда, куда нельзя вставить
Бывает такое, что необходимо вставить текст туда, где не предусмотрена возможность вставки текста.  
Не работает Ctrl+v и нет других способов вставить скопированный текст.  
Например это может быть удаленный рабочий стол Windows или терминал сервера, расшареный в браузере или просто Вы подключились к консоли KVM.

Я попал в такую ситуацию, мне надо было ввести длинный текст в консоль KVM и я сделал себе утилиту, которая позволят это сделать.
Она умеет вставлять любой однострочный текс в такие "неудобные места".  

##### Функционал:
* Умеет передевать как текст так и символы первода строки и табуляции:
    * tab \t
    * перевод строки \n
* Можно вторым параметром задать время в секундах, чтоб успеть поставить курсор в нужное место. По умолчанию 15 секунд.
* Третьим параметром можно задать время таймаута между ввода каждой буквы (по умочанию 0 секунд)
* Четвертым параметром можно задать время таймаута после табуляции и перевода строки (по умолчанию 0.1 секунда)
##### Принцип работы:
Эмуляция нажатия клавиш.

##### Установка:
```
cd /tmp/ 
git clone https://github.com/viktor-gorinskiy/prints.git
sudo cp /tmp/prints/main.py /usr/bin/prints
sudo chmod +x /usr/bin/prints
````
##### Установка зависимостей
```
pip install keyboard
pip install wheel
pip install pynput
pip install progress
```
##### Или так:
```
pip install -r requirements.txt
```
#### Использование:
```prints "текст который надо вставить" 10```
Где 10 это задержка в секундах, чтоб успеть установить курсор в нужное место.
#### И анимация как это работает
![demonstration animation](static/demonstration.gif)

#### P.S.
Я не успел сделать каких-либо проверок и обработку исключений. Мне так понравилась этот инструмент, что я спешу поделиться им с Вами, позже я конечно всё сделаю как следует. 
