from cinema import cinema_booking


def test_booking_success():
    result = cinema_booking("Avengers", 50, 4, 150)

    assert "Booking successful" in result
    assert "Total Price    : ₹600" in result
    assert "Seats Left     : 46" in result


def test_seats_not_available():
    result = cinema_booking("Avengers", 10, 15, 150)

    assert "Seats not available" in result
    assert "Total Price    : ₹0" in result
    assert "Seats Left     : 10" in result


def test_exact_seat_booking():
    result = cinema_booking("Avatar", 5, 5, 200)

    assert "Booking successful" in result
    assert "Total Price    : ₹1000" in result
    assert "Seats Left     : 0" in result
