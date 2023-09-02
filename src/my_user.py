class User:
    def __init__(self, user_name, user_age, user_address):
        self.name = user_name
        self.age = user_age
        self.address = user_address
        self.my_image = "my_image.png"
        self.goal = "서비스 만들기"
        self.favorit_food = ["짜장면", "피자", "치킨", "라면"] 
    
    def age_plus(self):
        self.age = self.age + 1 # 나이를 한살 먹는다

    def change_address(self, change_address):
        self.address = change_address

    def add_favorit_food(self, food):
        self.favorit_food.append(food)
    
    def eat_my_food(self):
        for food in self.favorit_food:
            print(f"Good my food {food}")
 



