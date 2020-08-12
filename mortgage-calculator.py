def mortgage_calculator(loan, years, rate):
    n = 0
    if rate > 0.99:
        rate = rate / 100
    answer = False
    interval = input('What compounding interval is your loan? (daily/weekly/biweekly/monthly/yearly) ')
    while not answer:
        if interval == 'daily':
            n = 365
            answer = True
        elif interval == 'weekly':
            n = 52
            answer = True
        elif interval == 'biweekly':
            n = 26
            answer = True
        elif interval == 'monthly':
            n = 12
            answer = True
        elif interval == 'yearly':
            n = 1
            answer = True
        else:
            print('Not a correct interval!')
            answer = False
            interval = input("What compounding interval is your loan? (daily/weekly/biweekly/monthly/yearly) ")

    payment = round(loan * (1 + rate) / (years * n), 2)
    print('Your {0} mortgage payment will be ${1}'.format(interval, payment))

mortgage_calculator(500000, 30, 3)
