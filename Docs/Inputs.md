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
- Winning amount: "gainsPlace", int

## Things in the dataset I don't what it is
- "rapport", float
- "nombrePlaces", int
- "nombreIndicateurTendance", float
- "engagement", bool
- "driverChange", bool

## We need to calculate
- Number of races ran with this jockey
