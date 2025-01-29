a = ['{"calories": 70, "proteins": 3, "fats": 4, "carbohydrates": 5}',
     '{"calories": 52, "proteins": 0.26, "fats": 0.17, "carbohydrates": 14}',
     '{"calories": 86, "proteins": 12, "fats": 5, "carbohydrates": 3}',
     '{"calories": 884, "proteins": 0, "fats": 100, "carbohydrates": 0}']

for i in a:
    w = i.replace('\'', '*')
    w = w.replace('\"', '\'')
    w = w.replace('*', '\"')
    print(w)
