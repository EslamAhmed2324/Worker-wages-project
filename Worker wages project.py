length_question = input("what is your room length \n")
width_question = input("what is your room width \n")
meter_question = input("how much for 1 meter \n")

length = float(length_question)
width = float(width_question)
meter = float(meter_question)

area = length * width
meter = 5 * area
area = str(area)
meter = str(meter)

print("your area space is " + area)
print("your price is " + meter)