numbers = {1, 2, 3, 4}

numbers.add(5)
numbers.add(6)

numbers.remove(1)
numbers.remove(2)


even_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

# აერთებს ორივე სეტს
numbers.union(even_numbers)

# ქმნის ახალ სეტს რომელშიც მხოლოდ ის რიცხვებია რომლებიც ორივე სეტშია
numbers.intersection(even_numbers)

# ქმნის ახალ სეტს რომელშიც ისეთი რიცხვებია რომლებიც პირველ სეტშია და მეორეში არა
numbers.difference(even_numbers)