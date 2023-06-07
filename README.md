# messageToSpeach_py

![messageToSpeach_py](https://imgur.com/OvMZBs9.png "screenshot")​  
> Основные команды бота

___

![messageToSpeach_py](https://imgur.com/OvMZBs9.png "screenshot")​  
> Обработка ошибок при неправильном вводе

___

Бот дает расшифровку текста сообщения и преобразует его в голосовое сообщение, написаный на python


### Установка

```sh
# Клонируйте этот репозиторий (или просто скачайте и разархивируйте zip)
$ git clone https://github.com/rawreflect/messageToSpeach_py.git

# Перейти в каталог
$ cd messageToSpeach_py

# Установите зависимости (если «pip» отсутствует, попробуйте использовать «pip3»)
$ sudo pip install -r requirements.txt
```

### Запуск

```sh
$ python messageToSpeach.py
```

Для изменения языка нужно изменить один параметр:

```py
def converter_text(text: str) -> BytesIO:
    ...
    audio = gTTS(text=text, lang="ru") -> audio = gTTS(text=text, lang="en")
    ...
```
