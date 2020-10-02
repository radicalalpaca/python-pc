digits = ["zero",
         "one",
         "two",
         "three",
         "four",
         "five",
         "six",
         "seven",
         "eight",
         "nine",]
teens = ["ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen"]
tens = ["twenty",
        "thirty",
        "fourty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety"]

def number_words():
    lengths = []
    for n in range(20, 100):
        number = str(n)
        word = ""
        if int(number) < 100:
            if int(number) < 10:
                word += digits[int(number)]
            elif int(number) < 20 and int(number) > 9:
                word += (teens[int(number) % 10])
            elif int(number) % 10 == 0:
                word += (tens[int(number[0]) - 2])
            else:
                word += (tens[int(number[0]) - 2] + digits[int(number[1])])
            lengths.append(word)
        else:
            word += (digits[int(number[0])] + "hundred")
            if int(number[1:]) < 20 and int(number[1:]) > 9:
                word += ("and" + teens[int(number[1:]) % 10])
            elif int(number[1:]) < 10 and int(number[1:]) > 0:
                word += ("and" + digits[int(number[1:])])
            elif int(number) % 100 == 0:
                pass
            elif int(number[1:]) % 10 == 0:
                word += ("and" + tens[int(number[1]) - 2])
            elif int(number[1:]) > 20:
                word += ("and" + tens[int(number[1]) - 2] + digits[int(number[2])])
            else:
                pass
            lengths.append(word)
    print(lengths)

if __name__ == '__main__':
    number_words()