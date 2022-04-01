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


    # print(event['title'])
    # print()
    # for key in event:
    #     print(key,': ', event[key])

# listing_strategy.end()
