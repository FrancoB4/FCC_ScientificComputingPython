def add_time(start, duration, day=''):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
    start_time = start.split()[0]
    start_hour = int(start_time.split(':')[0])
    start_mins = int(start_time.split(':')[1])
    hours_dur = int(duration.split(':')[0])
    mins_dur = int(duration.split(':')[1])
    extra_hours = 0
    extra_days = 0

    end_mins = start_mins + mins_dur
    if end_mins >= 60:
        end_mins -= 60 * (end_mins // 60)
        extra_hours += 1
    end_mins = f'0{end_mins}' if end_mins < 10 else end_mins

    am = True if start.split()[1] == 'AM' else False

    end_hour = start_hour + 12 + hours_dur + extra_hours if not am else start_hour + hours_dur + extra_hours

    if end_hour > 24:
        extra_days += 1 * ((end_hour + 12) // 24)
        end_hour = end_hour % 12

    end_range = 'AM' if end_hour < 12 else 'PM'

    if end_range == 'PM':
        end_hour -= 12

    if end_hour == 0:
        end_hour = 12

    if day == '':
        if extra_days == 0:
            new_time = f'{end_hour}:{end_mins} {end_range}'
        elif extra_days == 1:
            new_time = f'{end_hour}:{end_mins} {end_range} (next day)'
        else:
            new_time = f'{end_hour}:{end_mins} {end_range} ({extra_days} days later)'
    else:
        start_day = days.index(day.capitalize())
        end_day = days[(start_day + extra_days) % 7]

        if extra_days == 0:
            new_time = f'{end_hour}:{end_mins} {end_range}, {day.capitalize()}'
        elif extra_days == 1:
            new_time = f'{end_hour}:{end_mins} {end_range}, {end_day} (next day)'
        else:
            new_time = f'{end_hour}:{end_mins} {end_range}, {end_day} ({extra_days} days later)'

    return new_time
