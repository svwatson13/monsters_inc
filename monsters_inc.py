from monster_class import *
from monster_test import *

# name = 'Mike'
# monster1 = Monster(name, user_monster_skills)
name = 'Sulley'
monster2 = Monster(name, skills)
name = 'Sam'
monster3 = Monster(name, ['Hairy', 'Big', 'Strong'])
#testing scare_attack()

# for skill in monster1.skills:
#     print(skill)

# print(monster1.skills)

# print('I am', monster1.name, monster1.scare_attack(), 'Beware of my skills:', monster1.skills)
print('I am', monster2.name, monster2.scare_attack(), 'Beware of my skills:', monster2.skills, monster2.add_skills('Fear'))

# print('I am', monster2.name, monster2.scare_attack(), 'Beware of my skills:')
# for skill in skills:
#     print(skill)
# print(monster3.name)
# for skill in monster3.skills:
#     print(skill)