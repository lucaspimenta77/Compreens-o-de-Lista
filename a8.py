import calendar

ano_bissexto = 2024 
mes = 1  
dias_do_mes = calendar.monthrange(ano_bissexto, mes)[1]  

datas_de_janeiro = [f"{ano_bissexto}-01-{dia:02}" for dia in range(1, dias_do_mes + 1)]
print(datas_de_janeiro)
