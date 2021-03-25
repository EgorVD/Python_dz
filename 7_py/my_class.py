class geom_fig:
    def __init__():
        pass


class krug(geom_fig):
    def __init__(self, r):
        self.r = r

    def get_area(self): # считаем площадь 
        res = (self.r**2) * 3.14
        return res
    
    def get_perimetr(self): # считаем периметр
        res = self.r * 2 * 3.14
        return res


class treug(geom_fig):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self): # считаем площадь по формуле Герона
        p = self.get_perimetr() / 2
        res = (p * (p-self.a) * (p-self.b) * (p-self.c))**0.5
        return res

    def get_perimetr(self):
        res = self.a + self.b + self.c
        return res

class pryamoug(geom_fig):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        res = self.a * self.b
        return res

    def get_perimetr(self):
        res = (self.a + self.b) * 2
        return res


class prism(pryamoug):
    def __init__(self, v, a, b):
        self.v = v
        self.a = a
        self.b = b

    def get_vol(self): # считаем объем
        res = self.a * self.b * self.v
        return res

class shar(krug):
    def __init__(self, r):
        self.r = r

    def get_vol(self): # считаем объем
        res = (4/3) * 3.14 * (self.r**3)
        return res 