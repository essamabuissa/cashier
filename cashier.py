def main():
	# write code here

	items_list = []
	items_dic  = {"name":"","price":0,"quantity":0}

	while True:
		item_dic = items_dic.copy()
		item_dic["name"] = input('item (enter "done" when finished): ')
		if item_dic["name"] == "done":
			break
		item_dic["price"]= float(input('Price: '))
		item_dic["quantity"] = float(input('Quantity: '))
		items_list.append(item_dic)

	print()
	print("-------------------")
	print("receipt")
	print("-------------------")

	total_price = 0
	for items in items_list:
		print(f"{str(items['quantity'])} {items['name']} {str(float(items['price'] * items['quantity']))}KD")
		total_price += (float(items['price'] * items['quantity']))
	print("-------------------")
	print(f"Total Price: {str(total_price)}KD")


if __name__ == '__main__':
	main()
