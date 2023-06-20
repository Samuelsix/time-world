import datetime

def show_current_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    print("Текущее время:", formatted_time)

# Вызываем функцию для отображения текущего времени
show_current_time()
