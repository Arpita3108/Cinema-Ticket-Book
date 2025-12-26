import sys

def cinema_booking(movie_name, total_seats, tickets_booked, ticket_price):
    if tickets_booked > total_seats:
        status = "Seats not available"
        total_price = 0
        seats_left = total_seats
    else:
        status = "Booking successful"
        total_price = tickets_booked * ticket_price
        seats_left = total_seats - tickets_booked

    result = (
        f"Movie Name      : {movie_name}\n"
        f"Total Seats    : {total_seats}\n"
        f"Tickets Booked : {tickets_booked}\n"
        f"Ticket Price   : ₹{ticket_price}\n"
        f"Booking Status : {status}\n"
        f"Total Price    : ₹{total_price}\n"
        f"Seats Left     : {seats_left}"
    )
    return result


if __name__ == "__main__":

    # Default values
    movie_name = "Avengers"
    total_seats = 50
    tickets_booked = 4
    ticket_price = 150

    print("Cinema Ticket Booking Details:\n")
    print(cinema_booking(movie_name, total_seats, tickets_booked, ticket_price))
