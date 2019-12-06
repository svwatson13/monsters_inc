skills = ['scary', 'hairy', 'loud', 'big', 'evil', 'strong', 'invisible', 'mind control']

class Monster():
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def eat(self, food):
        return 'I love my ' + food
    def sleep(self, sleep='zzzz'):
        return 'I need my ' + sleep
    def scare_attack(self):
        return 'RAAAHHH'
    # Add skills
    def add_skills(self, skills):
        the_monster = self
        the_monster.skills.append(skills)

# user_monster_skills = input('What skills does your monster have? ')
# sam = Monster('Sam', user_monster_skills)

# print(sam.eat('pizza'))
# print(sam.skills == 'Super Strength')
