# README — Hogwarts Project 🧙‍♂️

## 1. General Presentation

**Project Title**  
Hogwarts Project: *The Art of Coding like a Wizard*

**Description**  
This project is an interactive **Python** adventure game developed as part of the **TI101I – Programming in Python** course. It is inspired by the *Harry Potter* universe and allows the player to experience the life of a Hogwarts student through a multi-chapter storyline.

The game is entirely text-based and runs in the terminal. It applies core programming concepts studied during the course, including functions, conditions, loops, data structures, and JSON file manipulation.

**Authors**  
- Cerqueda Lastovkina Luca  
- Darkova Dina  

Supervisor: *Cherifa Ben Khelil*

---

## 2. Installation

1. Clone the GitHub repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd hogwarts
```

No external libraries are required. The project runs with **Python 3.x**.

---

## 3. Usage

To launch the game:

```bash
python main.py
```

A main menu will appear, allowing the player to start the adventure from Chapter 1.

---

## 4. Main Features

- Character creation with customizable attributes
- Money, inventory, and spell management
- Automatic Hogwarts house assignment
- Narrative interactions influencing character attributes
- Random spell learning system
- Magic quiz affecting house points
- Quidditch match simulation or final scenario

---

## 5. Project Structure

```
hogwarts/
│
├── main.py
├── menu.py
│
├── universe/
│   ├── character.py
│   └── house.py
│
├── chapters/
│   ├── chapter_1.py
│   ├── chapter_2.py
│   ├── chapter_3.py
│   ├── chapter_4.py
│
├── utils/
│   └── input_utils.py
│
└── data/
    ├── inventory.json
    ├── houses.json
    ├── spells.json
    ├── magic_quiz.json
    └── teams_quidditch.json
```

---

## 6. Logbook

**Task Distribution**  
- Cerqueda Lastovkina Luca: game logic, chapters, universe modules
- Darkova Dina: input management, JSON data, menu system

**Project Timeline**  
- Week 1: project setup and Chapter 1
- Week 2: house management and Chapter 2
- Week 3: Chapter 3 and final scenario
- Week 4: finalization and testing

---

## 7. Control, Testing, and Validation

**Input Management**  
User inputs are validated using dedicated utility functions to prevent invalid or out-of-range values.

**Testing Performed**  
- Full walkthrough of each chapter
- Verification of inventory and money management
- Validation of house point calculations

**Known Bugs**  
- No blocking bugs identified at this stage.

---

