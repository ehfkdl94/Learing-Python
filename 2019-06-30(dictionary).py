lux = {'health':490, 'mana' : 334, 'melee': 550, 'armor':18.72}
print(lux)
print(lux['health'])

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print(lux2)

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3)

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
print(lux4)

print(lux['health'])
print(lux['armor'])
lux['health'] = 2037
lux['mana']=1184
print(lux)
lux['mana_regen'] = 3.28
print(lux)
print('health' in lux)
print('attack_speed'in lux)
print('attack_speed' not in lux)
print('health' not in lux)
print(len(lux))


list1 = list(input().split())
list2 = list(map(float, input().split()))
dict1 = dict(zip(list1, list2))
print(dict1)
