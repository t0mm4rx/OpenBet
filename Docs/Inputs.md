# What inputs to choose from the data we get ?

We have one neural network per runner, here are some ideas of inputs.

## In the dataset
- Handicap: 'handicapValeur', int
- Musique: 'musique', list of last positions, need to define a function to convert that in float
- Is the horse pregnant ? : 'jumentPleine', bool
- Rope number: "placeCorde", int
- Age: "age", int
- Number of ran races: "nombreCourses", int
- Victory number: "nombreVictoires", int
- Has the horse never run before ?: "indicateurInedit", bool
- Favorite ?: "favoris", bool
- Tendence ?: "indicateurTendance", +, -, or =
- Blinker type: "oeilleres", need to establish a list of possible values
- Terrain id, class, need to find a way to normalize it

## Things in the dataset I don't what it is
- "rapport", float
- "nombrePlaces", int
- "nombreIndicateurTendance", float
- "engagement", bool
- "driverChange", bool
- "numPmu", int

## Race data
- Total money given: "montantTotalOffert", int
- Money given to 5th: "montantOffert5eme", int
- Money given to 4th: "montantOffert4eme", int
- Money given to 3rd: "montantOffert3eme", int
- Money given to 1st: "montantOffert1er", int
- Number of runners: "nombreDeclaresPartants", int
- Distance: "distance", int
- Field type, "typePiste", class
- Audience: "audience", class
- Wind force: "forceVent", int
- Temperature: "temperature", int
- Period of the day: "nature", class
- Side of the rope: "corde", binary class

## We need to calculate
- Number of races ran with this jockey
- Jockey score
