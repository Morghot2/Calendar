# def menu():
#     global is_working
#     print("""
#         1. Add event
#         2. Print in text format
#         3. Print in vCalendar format
#         4. Exit
#     """)
#     action = input("Choose an option: ")
#     if action == "1":
#         add_event()
#     elif action == "2" and calendar:
#         list_calendar(calendar)
#     elif action == "3" and calendar:
#         if len(calendar):
#             print('true')
#         else:
#             print('false')
#         print(len(calendar))
#         list_vCalendar(calendar)
#     elif action == "4":  
#         is_working = False
