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


calendar = []


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










def list_vCalendar(calendar):
    print (
       "BEGIN:VCALENDAR"
       "VERSION:2.0"
       "BEGIN:VTIMEZONE"
       "TZID:Europe/Warsaw"
       "X-LIC-LOCATION:Europe/Warsaw"
       )
    list_in_vCalendar_format(calendar)
    print("END:VCALENDAR")
    
    




calendar = [{
    'Title': "Programowanie",
    'Date': '28.02.2010',
    'Time': '08:00'
    
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
        print(final_title)
                
        print(final_date)
        print(final_time)
        print("BEGIN:VEVENT")
        print(f'DTSTART:{final_date}T{final_time}00')
        print(f'DTSTART:{final_date}T{final_time}00')
        print(f'SUMMARY:{final_title}')
        print("END:VEVENT")

            





# txt = "hello, my name is Peter, I am 26 years old"

# x = txt.split(", ")
# list_in_vCalendar_format(calendar)
# print(x)








   # print(event['title'])
    # print()
    # for key in event:
    #     print(key,': ', event[key])

# listing_strategy.end()
