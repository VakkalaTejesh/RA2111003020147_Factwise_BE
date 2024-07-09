def num2word(number):
    if number == 0:
        return ""
    if number == 1000:
        return "one thousand"
    
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    word = ""
    
    hundreds = number // 100
    if hundreds > 0:
        word += ones[hundreds - 1] + " hundred"
        number %= 100
        if number > 0:
            word += " and "
    if number >= 20:
        tens_digit = number // 10
        word += tens[tens_digit]
        number %= 10
        if number > 0:
            word += "-" + ones[number - 1]
    elif number >= 10:
        word += teens[number - 10]
    elif number > 0:
        word += ones[number - 1]
    return word
def count_letters_in_words(number):
    total_letters = 0
    for i in range(1, number + 1):
        word = num2word(i)
        word_without_spaces_or_hyphens = word.replace(" ", "").replace("-", "")
        total_letters += len(word_without_spaces_or_hyphens)
    return total_letters
def solveEscape17():
    total_letters = count_letters_in_words(1000)
    print("Total letters used from 1 to 1000:", total_letters)
if _name_ == "_main_":
    solveEscape17()
