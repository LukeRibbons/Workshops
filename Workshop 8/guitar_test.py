from guitar import Guitar

guitar1 = Guitar("Fender Stratocaster", 2014, 765.40)
guitar2 = Guitar("Gibson L-5 CES", 1922, 16032.40)

print(guitar1.get_age())
print(guitar2.get_age())
print(guitar1.is_vintage())
print(guitar2.is_vintage())