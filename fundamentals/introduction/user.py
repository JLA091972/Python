

class User:
    def __init__(self, first_name, last_name, email, age):
        self.firstname = first_name
        self.lastname = last_name
        self.emailaddress = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.firstname, self.lastname, self.emailaddress, self.age, sep='\n')
        return self

    def enroll(self):
        if (self.is_rewards_member != True):
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
        else:
            print('Already a member')
            return False

    def spend_points(self, amount):
        if (self.gold_card_points >= amount):
            self.gold_card_points -= amount
            return self.gold_card_points
        else:
            print('Insufficient points!!')

user1 = User('Juleus','Alqui','juleus@email.com','20')
user1.display_info()
user1.enroll()
user1.spend_points(80)
print(user1.gold_card_points)


user2 = User('jay','Alquiz','jay@email.com','21')
user2.display_info()
user2.enroll()
user2.spend_points(50)
print(user2.gold_card_points)

user3 = User('jay','Alquiz','jay@email.com','21')
user3.display_info()
user3.enroll()
user3.spend_points(300)
print(user3.gold_card_points)




