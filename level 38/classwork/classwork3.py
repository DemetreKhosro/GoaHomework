'''3) შექმენით list, tuple და set. კომენტარებით დაწერეთ თითოეულის თვისება და ყველა თვისებიდან მოიყვანეთ მაგალითები'''

l1st = [1, 2, 3, 4, 5, 5, 1] # არის Mutable და აქვს დუპლიკატები, indexed
l1st.append(6)

tupl3 = (1, 2, 3, 4, 5) # არის Immutable, indexed
tupl3.append(6) # Error

s3t = {1, 2, 3, 4, 5, 5} # არის Mutable და არ აქვს დუპლიკატები, not indexed
s3t.append(6) # Error