# getting user info
city_flight = input("Enter the destination city (e.g., New York, Paris, Tokyo): ")
num_nights = int(input("Enter the number of nights: "))
rental_days = int(input("Enter the number of rental days: "))
def plane_cost(city_flight):
    if city_flight == "New York":
        return 500
    elif city_flight == "Paris":
        return 400
    elif city_flight == "Tokyo":
        return 600
    else:
        return 300

def hotel_cost(num_nights):
    return num_nights * 100  # Assuming $100 per night

def car_rental_cost(rental_days):
    return rental_days * 50  # Assuming $50 per day

def holiday_cost(num_nights, city_flight, rental_days):
    total_cost = (plane_cost(city_flight) +
                  hotel_cost(num_nights) +
                  car_rental_cost(rental_days))
    return total_cost
total = holiday_cost(num_nights, city_flight, rental_days)
print(f"Total holiday cost: £{total}")
