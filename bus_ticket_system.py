from bus_data import bus_schedule
from utils import check_seat_availability, update_seat_availability, calculate_ticket_price

def show_available_routes():
    print("Available Routes:")
    for source, destinations in bus_schedule.items():
        for destination in destinations:
            print(f"{source} -> {destination}")
    print()

def show_schedule(source, destination):
    route = f"{source}-{destination}"
    print(f"Available times for {source} to {destination}:")
    for time_slot in bus_schedule[source][destination]:
        print(f"- {time_slot}: AC Seats: {check_seat_availability(route, time_slot, 'AC')}, Non-AC Seats: {check_seat_availability(route, time_slot, 'Non-AC')}")
    print()

def buy_ticket(source, destination, time_slot, bus_type):
    route = f"{source}-{destination}"
    if update_seat_availability(route, time_slot, bus_type):
        price = calculate_ticket_price(route, bus_type)
        print(f"Ticket booked successfully! Price: {price} for {bus_type} on {time_slot}.")
    else:
        print("Sorry, no seats available for this option.")

def main():
    print("Welcome to the Bus Ticket System")
    while True:
        print("1. View Routes\n2. View Seat Availability\n3. Buy Ticket\n4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            show_available_routes()
        
        elif choice == '2':
            source = input("Enter source city: ")
            destination = input("Enter destination city: ")
            show_schedule(source, destination)
        
        elif choice == '3':
            source = input("Enter source city: ")
            destination = input("Enter destination city: ")
            time_slot = input("Enter time (Morning/Afternoon/Evening): ")
            bus_type = input("Enter bus type (AC/Non-AC): ")
            buy_ticket(source, destination, time_slot, bus_type)
        
        elif choice == '4':
            print("Exiting system.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
