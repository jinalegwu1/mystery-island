def welcome_player() :
    print("welcome to Mystery Island!")
    print("Your adventure starts now.")
welcome_player()

def welcome_name(name):
    print(f"welcome! {name}, welome to your farm")
welcome_name("James")

def check_energy(energy):
    if energy > 0:
        return True
    else:
        return False
result = check_energy(3)
print(result)

def shopping_baskets():
    basket = ["garri", "beans", "rice", "fish"]
    print(basket[0])
    basket.append("milk")
    print(basket)
    if "rice" in basket:
        print("rice is here!")
    basket.remove("fish")
    print(f"list of the availabe items: {basket}")
shopping_baskets()