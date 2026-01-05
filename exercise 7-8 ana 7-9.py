sandwich_order = ["david","john","paul","peter","pastrami"]
finished_sandwich = []
for sandwich in sandwich_order:
    print(f"{sandwich.title()} i made your tuna sandwich")
for sandwich in sandwich_order:
  finished_sandwich.append(sandwich)
print(finished_sandwich)
for sandwich in finished_sandwich:
   print(f"{sandwich.title()} all sandwich has been made")
#7.9
sandwich_order = ["peter","pastrami","paul","john","pastrami","david","pastrami"]
finished_sandwich = []
message ="deli has run out of sandwich"
print(message)
for sandwich in sandwich_order:
    sandwich_to_remove = "pastrami"
    while sandwich_to_remove in sandwich_order:
        sandwich_order.remove (sandwich_to_remove)
    print(sandwich_order)
for sandwich in sandwich_order:
        finished_sandwich.append(sandwich)
        print(finished_sandwich)
        for sandwich in finished_sandwich:
            print(f"{sandwich.title()} all sandwich has been send:")