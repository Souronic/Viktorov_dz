duration = int(input("Введите промежуток времен: "))
sec = duration % 60
minute = duration % 3600 // 60
hour = duration % 86400 // 3600
day = duration // 86400
if duration < 60:
    print(sec, "сек")
elif 0 < duration <= 60:
    print(minute, "мин")
elif 60 < duration <= 3600:
    print(minute, "мин", sec, "сек")
elif 3600 < duration <= 86400:
    print(hour, "час", minute, "мин", sec, "сек")
elif duration >= 86400:
    print(day, "дн", hour, "час", minute, "мин", sec, "сек")
else:
    pass
