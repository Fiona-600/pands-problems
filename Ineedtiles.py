# Calculating Tiles Needed for Bathroom in m2

length = float(input ("Enter Room Length: "))
width = float(input ("Enter Room Width: "))


area = length * width

wastage = area * 0.05

needed = area + wastage

print("You need",needed,"tiles in meters squared")


