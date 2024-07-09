#3адание:
#Напишите программу, которая создает два потока.
#Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
#Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
#Оба потока должны работать параллельно.

#Примечание:
#Используйте методы: start() для старта потока, join() для заморозки дальнейшей интерпретации, пока процессы не завершаться.
#Для установки интервала в 1 секунду используйте функцию sleep() из модуля time, предварительно импортировав его.
from threading import Thread
from time import sleep



def func_1 (end, start=1, time=1):
    for i in range (start, end+1):
        print(i)
        sleep(time)

def func_2(start1, end1, time=1):
    start2 = ord(start1)
    end2 = ord(end1)

    for i in range(start2, end2+1):
        print(chr(i))
        sleep(time)

thr_fist = Thread(target=func_1, args=(10,))
thr_second = Thread(target=func_2, kwargs=dict(start1='a', end1='j'))


thr_fist.start()
thr_second.start()
thr_fist.join()
thr_second.join()
