def to_era(year):
    
    if year > 1868 and year <= 1912:
        return "明治" + str(year - 1868 + 1) + "年です!"
    
    if year > 1912 and year <= 1926:
        return "大正" + str(year - 1912 + 1) + "年です!"

    if year > 1926 and year <= 1989:
        return "昭和" + str(year - 1926 + 1) + "年です!"

    if year > 1989 and year <= 2019:
        return "平成" + str(year - 1989 + 1) + "年です!"
    
    if year > 2019:
        return "令和" + str(year - 2019 + 1) + "年です!"

    return "siran"

print(to_era(2023))
