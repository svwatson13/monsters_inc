# Monster inc & others OOP 🌮
This is a very serious exercise where we will bravely attempt to OOP monsters.

This exercise will consolidate the knowledge of:

## OOP
- Git & github basics
- Making documentation
- Scrum - needs to meet the definition of DONE
- (extra) start of unit testing (just because)(check if a monster obj can scare_attack)
test could be something along the lines of:

#imports the modules

#Setup 
name = 'Paul'
skills = ['scary', 'hairy', 'loud']
monster1 = Monster(name, skills)

#testing scare_attack()

print('chekcing if monster can scare_attack properly')
print(monster1.scare_attack() == 'RAAAHHH')

Specification
AS a user I should be able to create a monster from Monster()
Behaviors of monster (methods)

A monster should be able to sleep --> respond back with something including 'zzzz'
A monster should be able to eat --> respond back with something including 'nom nom'
A monster should be able to scare_attack --> should return something including 'RAAAHHH'
A monster should be able to have a skill added to his/her list of skills
Looks of a monster (Attributes)

Should have a name that is a string
Should have list of skills