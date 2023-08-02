def add_time(start, duration, day = 0):

    #Start time
    row_hours = start.split()[0]
    stage_day = start.split()[1]
    hours = row_hours.split(':')[0]
    minutes = row_hours.split(':')[1]
    #Addition time
    row_add_hours = duration.split()[0]
    add_hours = row_add_hours.split(':')[0]
    add_minutes = row_add_hours.split(':')[1]
    #Results values
    rounding_hours = 0
    rounding_minutes = 0
    total_hours = int(hours) + int(add_hours)
    total_minutes = int(minutes) + int(add_minutes)
    #Rounding time
    if total_minutes > 59:
        rounding_hours = 1
        rounding_minutes = 60

    net_hours = total_hours + rounding_hours
    net_minutes = total_minutes - rounding_minutes
    if len(str(net_minutes)) < 2:
        net_minutes = '0'+ str(net_minutes)
    time_str = str(net_hours) + str(net_minutes)
    day_lapse = ''
    #Day counting
    day_count = 0
    n = 0
    if int(add_hours) >= 24:
        day_count = round((int(add_hours)/24))

    #Clock time correction
    if day_count >= 1:
        net_hours -= (24*(day_count))

    cicles = round(net_hours/12)
    jump = 0
    while cicles > 0:
        if net_hours >= 12 and stage_day == 'AM':
            stage_day = 'PM'
            if net_hours >= 13 and stage_day == 'PM':
                net_hours -= 12
        elif net_hours >= 12 and stage_day == 'PM':
            stage_day = 'AM'
            net_hours -= 12
            jump = 1
        cicles -= 1
    if net_hours == 0:
        net_hours =12
    jump_count = day_count + jump
    g = 0
    if net_hours >= 0 and stage_day == 'AM' and int(add_hours) > 1:
        day_lapse = ' (next day)'
        n = 1
    if jump_count > 1:
        day_lapse = f' ({day_count + n} days later)'
        g = 1


    #Days
    if day == 0:
        current_day = ''
    else:
        day_list = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
        current_day = ""

        in_day = day.lower()
        day_pos = day_list.index(in_day)
        total_days = day_pos+day_count+g

        if total_days > 6:
            week_day_counter = total_days - 6
            day_cicle = -1
            while week_day_counter > 0:
                day_cicle += 1
                week_day_counter -= 1
                if day_cicle > 6:
                    day_cicle = 0
            current_day = day_list[day_cicle]
        else:
            current_day = f'{day_list[total_days]}'
        current_day = f', {current_day.title()}'

    new_time = str(net_hours)+':'+str(net_minutes)+' '+stage_day+''+current_day+''+day_lapse

    return new_time



def main():
    start = '11:50 AM'
    duration = '152:00'
    print(add_time("11:59 PM", "24:05"))

if __name__ == '__main__':
    main()
