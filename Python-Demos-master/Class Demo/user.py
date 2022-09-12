class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        print("=================================")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200
        # self.gold_card_points = self.gold_card_points + 200
        return self
    
    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self
        
antoine = User("Antoine", "Gaton", "agaton@codingdojo.com.", 33, False, 0)
yifan = User("Yifan", "Qiu", "yq@gmail.com.", 24)
giovanni = User("Giovanni", "Torres", "gt@gmail.com.", 28)

antoine.enroll().spend_points(50).display_info()
yifan.enroll().spend_points(80).display_info()
giovanni.display_info()

