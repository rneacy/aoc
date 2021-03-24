from pathlib import Path

with open(Path(__file__).parent.joinpath("input"), "r") as f:
    data = [int(item) for item in f.readline().split(" ")]

meta_count = 0
def partA():
    analyse(0)
    print("Metadata total: " + str(meta_count))

def analyse(index):
    global meta_count
    cnodes = data[index] # num child nodes
    mnodes = data[index+1] # num meta nodes

    print("Node has " + str(cnodes) + " children, " + str(mnodes) + " metadatas.")

    index += 2

    c_index = index
    if cnodes:
        for i in range(cnodes):
            c_index = analyse(c_index) # analyse the child node

    if mnodes:
        index = c_index
        for i in range(mnodes):
            meta_count += data[index]
            index += 1

    return index

partA()