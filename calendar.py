
def list_calendar(calendar):
    # listing_strategy.begin()
    for event in calendar:
        for key in event:
            # date_time = ''
            if key == 'title':
                print(f'{key}: {event[key]}')
                # print(key,event[key])
            elif key == 'date':
                # print(event[key])
                date = event[key]
            else:
                # key = 'time':
                time = event[key]
        print(f'Date: {date}, {time}')

def list_in_vCalendar_format(calendar):
    for event in calendar:
        for element in event:
            if element == 'Date':
                splitted_date = event[element].split(".")[::-1]
                final_date = '.'.join(splitted_date).replace('.', '')
            if element == 'Time':
                splitted_time = event[element].split(".")[::-1]
                final_time = '.'.join(splitted_time).replace(':', '')
            if element == "Title":
                final_title = event[element]
        print("BEGIN:VEVENT")
        print(f'DTSTART:{final_date}T{final_time}00')
        print(f'DTEND:{final_date}T{final_time}00')
        print(f'SUMMARY:{final_title}')
        print("END:VEVENT")
# list_in_vCalendar_format(calendar)
def list_vCalendar(calendar):
    print("BEGIN:VCALENDAR")
    print("VERSION:2.0")
    print("BEGIN:VTIMEZONE")
    print("TZID:Europe/Warsaw")
    print("X-LIC-LOCATION:Europe/Warsaw")
    list_in_vCalendar_format(calendar)
    print("END:VCALENDAR")
    








