data = [
    {'Имя': 'Маша', 'Фамилия': 'Иванова', 'Возраст': 27},
    {'Имя': 'Маша', 'Фамилия': 'Иванова', 'Возраст': 28},
    {'Имя': 'Маша', 'Фамилия': 'Петрова', 'Возраст': 27},
    {'Имя': 'Маша', 'Фамилия': 'Cидорова', 'Возраст': 27}
]

keys = ['Имя', 'Возраст']

unig = []
result = []
for _dict in data:
    for key in _dict:
        if key in keys:
            if _dict[key] not in unig:
                unig.append(_dict[key])
                result.append(_dict)

print(result)
