time  = '1h 45m,360s,25m,30m 120s,2h 60s'
time_edit = time.replace(",", " ")
time_edit = time_edit.split(" ")
total_time = 0

for i in time_edit:
    if i[-1] == "h":
        total_time += int(i[:-1]) * 60
    elif i[-1] == "m":
        total_time += int(i[:-1])
    elif i[-1] == "s":
        total_time += int(i[:-1]) // 60

print(total_time)
