
def menu():
    print("""
        1. Add event
        2. Print in text format
        3. Print in vCalendar format
        4. Exit
    """)
    wybor = input("Choose an option: ")

    if wybor == "1":
        print('dupa')
    elif wybor == "2":
        list_calendar(calendar)
    elif wybor == "3":
        list_in_vCalendar_format(calendar)
    elif wybor == "4":
        is_working = False
    else:
        print("Invalid option chosen")