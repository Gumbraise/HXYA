import math, random, datetime, sys

visaPrefixList = [4539,4556,4916,4532,4929,40240071,4485,4716,4]
mastercardPrefixList = [51,52,53,54,55,2221,2222,2223,2224,2225,2226,2227,2228,2229,223,224,225,226,227,228,229,23,24,25,26,270,271,2720]

def completed_number(prefix, length):
    ccnumber = str(prefix)
    while (len(ccnumber) < (length - 2)):
        ccnumber = str(ccnumber) + str(math.floor(random.randint(0, 9)))
    
    reversedCCnumberString = str(ccnumber)[::-1]

    reversedCCnumber = []

    i = 0
    while i < len(reversedCCnumberString):
        reversedCCnumber.append(int(reversedCCnumberString[i]))
        i = i + 1

    sum = 0
    pos = 0

    while pos < 4:
        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd = odd - 9

        sum = sum + odd

        if pos != (length - 2):
            sum = sum + reversedCCnumber[pos + 1]
        
        pos = pos + 2

        checkdigit = int(((math.floor(sum/10) + 1) * 10 - sum) % 10)
        ccnumber = str(ccnumber) + str(checkdigit)

    return ccnumber

def exp_number():
    year_now = int(datetime.datetime.now().strftime("%Y"))

    month = str(random.randint(1, 12))
    year = str(random.randint(year_now + 1, year_now + 3))

    if len(month) < 2:
        month = '0' + month
    
    exp = month + '|' + year
    return exp

def cvv():
    cvv = str(random.randint(100, 999))

    return cvv

def credit_card_number(prefixList):
    randomArrayIndex = int(math.floor(random.randint(0, (len(prefixList) - 1))))
    ccnumber = prefixList[randomArrayIndex]

    result = completed_number(ccnumber, 16) + '|' + exp_number() + '|' + cvv()

    print(result)
    
    return result


prefix_value = str(input('Choose between Visa or MasterCard: '))
if prefix_value == 'Visa':
    try:
        many = int(input('How many ?: '))
    except ValueError:
        sys.exit('Please type a number between 1-∝')
    for i in range (many):
        credit_card_number(visaPrefixList)
elif prefix_value == 'MasterCard':
    try:
        many = int(input('How many ?: '))
    except ValueError:
        sys.exit('Please type a number between 1-∝')

    for i in range (many):
        credit_card_number(mastercardPrefixList)
else:
    sys.exit('Wrong entry')
