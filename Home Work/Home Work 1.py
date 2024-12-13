Monday = float(input('See the expense for Monday'))
Tuesday = float(input('See the expense for Tuesday'))
Wednesday = float(input('See the expense for Wednesday'))
Thursday = float(input('See the expense for Thursday'))
Friday =  float(input('See the expense for Friday'))
Saturday = float(input('See the expense for Saturday'))
Sunday = float(input('See the expense for Sunday'))

summ = Monday+Tuesday+Wednesday+Thursday+Friday+Saturday+Sunday
print(f'Total amount of expenses{summ}')
averag = summ / 7
averag_round = round(averag,1)
print(f'Average amounge of expenses {averag_round}')

