devsMoney = 100
devCanPlaySmash = False

if devsMoney > 10 and devCanPlaySmash:
    print("Dev enters a smash tournament!")
elif devsMoney < 1 and devCanPlaySmash:
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash")
