from bus_data import seat_availability, ticket_prices

def check_seat_availability(route, time_slot, bus_type):
    available_seats = seat_availability.get(route, {}).get(time_slot, {}).get(bus_type, 0)
    return available_seats

def update_seat_availability(route, time_slot, bus_type):
    if check_seat_availability(route, time_slot, bus_type) > 0:
        seat_availability[route][time_slot][bus_type] -= 1
        return True
    return False

def calculate_ticket_price(route, bus_type):
    return ticket_prices[route][bus_type]
