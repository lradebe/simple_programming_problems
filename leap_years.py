def leap_years():

    last_leap = int(2020)
    leap_years = []

    while len(leap_years) != 20:
        last_leap = last_leap + 4
        leap_years.append(last_leap)
    print(leap_years)

leap_years()
