
# def list_calendar(calendar):
#     for event in calendar:
#         date = ''
#         time = ''
#         for key in event:

#             if key == "Title":
#                 print(f'{key}: {event[key]}')
#             if key == 'Date':
#                 date = event[key]
#             if key == "Time":
#                 time = event[key] 
#         print(f'Date: {date}, {time}')

# def list_in_vCalendar_format(calendar):
#     for event in calendar:
#         final_date = ''
#         final_time = ''
#         for element in event:
#             if element == 'Date':
#                 splitted_date = event[element].split(".")[::-1]
#                 final_date = '.'.join(splitted_date).replace('.', '')
#             if element == 'Time':
#                 splitted_time = event[element].split(".")[::-1]
#                 final_time = '.'.join(splitted_time).replace(':', '')
#             if element == "Title":
#                 final_title = event[element]
#         print("BEGIN:VEVENT")
#         print(f'DTSTART:{final_date}T{final_time}00')
#         print(f'DTEND:{final_date}T{final_time}00')
#         print(f'SUMMARY:{final_title}')
#         print("END:VEVENT")
# # list_in_vCalendar_format(calendar)
# def list_vCalendar(calendar):
#     print("BEGIN:VCALENDAR")
#     print("VERSION:2.0")
#     print("BEGIN:VTIMEZONE")
#     print("TZID:Europe/Warsaw")
#     print("X-LIC-LOCATION:Europe/Warsaw")
#     list_in_vCalendar_format(calendar)
#     print("END:VCALENDAR")
    








