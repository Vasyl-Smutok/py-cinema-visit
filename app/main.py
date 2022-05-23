from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(customers: list, hall_number, cleaner, movie):
    customers = [
        Customer(customer["name"], customer["food"]) for customer in customers
    ]
    for customer in customers:
        CinemaBar().sell_product(customer, customer.food)
    cleaner = Cleaner(cleaner)
    CinemaHall(hall_number).movie_session(movie, customers, cleaner)
