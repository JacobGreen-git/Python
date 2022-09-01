class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200
        return self

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self

Joe = User('Joe', 'Brown', ' fafq @gmail.com', 34)
Noel = User('Noel', 'Smith', ' fafq @gmail.com', 24)
Jose = User('Jose', 'Jones', ' fafq @gmail.com', 55)
# Joe.display_info()

# Joe.enroll()
# Joe.spend_points(50)

# Noel.enroll()
# Noel.spend_points(80)

Joe.display_info()
Noel.display_info()
Jose.display_info()