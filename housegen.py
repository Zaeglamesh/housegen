import random

respect = {
	'an ancient and well-respected by all houses, great and small',
	'an ancient and greatly diminished in standing from what it once was',
	'an old with the respect of many houses, great and small',
	'an old and struggling to maintain respect of other houses',
	'an old but often overshadowed by other houses',
	'a newly raised up to the nobility'
}

colors = {
	'black',
	'red',
	'gold',
	'forest green',
	'royal blue',
	'violet',
	'silver',
	'bronze',
	'tan',
	'brown',
	'dark grey',
	'white',
	'maroon',
	'sky blue',
	'navy blue',
	'dark brown',
	'teal',
	'yellow',
	'orange',
	'olive green'
}

symbols = {
	'Weapon': {
		'symbol': ['arrow', 'axe', 'dagger', 'hammer', 'mace', 'spear', 'staff', 'sword']
	},
	'Armor': {
		'symbol': ['breastplate', 'gauntlet', 'helmet', 'shield']
	},
	'Celestial Body': {
		'symbol': ['sun', 'moon', 'star', 'comet']
	},
	'Plant': {
		'symbol': ['apple', 'barely', 'briar', 'fig', 'grapes', 'lily', 'maple', 'oak', 'olive', 'pine', 'rose', 'wheat']
	},
	'Aquatic Beast': {
		'symbol': ['crab', 'crocodile', 'frog', 'fish', 'octopus', 'whale']
	}	,
	'Small Beast': {
		'symbol': ['badger', 'bat', 'beaver', 'dog', 'ferret', 'fox', 'hedgehog', 'lizard', 'rat', 'scorpion', 'snake', 'spider']
	},
	'Great Beast': {
		'symbol': ['bear', 'boar', 'bull', 'dragon', 'lion', 'ox', 'stag', 'wolf']
	},
	'Bird': {
		'symbol': ['cardinal', 'dove', 'eagle', 'hawk', 'mockingbird', 'owl', 'pelican', 'raven', 'rooster', 'sparrow', 'swan', 'vulture']
	}
}

motto = {
	'compassion',
	'courage',
	'courtesy',
	'determination',
	'discipline',
	'duty',
	'excellence',
	'faith',
	'generosity',
	'honor',
	'hope',
	'integrity',
	'justice',
	'loyalty',
	'mercy',
	'patience',
	'righteousness',
	'strength',
	'trust',
	'wisdom'
}

known = {
	'a gallant knight',
	'a beatiful woman',
	'a rutheless negotiator',
	'an adept diplomat',
	'a famous traveler or explorer'
	'a brilliant military strategist',
	'a notorious rebel or outlaw',
	'a dashing swashbuckler',
	'a fearsome warrior',
	'a brilliant scholar',
	'a gifted orator',
	'a dangerous and mad ruler'
}

head = {
	'a kindly old man or woman',
	'a ruthless old man or woman',
	'a wily old man or woman',
	'a charming man or woman',
	'a grim veteran of wars'
	'an astute politician',
	'a devout adherent of a religion',
	'a heartbroken widower or widow'
	'a reckless or hot-headed young man or woman',
	'a child'
}

goals = {
	'support the king\'s top priority plan of': {
		'goal': ['expansion', 'expansion', 'warfare', 'diplomacy', 'diplomacy', 'rooting out dissidents']
	},
	'advance the church'
	'acquire more land with a': {
		'goal': ['strategic location', 'strategic location', 'valuable resource', 'valuable resource', 'valuable resource', 'special feature']
	},
	'dispose of': {
		'goal': ['another noble', 'another noble', 'non-secular official', 'military officer', 'high-level bureaucrat', 'powerful adventurer']
	},
	'marry into a particular family for': {
		'goal': ['wealth', 'love', 'political advantage', 'political advantage', 'lust', 'nefarious purposes']
	},
	'bring about political reform'
	'bring local outlaws to justice'
	'build a fortification in the form of a': {
		'goal': ['defensive wall', 'defensive wall', 'defensive wall', 'tower', 'tower', 'keep']
	},
	'establish a new settlement'
	'build infrastructure': {
		'goal': ['road', 'road', 'bridge', 'watch tower', 'signal beacon', 'folly']
	},
	'clear stain on family name'
	'make a name for the family via': {
		'goal': ['adventuring or exploring', 'adventure or exploring', 'amassing wealth', 'amassing wealth', 'military conquest', 'political influence']
	}
}

