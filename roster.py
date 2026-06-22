#stap 1
agents = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']
print(agents)

#stap 2
print(agents[0],agents[-1]) #

#stap 3
print(agents[2])

#stap 4
print(agents[1:4])

#stap 5
agents.append("Foxtrot")
print(agents)

#stap 6
agents.insert(2, "Zulu")
print(agents)


# #stap 7
agents.remove("Bravo")
print(agents)

#stap 8
print(len(agents))

#stap 9
scores = [42, 17, 95, 8, 61]
print(max(scores),min(scores))

#stap 10
copy_agents =agents.copy()
print(agents)
agents[0]="yehosh"
print(agents)


##Part 2 — Optional Advanced Basics

#stap 1
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)

numbers2 = [3, 1, 4, 1, 5, 9, 2, 6]
print(numbers2)
numbers2= sorted(numbers2)
print(numbers2)

#stap 2
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
a.extend(b)
print(a)

#stap 3
items = ['x', 'y', 'z', 'x', 'y', 'x']
# x_count = items.count('x')
x = items.count("x")
print(x)
items.remove("x")
items.remove("x")
items.remove("x")
print(items)

#stap 4
data = [1, 2, 3, 4, 5]
print(data[0::1 ])

#stap 5
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])