# Bus schedule with time slots
bus_schedule = {
    'Kanpur': {'Lucknow': ['Morning', 'Afternoon', 'Evening'],
               'Jhansi': ['Morning', 'Afternoon', 'Evening'],
               'Mahoba': ['Morning', 'Afternoon', 'Evening'],
               'Banarasi': ['Morning', 'Afternoon', 'Evening'],
               'Farukhabad': ['Morning', 'Afternoon', 'Evening'],
               'Agra': ['Morning', 'Afternoon', 'Evening']},
    'Lucknow': {'Kanpur': ['Morning', 'Afternoon', 'Evening'],
                'Jhansi': ['Morning', 'Afternoon', 'Evening'],
                'Mahoba': ['Morning', 'Afternoon', 'Evening'],
                'Banarasi': ['Morning', 'Afternoon', 'Evening'],
                'Farukhabad': ['Morning', 'Afternoon', 'Evening'],
                'Agra': ['Morning', 'Afternoon', 'Evening']},
    # Add more cities if needed
}

# Bus seat availability (50 seats per bus)
seat_availability = {
    'Kanpur-Lucknow': {'Morning': {'AC': 50, 'Non-AC': 50},
                       'Afternoon': {'AC': 50, 'Non-AC': 50},
                       'Evening': {'AC': 50, 'Non-AC': 50}},
    'Lucknow-Kanpur': {'Morning': {'AC': 50, 'Non-AC': 50},
                       'Afternoon': {'AC': 50, 'Non-AC': 50},
                       'Evening': {'AC': 50, 'Non-AC': 50}},
    # Add more routes for other destinations similarly
}

# Ticket pricing for routes
ticket_prices = {
    'Kanpur-Lucknow': {'AC': 500, 'Non-AC': 300},
    'Lucknow-Kanpur': {'AC': 500, 'Non-AC': 300},
    # Add more routes and their pricing similarly
}
