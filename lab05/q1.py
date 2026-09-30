filename = "experiments.txt"

def display(filename):
    with open(filename) as f:
        for line in f:
            data = line.strip().split(",")
            print("ID: ", data[0])
            print("Model Name: ", data[1])
            print("dataset name: ", data[2])
            print("learning rate: ", data[3])
            print("epochs: ", data[4])

def search(id):
    file = open(filename,"r")
    for line in file:
        data = line.strip().split(",")
        if int(data[0]) == id:
            print(data)
            file.close()
            return
    print("Not found")
    file.close()

def add(id, mName, dName, rate, ep):
    file = open(filename,"a")
    file.write(str(id)+","+mName+","+dName+","+str(rate)+","+str(ep)+"\n")
    file.close()

def update(id, mName, dName, rate, ep):
    file = open(filename,"r")
    updLines = []
    for line in file:
        data = line.strip().split(",")
        if int(data[0]) == id:
            line = data[0]+","+mName+","+dName+","+str(rate)+","+str(ep)+"\n"
        updLines.append(line)
    file.close()
    file = open(filename,"w")
    file.writelines(updLines)
    file.close()

def delete(id):
    file = open(filename,"r")
    oglines = []
    for line in file:
        data = line.strip().split(",")
        if int(data[0]) != id:
            oglines.append(line)
    file.close()
    file = open(filename,"w")
    file.writelines(oglines)
    file.close()

with open(filename, "w") as file:
    file.write("101,CNN,MNIST,0.01,20\n")
    file.write("102,RNN,IMDB,0.001,30\n")
display(filename)
search(102)
add(103,"ANN","CIFAR10",0.05,50)
update(103,"ANN","CIFAR10",0.05,10)
delete(101)
display(filename)