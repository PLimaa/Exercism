"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ["A","B","C","D"]
    current_letter = 0
    limit = 0 
    while limit < number:
        yield seats[current_letter]
        current_letter += 1
        limit +=1
        if current_letter >= len(seats):
            current_letter = 0
            

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    fileira = 1 
    limite = 0
    letras = generate_seat_letters(number)
    while limite < number:
        if fileira == 13:
            fileira += 1
            continue
        else:
            letra = next(letras)
            yield f"{fileira}{letra}"
            limite +=1
        if letra == "D":
            fileira += 1         
    
def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seat_passengers = dict()
    seats = generate_seats(len(passengers))
    for passenger in passengers:
        seat_passengers[passenger] = next(seats)
    return seat_passengers
    

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat in seat_numbers:
        base_code = f"{seat}{flight_id}"
        zeros = 12 - len(base_code)
        yield base_code + (zeros*"0")
    
        
    
