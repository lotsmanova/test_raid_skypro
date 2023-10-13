### Тестовое задание для бекендера

Шаг 1

Создайте базу данных и модельку FrameworkModel к ней с полями

```python
pk
name
language
```

Шаг 2

Наполните базу записями

```python
pk  name      language
-------------------------
1   React     Javascript
2   Vue       Javascript
3   FastApi   Python
4   Laravel   PHP
5   Spring    Java
```

Шаг 3

Напишите вьюшки

`GET /frameworks` – вернет список в формате 

```python
[{"pk": 1, "name": "React", ....}]
```

`GET /frameworks/<language>` – вернет полные данные фреймворка:

```python
[
  {"pk": 1, "name": "React", "language": "Javascript"},
  {"pk": 2, "name": "Vue", "language": "Javascript"},
]
```

Настройте CORS 

Разместите на сервере [render.com](http://render.com) или [railway.app](http://railway.app) или https://www.pythonanywhere.com/

###