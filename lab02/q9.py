info = ("MyApp", "7", ("windows", "linux"), ("MySql", "oracle"))
print("Application Name:", info[0])
print("Version:", info[1])
print("Supported Enviroments:", info[2])
print("Database configuration:", info[3])
#tuple are immutable, values can't be altered
#info[0] = "notMyApp" gives TypeError: 'tuple' object does not support item assignment