secrets = {
	'how they engaged in treasonous activity with': {
		'secret': ['an independent', 'an official body', 'an official body', 'a foreign power', 'a foreign power', 'a dissident element']
	},
	'how they perpetrated an covered up a capital crime'
	'how they\'re under the enchantment of a': {
		'secret': ['curseditem', 'cursed item', 'sorcerer', 'demon', 'fey creature', 'geas spell']
	},
	'how they manipulates the system to avoid military service'
	'how they support a band of': {
		'secret': ['outlaws', 'outlaws', 'outlaws', 'humanoids', 'organized thieves', 'dangeours mercenaries']
	},
	'how they withhold the king\'s fees to': {
		'secret': ['amass personal hoard', 'amass personal hoard', 'divert funds', 'divert funds', 'cover gambling debts', 'pay an extortionist']
	},
	'how they sideline a poacher of': {
		'secret': ['fish & game', 'fish & game', 'a natural resource', 'anatural resource', 'anatural resource', 'a valuable commodity']
	},
	'how they\'re afflicted with lycanthropy'
	'how they have a family history of mental illness'
	'how they\'re members of': {
		'secret': ['a death cult', 'a death cult', 'an outlawed profession', 'an outlawed profession', 'seditious faction', 'seditious faction']
	},
	'how they\'re addicted to': {
		'secret': ['an opiate', 'an opiate', 'a hallucinogen', 'a hallucinogen', 'a stimulant', 'an exotic drug']
	}
}

seat = {
	'a port city',
	'a range of mountains',
	'a wide, fertile plain',
	'a fertile river valley',
	'an ancient forest',
	'a jagged coastline',
	'a sodden swamp',
	'a pristine lake',
	'a desert plateau',
	'an idyllic hill country'
}

influence = {
	'no',
	'scant',
	'marginal',
	'average',
	'significant',
	'considerable'
}

holdings = {
	'modest': {
		'hexes': ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50']
	},
	'modest': {
		'hexes': ['5', '10', '15', '20', '25', '30', '35', '40', '45', '50']
	},
	'appreciable': {
		'hexes': ['55', '60', '65', '70', '75', '80', '85', '90', '95', '100']
	},
	'appreciable': {
		'hexes': ['55', '60', '65', '70', '75', '80', '85', '90', '95', '100']
	},
	'appreciable': {
		'hexes': ['55', '60', '65', '70', '75', '80', '85', '90', '95', '100']
	},
	'extensive': {
		'hexes': ['105', '110', '115', '120', '125', '130', '135', '140', '145', '150']
	}
}

family = {
	'small': {
		'size': ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
	},
	'small': {
		'size': ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
	},
	'medium': {
		'size': ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
	},
	'medium': {
		'size': ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
	},
	'medium': {
		'size': ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
	},
	'huge': {
		'size': ['14', '15', '16', '16', '17', '18', '19', '20', '21', '22', '23', '24']
	}
}

respectChoice = random.choice(list(respect))
colorChoice1 = random.choice(list(colors))
colorChoice2 = random.choice(list(colors))
colorChoice3 = random.choice(list(colors))
symbolCategoryChoice = random.choice(list(symbols))
symbolChoice = random.choice(list(symbols[symbolCategoryChoice]['symbol']))
mottoChoice = random.choice(list(motto))
knownChoice = random.choice(list(known))
headChoice = random.choice(list(head))
goalsCategoryChoice = random.choice(list(goals))
goalsChoice = random.choice(list(goals[goalsCategoryChoice]['goal']))
secretCategoryChoice = random.choice(list(secrets))
secretChoice = random.choice(list(secrets[secretCategoryChoice]['secret']))
seatChoice = random.choice(list(seat))
influenceChoice = random.choice(list(influence))
holdingsCategoryChoice = random.choice(list(holdings))
holdingsChoice = random.choice(list(holdings[holdingsCategoryChoice]['hexes']))
familyCategoryChoice = random.choice(list(family))
familyChoice = random.choice(list(family[familyCategoryChoice]['size']))


print('The house is', respectChoice + ', known for', knownChoice, 'and now lead by', headChoice + '.', 'The house\'s emblem is a', colorChoice1, symbolChoice, 'on a', colorChoice2, 'and', colorChoice3, 'background.', 'Their motto is', mottoChoice + '.', 'Their seat of power is located in', seatChoice, 'where they have', influenceChoice, 'influence', 'and a', familyCategoryChoice, 'sized family of', familyChoice, 'people on', holdingsChoice, 'miles of land.', 'Their current goal is to', goalsCategoryChoice, goalsChoice, 'and making sure no one finds out about', secretCategoryChoice, secretChoice + '.')