import os
import plan

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def print_hi(name):
    clearConsole()
    if name != "Admin":
        print(f'Hi, {name} \n Lets begin with planning your trip to Berlin :)'
              f'\n Please answer the following questions and we might be able to find the perfect itinerary for you!')

        plan.start_plan(input('\nNumber of days (1 to 4): '))
    else:
        plan.modify()


if __name__ == '__main__':
    print_hi(input('Hi there, Please enter your name: '))


