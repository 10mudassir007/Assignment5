sugar = 1
milk = 0.25
tea_leaf = 0.25
water = 1


servings = int(input('Enter number of servings to make : '))

adjusted_sugar = servings * sugar
adjusted_milk = servings * milk
adjusted_tea_leaf = servings * tea_leaf
adj_water = servings * water

print('Sugar(tspoon) required',adjusted_sugar)
print('Milk(cups) required',adjusted_milk)
print('Tea leaf(tspoon) required',adjusted_tea_leaf)
print('Water(cups) required',adjusted_sugar)