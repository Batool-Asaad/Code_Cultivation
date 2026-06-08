# Code Cultivation 🌱

Object-Oriented Garden Systems

> A Python project from the 42 curriculum focused on Object-Oriented Programming, software architecture, encapsulation, inheritance, and scalable system design through a digital garden ecosystem.

---

# Overview

`Code Cultivation` is an advanced Python project from the 42 curriculum designed to introduce Object-Oriented Programming (OOP) concepts through practical garden management simulations.

The project progressively evolves from:
- basic Python program structure
- variables and functions
- classes and objects
- encapsulation
- constructors
- inheritance
- scalable system architecture
- data analysis

Each exercise builds on previous concepts to create a complete digital garden ecosystem.

---

# Project Objectives

The project focuses on teaching:

- Python program structure
- Object-Oriented Programming
- reusable software components
- data encapsulation
- constructors and initialization
- inheritance and specialization
- scalable code architecture
- data integrity protection
- analytical thinking

According to the official subject, the project aims to simulate real-world systems through modular software design. 

---

# Technologies Used

- Python 3.10+
- flake8
- mypy
- Object-Oriented Programming

---

# General Rules

The project follows strict Python standards:

- Python 3.10+
- flake8 compliance
- type hints required
- PascalCase for classes
- snake_case for functions & variables
- one exercise per directory
- programs must run without errors


---

# Project Structure

```bash
CodeCultivation/
├── ex0/
│   └── ft_garden_intro.py
│
├── ex1/
│   └── ft_garden_data.py
│
├── ex2/
│   └── ft_plant_growth.py
│
├── ex3/
│   └── ft_plant_factory.py
│
├── ex4/
│   └── ft_garden_security.py
│
├── ex5/
│   └── ft_specialized_plants.py
│
├── ex6/
│   └── ft_garden_analytics.py
│
└── README.md
```

---

# Exercise 0 — Planting Your First Seed

## File

```bash
ft_garden_intro.py
```

## Concepts Learned

- program execution flow
- variables
- print()
- `if __name__ == "__main__"`
- Python script execution

## Objective

Create a simple executable Python program displaying plant information.

This exercise introduces:
- how Python programs start
- execution entry points
- script organization
- direct execution behavior

---

## Understanding `if __name__ == "__main__"`

One of the most important concepts introduced in this exercise is:

```python
if __name__ == "__main__":
```

This condition ensures:
- code executes only when the file runs directly
- imported modules do not automatically execute test code

This becomes fundamental for:
- modular programming
- imports
- reusable software design

---

## Shebang Introduction

The project also introduces the concept of:

```python
#!/usr/bin/env python3
```

The shebang allows:
- executable Python scripts
- direct terminal execution
- interpreter specification

---

# Exercise 1 — Garden Data Organizer

## File

```bash
ft_garden_data.py
```

## Concepts Learned

- classes
- objects
- attributes
- methods
- object instantiation

## Objective

Create a `Plant` class capable of storing:
- name
- height
- age

Each plant instance represents a separate object with its own data.

---

## Object-Oriented Programming Introduction

This exercise introduces core OOP concepts:

### Class

A blueprint describing how objects should behave.

Example:

```python
class Plant:
```

---

### Object

An instance created from the class.

Example:

```python
rose = Plant()
```

---

### Attributes

Variables stored inside objects.

Example:

```python
self.name
self.height
self.age
```

---

### Methods

Functions attached to objects.

Example:

```python
def show(self):
```

---

# Exercise 2 — Plant Growth Simulator

## File

```bash
ft_plant_growth.py
```

## Concepts Learned

- object behavior
- state modification
- simulation systems
- methods updating internal data

## Objective

Simulate plant growth over time using:
- `grow()`
- `age()`

The plant changes dynamically over multiple days.

---

## State Management

This exercise introduces the concept of object state.

A plant object stores mutable data:
- height changes
- age increases
- growth evolves over time

This models real-world entities using software objects.

---

## Simulation Logic

Growth systems demonstrate:
- iterative processing
- temporal simulation
- evolving object states

Example:

```python
for day in range(7):
```

---

# Exercise 3 — Plant Factory

## File

```bash
ft_plant_factory.py
```

## Concepts Learned

- constructors
- object initialization
- reusable initialization logic

## Objective

Create plants directly with initial values using constructors.

---

## Constructors

This exercise introduces:

```python
def __init__(self):
```

Constructors automatically initialize objects during creation.

Example:

