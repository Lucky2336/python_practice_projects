n = int(input("enter a number: 10000"))

table = [n*i for i in range(1, 11)]
with open("tables", "a") as f:
      f.write(str(table) + "\n")