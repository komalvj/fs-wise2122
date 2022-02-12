from main import clearConsole
from src import tds


def start_plan(days):
    clearConsole()
    match days:
        case '1':
            print('Plan for 1 day trip:')
            _trip = tds.find_places_by_day(days)
            for _trip_items in _trip:
                print(f"  - {_trip_items.get_place()} : {_trip_items.get_category()}")
        case '2':
            print('Plan for 2 day trip:')
            for d in range(1, int(days)+1):
                print(f" Day {d}")
                _trip = tds.find_places_by_day(str(d))
                for _trip_items in _trip:
                    print(f"  - {_trip_items.get_place()} : {_trip_items.get_category()}")
        case '3':
            print('Plan for 3 day trip:')
            for d in range(1, int(days)+1):
                print(f" Day {d}")
                _trip = tds.find_places_by_day(str(d))
                for _trip_items in _trip:
                    print(f"  - {_trip_items.get_place()} : {_trip_items.get_category()}")
        case '4':
            print('Plan for 4 day trip:')
            for d in range(1, int(days)+1):
                print(f" Day {d}")
                _trip = tds.find_places_by_day(str(d))
                for _trip_items in _trip:
                    print(f"  - {_trip_items.get_place()} : {_trip_items.get_category()}")
        case _:
            print('Oops! We only provide support for 1 to 4 days! Please try again.')
            start_plan(input('\nNumber of days (1 to 4): '))


def modify():
    clearConsole()
    print("Hello Admin, You can modify here!")
