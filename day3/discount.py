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
