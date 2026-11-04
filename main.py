print("=======================================================")
print("Welcome to farm management system")
print("=======================================================")
nickName = input("Enter Your Nick Name: ")
farm_count = 0
farm_count = farm_count + 1
farm_count = farm_count + 1
rice_harvested = int(input("how many bags of rice did you harvested: "))
if rice_harvested > 10:
    print("high harvest")
elif rice_harvested >= 10:
    print("normal harvest")
else:
    print("not enough harvest")
print(f"Hello {nickName}, welcome to farm management system")
print(f"farm count: {farm_count}")
print("bags of rice:", rice_harvested + 5)
