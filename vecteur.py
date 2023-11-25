class Vecteur2D:
    count = 0
    def __init__(self, X = 0.0 , Y = 0.0):
        self.X = X
        self.Y = Y
        Vecteur2D.count += 1
    
    def ToString(self):
        return f"X={self.X}- Y={self.Y}"
    
    def Equal(self, Vec2):
        if (self.X == Vec2.X and self.Y == Vec2.Y):
            return True
        else : 
            return False
        
    def Norm(self):
        return (self.X ** 2 + self.Y ** 2) ** 0.5

class Vecteur3D(Vecteur2D):
    def __init__(self, X=0.0, Y=0.0, Z = 0.0):
        super().__init__(X, Y)
        self.Z = Z

    def ToString(self):
        return f"X={self.X} - Y={self.Y} - Z={self.Z}"
    
    def Equal(self, Vec2):
        if (self.X == Vec2.X and self.Y == Vec2.Y and self.Z == Vec2.Z):
            return True
        else :
            return False
        
    def Norm(self):
        return (self.X ** 2 + self.Y ** 2 + self.Z ** 2) ** 0.5
    
#usage exempl :
vec1 = Vecteur2D(5.0, 5.0)
vec2 = Vecteur2D(5.0, 5.0)
vec3 = Vecteur3D(5.0, 5.0, 5.0)
vec4 = Vecteur3D(3.0, 4.0, 5.0)
print("vecteur 1 :")
print(vec1.ToString())
print(vec1.Equal(vec2))
print(vec1.Norm())

print("vecteur 2 :")
print(vec3.ToString())
print(vec3.Equal(vec4 ))
print(vec3.Norm( ))

print(f"nombre d instance cree : {Vecteur2D.count}")


    
