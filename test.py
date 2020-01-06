class Gowno():

    def __init__(self):

        self.x = 10

    def print(self):

        return self.x


gowno = Gowno()

print(type(gowno))
print(isinstance(gowno, Gowno))

if isinstance(gowno, Gowno) is True:

    print(gowno.print())
    print("cos")