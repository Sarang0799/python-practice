class Phone:
    def model(self,model_type):
        print("Model=",model_type)
    def set_cost(self,cost):
        print("Cost=",cost)

class Redmi(Phone):
    def color(self,color):
        print("Color of Phone is", color)

p1= Phone()
p_s= Redmi()
p_s.model("Samsung S22 Ultra")
p_s.cost(30000)
p_s.color("Rose Gold")