```python
rose = Plant("Rose", 25, 30)
```

Advantages:
- cleaner object creation
- reusable initialization
- scalable architecture
- easier maintenance

---

# Exercise 4 — Garden Security System

## File

```bash
ft_garden_security.py
```

## Concepts Learned

- encapsulation
- protected attributes
- getters and setters
- validation systems
- data integrity

## Objective

Protect plant data from invalid modifications.

---

## Encapsulation

Encapsulation restricts direct access to internal object data.

Instead of modifying attributes directly:

```python
plant.height = -50
```

Safe methods are used:

```python
plant.set_height(25)
```

---

## Data Validation

Validation ensures:
- no negative height
- no negative age
- consistent object state

This introduces defensive programming concepts.

---

## Getters & Setters

### Getter

Provides controlled access to data.

Example:

```python
get_height()
```

---

### Setter

Controls modifications safely.

Example:

```python
set_height()
```

---

# Exercise 5 — Specialized Plant Types

## File

```bash
ft_specialized_plants.py
```

## Concepts Learned

- inheritance
- subclassing
- method overriding
- specialization

## Objective

Create specialized plant types inheriting from the base `Plant` class.

Examples:
- Flower
- Tree
- Cactus

---

## Inheritance

Inheritance allows one class to reuse another class.

Example:

```python
class Flower(Plant):
```

Advantages:
- code reuse
- cleaner architecture
- reduced duplication
- scalable systems

---

## Method Overriding

Child classes can redefine behavior.

Example:
- cactus grows slowly
- sunflower grows rapidly

This introduces polymorphic behavior.

---

# Exercise 6 — Garden Analytics

## File

```bash
ft_garden_analytics.py
```

## Concepts Learned

- data aggregation
- statistics
- collection processing
- analytical programming

## Objective

Analyze multiple plants and generate garden statistics.

Possible calculations:
- average height
- oldest plant
- total plants
- growth summaries

---

## Analytical Systems

This exercise demonstrates:
- iterating over collections
- extracting insights from data
- building scalable analytics systems

It introduces real-world software engineering patterns used in:
- dashboards
- monitoring systems
- data science pipelines

---

# Object-Oriented Concepts Covered

| Concept | Exercise |
|---|---|
| Classes & Objects | ex1 |
| Methods | ex1 |
| State Management | ex2 |
| Constructors | ex3 |
| Encapsulation | ex4 |
| Validation | ex4 |
| Inheritance | ex5 |
| Polymorphism | ex5 |
| Analytics | ex6 |

---

# Python Standards

## flake8

The project follows PEP8 formatting standards.

Install:

```bash
pip install flake8
```

Run:

```bash
flake8 .
```

---

## mypy

Type annotations are required.

Install:

```bash
pip install mypy
```

Run:

```bash
mypy .
```

---

# Running the Project

Run individual exercises:

```bash
python3 ex0/ft_garden_intro.py
```

```bash
python3 ex1/ft_garden_data.py
```

```bash
python3 ex2/ft_plant_growth.py
```

---

# Educational Philosophy

The project uses community gardens as a metaphor for software systems.

Just like gardens:
- software systems evolve over time
- components interact together
- organization matters
- scalability requires planning
- protection ensures stability

This transforms abstract OOP concepts into practical and intuitive examples.

---

# Skills Developed

Through this project, students practice:

- Object-Oriented Programming
- software architecture
- abstraction
- encapsulation
- inheritance
- reusable code design
- simulation systems
- defensive programming
- analytical thinking
- scalable design principles

---

# Resources

## Documentation

- Python Official Documentation
- PEP8 Style Guide
- mypy Documentation
- Object-Oriented Programming Guides

## Useful Links

- https://docs.python.org/3/
- https://peps.python.org/pep-0008/
- https://mypy.readthedocs.io/
- https://realpython.com/python3-object-oriented-programming/

---

# AI Usage

AI tools were used for:
- understanding OOP concepts
- reviewing software architecture ideas
- improving explanations
- refining documentation

All implementations, debugging, testing, and architectural decisions were completed manually and fully understood.

---

# What I Learned

`Code Cultivation` transformed Python from simple scripting into structured software engineering.

Through this project, I learned:
- how Object-Oriented Programming works
- how to design reusable systems
- how encapsulation protects data
- how inheritance improves scalability
- how software architecture evolves
- how real-world systems can be modeled using classes

This project provided a strong foundation for future work in:
- backend development
- software engineering
- system design
- data modeling
- scalable Python applications
