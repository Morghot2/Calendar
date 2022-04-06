import string
import re

calendar = [{
    'Title': "Programowanie",
    'Date': '28.02.2010',
    'Time': '08:00'
    
}, 
{
    'Title': "Fizyka",
    'Date': '26.01.2012',
    'Time': '23:15'
}]
is_working = True


def main():
    while is_working:
        menu()

def menu():
    global is_working
    print("""
        1. Add event
        2. Print in text format
        3. Print in vCalendar format
        4. Exit
    """)
    action = input("Choose an option: ")
    if action == "1":
        add_event()
    elif action == "2":
        list_calendar(calendar)
    elif action == "3":
        list_vCalendar(calendar)
    elif action == "4":  
        is_working = False
    else:
        print("Invalid option chosen")
def list_calendar(calendar):
    for event in calendar:
        date = ''
        time = ''
        for key in event:

            if key == "Title":
                print(f'{key}: {event[key]}')
            if key == 'Date':
                date = event[key]
            if key == "Time":
                time = event[key] 
        print(f'Date: {date}, {time}')

def list_in_vCalendar_format(calendar):
    for event in calendar:
        final_date = ''
        final_time = ''
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

def add_event():
    global calendar
    new_event = {}
    event_title = input('Please provide a title: ')
    event_title_set = set(event_title)
    allowed = set(string.ascii_letters + string.digits + '.' + ',' + '-' +' ')
    if event_title_set.issubset(allowed):
        new_event.update({'Title': event_title})
        new_date = input('Please provide a date in DD.MM.YYYY format: ')
        if re.match("^\d\d.\d\d.\d\d\d\d$", new_date):
            new_event.update({'Date': new_date})
            new_time = input('Please provide time in DD.MM.YYYY format: ')
            if re.match('^\d\d:\d\d$', new_time):
                new_event.update({'Time': new_time})
                calendar.append(new_event)
   
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    else:
        print("Invalid input")
    



main()



