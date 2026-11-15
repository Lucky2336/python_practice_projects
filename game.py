

def table():  
    with open("table.txt", "w") as f:
        for i in range(2, 30):
            st = f"{i} ka pahada\n"
            f.write(st)
            for j in range(1, 11):
               
                jh = f"{i} * {j} = {i*j}\n"
                f.write(jh)
            print(f"table of {i} is written in file")    

table()
# with open("file.txt") as f:
#     data = f.read()
#     if("twinkle" in data):
#         print("prstent")
#     else:
#         print("not")    