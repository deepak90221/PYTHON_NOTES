class TicketBookingSystem:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets
        self.available_tickets = total_tickets
        self.booked_tickets = {}

    def view_tickets(self):
        print(f"Available tickets: {self.available_tickets}/{self.total_tickets}")

    def book_ticket(self, customer_name):
        if self.available_tickets > 0:
            ticket_id = self.total_tickets - self.available_tickets + 1
            self.booked_tickets[ticket_id] = customer_name
            self.available_tickets -= 1
            print(f"Ticket booked successfully! Ticket ID: {ticket_id}")
        else:
            print("No tickets available!")

    def cancel_ticket(self, ticket_id):
        if ticket_id in self.booked_tickets:
            del self.booked_tickets[ticket_id]
            self.available_tickets += 1
            print(f"Ticket ID: {ticket_id} has been canceled.")
        else:
            print("Invalid Ticket ID!")

    def view_booked_tickets(self):
        if self.booked_tickets:
            print("Booked Tickets:")
            for ticket_id, customer_name in self.booked_tickets.items():
                print(f"Ticket ID: {ticket_id}, Customer Name: {customer_name}")
        else:
            print("No tickets booked yet!")


system = TicketBookingSystem(total_tickets=5)

while True:
    print("\nTicket Booking System")
    print("1. View Available Tickets")
    print("2. Book a Ticket")
    print("3. Cancel a Ticket")
    print("4. View Booked Tickets")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        system.view_tickets()
    elif choice == '2':
        customer_name = input("Enter your name: ")
        system.book_ticket(customer_name)
    elif choice == '3':
        ticket_id = int(input("Enter Ticket ID to cancel: "))
        system.cancel_ticket(ticket_id)
    elif choice == '4':
        system.view_booked_tickets()
    elif choice == '5':
        break
    else:
        print("Invalid choice! Please try again.")
