<!-- Hexlet logo -->
<a id="anchor-top"></a>
<div align="center"
      style="display: flex; flex: 1;
            flex-wrap: wrap; flex-direction: column; 
            margin: 0; margin-bottom: 25px">
  <a href="https://ru.hexlet.io/" style="color: black">
    <img src="images/hexlet_logo_full.svg" 
          alt="Logo" 
          width="210" height="60"
          style="display: flex; flex-wrap: wrap; margin: 6px"> 
  </a>
  <p style="display: flex; flex: 1; 
            flex-wrap: wrap; justify-content: center; 
            margin: 0; color: #1100A0 !important;
            font-weight: 500; letter-spacing: 1px;">hands-on programming courses</p>
</div>

<!-- Hexlet header -->
<a href="https://ru.hexlet.io/" style="color: black">
  <img src="images/hexlet_background.jpg" 
        alt="Hexlet header image" 
        width="auto" height="auto"
        style="display: flex; flex-wrap: wrap; max-width: 100%; border-radius: 50% !important;"> 
</a>


### Hexlet tests, linter and Code Climate status:
[![Actions Status](https://github.com/bazarovstas/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/bazarovstas/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/5d6e3363a9f1e31f303f/maintainability)](https://codeclimate.com/github/bazarovstas/python-project-49/maintainability)  


<!-- Main page -->
## Table of contents  
**[1. The Brain Games](#the-brain-games)**  
**[- 1.1 Even Game](#even-game)**  
**[- 1.2 Calc Game](#calc-game)**  
**[- 1.3 GCD Game](#gcd-game)**  
**[- 1.4 Progressive Game](#progressive-game)**  
**[- 1.5 Prime Game](#prime-game)**    
**[2. Tech Stack](#tech-stack)**    
**[3. Installation](#installation)**    
**[4. Usage](#usage)**    
**[5. Reinstall](#reinstall)**    


# The Brain Games  
Brain Games is a set of 5 logic puzzles that let you test how smart you are:

|Game|Question|Example|
|---|---|--:| 
| The Even Game | Answer "yes" if the number is even, otherwise answer "no" | 44 |
| The Calc Game | What is the result of the expression? | 7 + 11 |
| The GCD Game | Find the greatest common divisor of given numbers | 10 90 |  
| The Progressive Game | What number is missing in the progression? | 3 7 .. 15 |
| The Prime Game | Answer "yes" if given number is prime. Otherwise answer "no" | 21 |

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>

## Even Game  
This demo of the even game shows the game process:  
[![asciicast](https://asciinema.org/a/687407.svg)](https://asciinema.org/a/687407)

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>

## Calc Game
This demo of the calc game shows the game process:  
[![asciicast](https://asciinema.org/a/687410.svg)](https://asciinema.org/a/687410)

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>

## GCD Game
This demo of the gcd game shows the game process:  
[![asciicast](https://asciinema.org/a/687411.svg)](https://asciinema.org/a/687411)

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>

## Progressive Game
This demo of the progressive game shows the game process:  
[![asciicast](https://asciinema.org/a/687412.svg)](https://asciinema.org/a/687412)

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>

## Prime Game
This demo of the prime game shows the game process:  
[![asciicast](https://asciinema.org/a/687413.svg)](https://asciinema.org/a/687413)

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>


## Tech Stack  
![Static Badge](https://img.shields.io/badge/python-3.12-ffde57?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/poetry-1.8.4-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/pip-24.3.1-f0efe0?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/prompt-0.4.1-green?style=for-the-badge)

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>


## Installation
The installation is simple and does not take much time

**1. Installing pipx**

If you don't have a python 3.8+ than is required to install pipx:  
  * Ubuntu:  
  ```
  sudo apt install pipx
  ```
  * Using pip:
  ```
  python3 -m pip install --user pipx
  ```
  * Or on Windows via Scoop:  
  ```
  scoop install pipx
  ```

**2. Install Poetry**

If pipx is already installed, you can install poetry:
  ```
  pipx install poetry
  ```
  add pyproject.toml to project folder:
  ```
  poetry new project_name
  ```
  or in pre-populated directory:
  ```
  poetry init
  ```
  and the last thing in this step, install virtual environment:
  ```
  poetry install
  ```

**3. Repository**

Visit GitHub at the following link: https://github.com/bazarovstas/python-project-49  
and finnaly, enter the following command in the CLI:
  ```
  poetry add git+ssh://git@github.com:bazarovstas/python-project-49.git
  ```

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>


## Usage  
you can use scripts from the Makefile by installing the package, or use poetry scripts without installing anything:
  * Poetry:  
  ```
  poetry run brain-even
  poetry run brain-calc
  poetry run brain-gcd
  poetry run brain-progression
  poetry run brain-prime
  ```
  * Scripts:  
generate a distributive and install them:
  ```
  make build
  make package-install
  ```
  use one of the following commands to run a specific game:  
  ```
  brain-even
  brain-calc
  brain-gcd
  brain-progression
  brain-prime
  ```

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>


## Reinstall  
  to reinstall the package, use the following command:  
  ```
  make package-reinstall
  ```

<p align="right">[<a href="#anchor-top" style="color: black">BACK TO TOP</a>]</p>

<!-- Hexlet footer -->
<div align="center"
      style="display: flex; flex: 1;  
      flex-wrap: wrap; flex-direction: column; 
      margin: 0; margin-top: 20px;">
  <a href="https://ru.hexlet.io/" style="color: black">
    <img src="images/hexlet_background.png" 
          alt="Hexlet footer image" 
          width="auto" height="auto"
          style="display: flex; flex-wrap: wrap; border-radius: 25%"> 
  </a>
</div>
