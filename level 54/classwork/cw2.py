def greet_people(special, *guests, **visitors):
    print(f'Hello {special}, you are our most important guest')

    for guest in guests:
        print(f'Hello {guest}')

    for key, name in visitors.items():
        print(f'Hello {name} you are one of our visitors')

# arg აგროვებს ყველა გადაცემულ არგუმენტს და ინახავს tuple-ში
# kwarg აგროვებს ყველა გადაცემულ არგუმენტს და ინახავს dictionary-შ