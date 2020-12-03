price_of_first_sweet = str(input("Enter the price of the first sweet: "))
price_of_second_sweet = str(input("Enter the price of the second sweet: "))
price_of_third_sweet = str(input("Enter the price of the third sweet: "))
price_of_fourth_sweet = str(input("Enter the price of the fourth sweet: "))
price_of_fifth_sweet = str(input("Enter the price of the fifth sweet: "))

price1=int(price_of_first_sweet[:2])
price2=int(price_of_second_sweet[:2])
price3=int(price_of_third_sweet[:2])
price4=int(price_of_fourth_sweet[:2])
price5=int(price_of_fifth_sweet[:2])
p='p'
sum_price=[price1,price2, price3, price4, price5]
total_price=int(price1 + price2 + price3 + price4 + price5)
print("total price: " + str(total_price)+p)
length_of_sweets= len(sum_price)
mean =total_price/length_of_sweets
print('average price: ' + str(mean)+p)
print('Highest price: '+ str(max(sum_price))+p)
print ('lowest price: ' + str(min(sum_price))+p)