<h1 align="center">Brain Games</h1>
<h2 align="center">
 
<a href="https://codeclimate.com/github/shhama/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/cf71ff52c98e562d0f05/maintainability" /></a>

</h2>

<p align="center">

---

## Description

Brain-games - includes 5 simple games. Which are somehow connected with mathematical operations. The difficulty increases with each game.

---

## Requirements
[Python](https://www.python.org) - ^3.10

[Poetry](https://python-poetry.org) - ^1.3.1

---

## Installation

### ***For developers:***
- **install** the current version with [Github](https://github.com/shhama/python-project-50):
```
git clone git@github.com:shhama/python-project-50.git
```
- **select** root directory:
```
cd python-project-49
```
- **Install** dependencies from [pyproject.toml](https://github.com/shhama/python-project-49/blob/main/pyproject.toml):
```
poetry install --dev
```
- **assemble** the package:
```
make build
```
- **install** it:
```
make package-install
```
### ***For users:***
- **Install** the latest version from the repository:
```
python3 -m pip install --user git+https://github.com/shhama/python-project-49
```

---

### ***Linter check:***
- Run the command:
```
make lint
```

---


## ***Games:***

### 1. ***Brain_even***
The essence of the game is as follows: the user is shown a random number. And he needs to answer yes if the number is even, or no if it is odd
```
brain-even
```
[![asciicast](https://asciinema.org/a/qwidBcBWaFaSCPKEaTLSCjBXI.svg)](https://asciinema.org/a/qwidBcBWaFaSCPKEaTLSCjBXI)
 
### 2. ***Brain_calc***
The essence of the game is as follows: the user is shown a random mathematical expression, for example 35 + 16, which must be calculated and the correct answer written down.
```
brain-calc
```
[![asciicast](https://asciinema.org/a/X7lHeoCC3zcLgMzQtzyBwUYM9.svg)](https://asciinema.org/a/X7lHeoCC3zcLgMzQtzyBwUYM9)
 
### 3. ***Brain_gcd***
The essence of the game is as follows: the user is shown two random numbers, for example, 25 50. The user must calculate and enter the greatest common divisor of these numbers.
```
brain-gcd
```
[![asciicast](https://asciinema.org/a/CnTP5fXIMU3iw2Ko2mucanWzD.svg)](https://asciinema.org/a/CnTP5fXIMU3iw2Ko2mucanWzD)

### 4. ***Brain-progression***
We show the player a series of numbers that form an arithmetic progression, replacing any of the numbers with two dots. The player must determine this number.
```
brain-progression
```
[![asciicast](https://asciinema.org/a/mN1xdvpmwsxUzYzuOAhQM33dA.svg)](https://asciinema.org/a/mN1xdvpmwsxUzYzuOAhQM33dA)

### 5. ***Brain_prime***
The player is given a number. He, in turn, must guess whether it is simple.
```
brain-prime
```
[![asciicast](https://asciinema.org/a/AseLFKrAppuvCnKARq3VIzOZm.svg)](https://asciinema.org/a/AseLFKrAppuvCnKARq3VIzOZm)
 
