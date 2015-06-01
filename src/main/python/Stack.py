from sys import argv

class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def getElements(self):
        return self.items
    def saveAsFile(self):
        f = open("Stack", "w")
        list_of_string = list(map(lambda x: str(x), self.getElements()))
        f.writelines(str(list_of_string))
        f.close()
        


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print stack.getElements()
    stack.saveAsFile()

if __name__ == "__main__":
    main()    