import time

def countdown_clock(end_time, update_interval=1):
    elapsed_time = 0
    while elapsed_time < (end_time - time.time()):
        remaining_time = end_time - (time.time() - elapsed_time)
        print(f'Remaining time: {remaining_time:.2f} seconds')
        time.sleep(update_interval)
        elapsed_time += update_interval

def main():
    minutes = int(input('Enter the number of minutes for the countdown: '))
    end_time = time.time() + (60 * minutes)

    countdown_clock(end_time)

if __name__ == '__main__':
    main()   
