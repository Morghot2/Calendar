'''
W tym pliku znajdziesz kod odpowiedzialny za wyświetlanie zdarzeń z kalendarza.

Do zmiany zachowania funkcji list_calendar wykorzystaj strategię ListingStrategy.

'''


class ListingStrategy:
    def begin(self):
        pass

    def event(self, title, date, time):
        pass

    def end(self):
        pass





def list_calendar(calendar, listing_strategy):
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
    
list_vCalendar(calendar)







   # print(event['title'])
    # print()
    # for key in event:
    #     print(key,': ', event[key])

# listing_strategy.end()
