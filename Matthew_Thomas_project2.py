Dates = open("Project2.txt", "r", encoding="utf-8")
lines_in_file = Dates.readlines()

data_lines = lines_in_file[1:]

for line in data_lines:
    parts = line.split(";")

    date_string = parts[0]
    year = date_string[:4]

    income = float(parts[1])
    house_price = float(parts[2])

    ratio = house_price / income

    print(f"{year}: {ratio:.2f}")