import datetime
x = datetime.datetime.now()


print(x)

print(x.year) #Pega o Ano da data atual
print(x.strftime("%A")) #Pega o nome do dia da semana
x = datetime.datetime(2020, 5, 17, 5, 12, 49) #(Year, Month, Day, Hour, Minute, Second, Microsecond)
print(x)

#strftime can be used with A for weekdays, B for Month's name, d for day of month 0-31, Y for year, W weakday as a number 0-6, 0 is Sunday, H for hour, 




exit()
