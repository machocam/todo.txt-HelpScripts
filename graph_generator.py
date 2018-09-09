# -*- coding: UTF-8 -*-
# I got this code from this website : https://gkbrk.com/2017/04/graphs-from-my-todo-txt/
# The goal of the script is to graph progress on todolist



import datetime
import matplotlib.pyplot as plt

DaysWanted = 10

def get_stats(filename):
    data = {}
    with open(filename) as todofile:
        for line in todofile:
            date = line.split()[1]
            if date in data:
                data[date] += 1
            else:
                data[date] = 1
    print data
    return data


def get_last_days(days):
	DateList = []
	for day in range(days)[::-1]:
		date = datetime.datetime.today() - datetime.timedelta(days=day)
		DateList.append(date.date().isoformat()) # Isoformat is 2017-04-18
	return DateList


stats = get_stats("/Users/rodrigocamacho/Dropbox/Apps/Simpletask/done.txt")

todoCounts = []
for date in get_last_days(DaysWanted):
    # Get the value from the txt file that you are parsing
    # 0 here is the default when no tasks were accomplished that day
    todoCounts.append(stats.get(date, 0))

print todoCounts
print get_last_days(DaysWanted)

plt.grid(True)
plt.title("Todo.txt Progress")
plt.ylabel("Number of tasks done")
plt.yticks(range(max(todoCounts) + 1))
plt.xticks(range(DaysWanted), get_last_days(DaysWanted), rotation=80)

plt.plot(todoCounts,marker = 'x')
plt.tight_layout()
plt.savefig('/Users/rodrigocamacho/Desktop/todo.png', dpi=200)