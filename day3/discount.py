from datetime import date, datetime, timedelta

today = date.today()
print("Dzisiaj jest:", today)  # Dzisiaj jest: 2026-02-18
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2026-02-18 10:55:47.696139

print(today.day)  # 18
print(today.year)  # 2026

formated_date = datetime.now().strftime("%d/%m/%Y")
print("Dzisiejsza data:", formated_date)  # Dzisiejsza data: 18/02/2026
print(type(formated_date))  # <class 'str'>

# 11:16 11:16:56
# 11:16 am
formated_time = datetime.now().strftime("%H:%M:%S")
print("Aktualna godzina:", formated_time)  # Aktualna godzina: 11:21:06
print(type(formated_time))  # <class 'str'>

# Aktualna godzina: 11:20:14
# <class 'str'>

formated_time_12h = datetime.now().strftime("%I:%M:%S %p")
print("Aktualna godzina (12h):", formated_time_12h)  # Aktualna godzina (12h): 11:21:06 AM
print(type(formated_time_12h))  # <class 'str'>
# Aktualna godzina (12h): 11:21:06 AM
# <class 'str'>

object_data = datetime.now().strptime("18/02/2026", "%d/%m/%Y")
print(object_data)
print(type(object_data))
# 2026-02-18 00:00:00
# <class 'datetime.datetime'>

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print("Jutrzejsza data:", tomorrow)  # Jutrzejsza data: 2026-02-19
