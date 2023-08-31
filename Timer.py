import time

def countdown(number_of_seconds):
    while number_of_seconds:
        m, s = divmod(number_of_seconds, 60)
        minute_second_format = '{:02d}:{:02d}'.format(m, s)
        print(minute_second_format, end='/r')
        time.sleep(1)
        number_of_seconds -= 1

    print("Countdown finished.")

input = int(input("Input number of seconds to countdown:"))
countdown(input)