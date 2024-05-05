class StarCinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)
        


class Hall:
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        StarCinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        self.__seats[id] = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        

    def book_seats(self, id, seats_to_book):
        if id not in self.__seats:
            print(f"No show in this  ID {id} exists.")
            return False

        seats = self.__seats[id]
        all_seats_valid = True
        for row, col in seats_to_book:
            if not (0 <= row < self.__rows and 0 <= col < self.__cols):
                print(f"Seat at row {row}, column {col} is out of bounds.")
                all_seats_valid = False
            elif seats[row][col] != 0:
                print(f"Seat at row {row}, column {col} is already booked.")
                all_seats_valid = False

        if not all_seats_valid:
            return False

        for row, col in seats_to_book:
            seats[row][col] = 1
        print(f"Successfully booked {len(seats_to_book)} seats for show ID {id}.")
        return True

    def view_available_seats(self, id):
        if id not in self.__seats:
            print(f"No show with ID {id} found in Hall {self.__hall_no}.")
            return

        print(f"Available seats for Show ID {id} in Hall {self.__hall_no}:")
        for row in self.__seats[id]:
            print(row)

    def get_hall_no(self):
        return self.__hall_no


hall1 = Hall(10, 12, 1)
hall2 = Hall(8, 10, 2)

hall1.entry_show("001", "Avengers Endgame", "18:00")
hall2.entry_show("002", "Inception", "20:00")

run = True

while run:
    print(" 1. View all shows")
    print(" 2. View available seats")
    print(" 3. Book tickets")
    print(" 4. Exit")

    option = int(input("Enter an option: "))

    if option == 1:
        
        for hall in StarCinema._StarCinema__hall_list:  
            for show_info in hall._Hall__show_list:      
                print(f"Hall {hall.get_hall_no()}: ID {show_info[0]} - {show_info[1]} at {show_info[2]}")

    elif option == 2:
        id = input("Enter the show ID to view available seats: ")
        for hall in StarCinema._StarCinema__hall_list:  
            if id in hall._Hall__seats:                
                hall.view_available_seats(id)
                break
        else:
            print(f"No show with ID {id} found.")

    elif option == 3:
        id = input("Enter the show ID to book tickets: ")
        for hall in StarCinema._StarCinema__hall_list:  
            if id in hall._Hall__seats:                
                row = int(input("Enter the row number: "))
                col = int(input("Enter the column number: "))
                if hall.book_seats(id, [(row, col)]):
                    print("Booking successful.")
                else:
                    print("Booking failed.")
                break
        else:
            print(f"No show with ID {id} found.")

    elif option == 4:
        run = False
        break

    else:
        print("Invalid option")
