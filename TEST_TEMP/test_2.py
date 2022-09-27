list_1 = [{"name": "aaaa", "id": "0001"}, {"name": "bbbb", "id": "0002"}, {"name": "cccc", "id": "0003"}, {"name": "dddd", "id": "0004"}]

list_2 = [[["0001", 1], ["0002", 2]], [["0003", 3], ["0004", 4]]]

list_3 = []


for element in list_2:
    match = [element[0][0], element[0][1]] ,[element[1][0], element[1][1]]
    for sub in list_1:
        if match[0][0] in sub["id"]:
            match[0][0] = sub["name"]
        elif match[1][0] in sub["id"]:
            match[1][0] = sub["name"]
    new_match = [[match[0][0],match[0][1]],[match[1][0],match[1][1]]]
    list_3.append(new_match)

for match in list_3:
    print(match)
    
