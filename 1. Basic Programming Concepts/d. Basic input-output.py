# # Create a program that asks for a temperature in Celsius and converts it to Fahrenheit, with proper error handling.
# # °C = (°F - 32) × 5/9

# def c_to_f(c):
#     # A function that converts celcius to fahrenheit
#     F = c*9/5 +32
#     return F

# try:
#     # takes input temperature from user in float value 
#     celcius = float(input("Enter the temperature(in C): "))
#     Fahrenheit = c_to_f(celcius) # access the function
#     print(f"{celcius} C in Fahrenheit is {Fahrenheit} F") # print the output using fstring method
# except ValueError: # in case of invalid value
#     print("Please enter a valid numeric value")
    

# # Make a program that creates a receipt for a shop, taking item names and prices as input and formatting them in a nice table.

# def linePrice(quantity, price):
#     return quantity*price

# def discount(total):
#     return total*0.1

# items = []
# total = 0
# shopMore = True
# with open('receipt.txt', 'w') as file:
#     while shopMore:
#         item = input("Enter an item or Press \"done\" to stop: ")
#         if item.lower() == "done":
#             shopMore = False
#             break
#         quantity = int(input("Enter the quantity : "))
#         price = float(input("Enter the price : "))
#         items.append((item, quantity, price))


#     file.write("\n|" + "-"*40 + "|")
#     file.write(f"\n|{"SHOP RECEIPT":^40}|")
#     file.write("\n|" + "="*40 + "|")
#     file.write(f"\n|{"Item":<10}{"Quantity":^10}{"Price":>10}{"linePrice":>10}|")
#     file.write("\n|" + "-"*40 + "|")
#     for item, quantity, price in items:
#         file.write(f"\n|{item:<10}{quantity:^10}{price:>10}{linePrice(quantity, price):>10}|")
#         total += linePrice(quantity, price)
#     file.write("\n|" + "-"*40 + "|")
#     file.write(f"\n|{"Total":>30}{total:>10}|")
#     file.write(f"\n|{"Discount":>30}{discount(total):>10}|")
#     file.write(f"\n|{"Final Price":>30}{total - discount(total):>10}|")

#     file.write("\n|" + "-"*40 + "|")

#     print("Receipt saved to receipt.txt")



# # Write a program that takes a sentence as input and file.writes statistics about it (number of words, letters, spaces, etc.).

# sentence = input("Enter a Sentence : ").strip()
# words = sentence.split()
# if words:
#     lenWord = 0
#     shorWord = float('inf')
#     lengthyword = ""
#     shortword = ""
#     for word in words:
#         cleaned_word = ''.join([i for i in word if i.isalnum()])
#         if lenWord<len(cleaned_word):
#             lenWord = len(cleaned_word)
#             lengthyword = cleaned_word
#         if shorWord>len(cleaned_word):
#             shorWord = len(cleaned_word)
#             shortword = cleaned_word
# letters = 0
# spaces = 0
# numbers = 0
# punc = 0

# for i in sentence:
#     if i.isspace():
#         spaces += 1
        
#     if not i.isalnum() and not i == ' ':
#         punc += 1

#     if i.isalpha():
#         letters += 1

#     if i.isdigit():
#         numbers += 1

# print(f"""Words : {len(words)}
# Longest word : {lengthyword}
# Shortest word : {shortword}
# Spaces : {spaces}
# Letters : {letters}
# Numbers : {numbers}
# Punctuations : {punc}"""
#       )