amarPets = ['Abigail', 'Ace', 'Adam', 'Addie', 'Admiral', 'Aggie', 'Aires', 'Aj', 'Ajax', 'Aldo', 'Alex', 'Alexus', 'Alf', 'Alfie', 'Allie', 'Ally', 'Amber', 'Amie', 'Amigo', 'Amos', 'Amy', 'Andy', 'Angel', 'Angus', 'Annie', 'Apollo', 'April', 'Archie', 'Argus', 'Aries', 'Armanti', 'Arnie', 'Arrow', 'Ashes', 'Ashley', 'Astro', 'Athena', 'Atlas', 'Audi', 'Augie', 'Aussie', 'Austin', 'Autumn', 'Axel', 'Axle', 'Babbles', 'Babe', 'Baby', 'Baby-doll', 'Babykins', 'Bacchus', 'Bailey', 'Bam-bam', 'Bambi', 'Bandit', 'Banjo', 'Barbie', 'Barclay', 'Barker', 'Barkley', 'Barley', 'Barnaby', 'Barney', 'Baron', 'Bart', 'Basil', 'Baxter', 'Bb']
print('Whats your pet name?')
petName = input()
if petName in amarPets:
    print('Your Pet ' + petName + ' Is Safe With Us!')
else:
    print('Sorry No Data Found')