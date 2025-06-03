# Smart Recipe Book

University Project – Introductory Programming Course  
Author: Miguel Hernández  
Collaborator: Fernanda Lizzete Rivera  
This repository contains the original project and documentation as delivered for the course.

---

## Overview

**Smart Recipe Book** is a desktop application developed in Python, designed to manage, browse, and learn recipes interactively. The system was created as a final project for my first programming course, preserving the original structure and documentation submitted for academic evaluation.

This project showcases skills in basic programming, data structures, file management, and GUI development in Python.

---

## Key Features

- **Recipe Database**: Add, view, edit, or delete recipes, organized by type (“Learn” and “Normal”).
- **Cooking Module**:  
  - Generate a random menu with 3 recipes.
  - Includes a unit conversion tool for ingredients.
- **Learning Module**:  
  - Step-by-step cooking walkthroughs.
  - Random recipe feature for practice.
  - Interactive quiz game mode (with both basic and advanced levels).

---

## Requirements & Installation

1. **Python**: Make sure you have the latest version of Python installed.
2. **Source Files**: Do not modify or delete any `.py` files or directories inside `Recetario Inteligente DB` to avoid program errors.
3. **Running the Program**:
   - Open and run `Recetario Inteligente.py`.
   - The program will automatically create the necessary directories for storing recipes if they don’t already exist.

---

## How to Use

### Navigation

The system uses a graphical interface with buttons to switch between the three main modules:
- **Recipe Book**
- **Cooking**
- **Learning**

### Recipe Management

- To unlock all features, start by adding recipes to the database from the **Recipe Book** module (`New Recipe`).
- **Type**: Must be exactly “Aprender” or “Normal”.
- **Name**: Maximum 100 characters.
- **Ingredients and Procedure**: Separate each item with a semicolon `;`.
- Recipes are stored internally as JSON dictionaries for application logic.

**Editing or Deleting Recipes:**  
- To edit, re-enter the recipe with the same “Type” and “Name”.
- To delete, remove the relevant files from the database and from the used recipes history folders.

**Sample Recipes:**  
Sample recipes are provided in the `Recetas de prueba` folder. To use them, copy and paste them into the `Aprender` or `Normal` folders inside `Recetario`, which is within `Recetario Inteligente DB`.

### Cooking Module

- **Unit Converter:** Select the type of conversion and amount, then click “Convert”.
- **Random Menu:** Generates a menu using 3 randomly selected “Normal” recipes (requires at least 3 recipes loaded).

### Learning Module

- **Step-by-Step Recipe:** Walks you through a recipe one step at a time.
- **Random Recipe:** Shows a random recipe for practice.
- **Quiz Game:** Answer cooking-related questions in either Junior or Master mode.

---

## Academic and Technical Notes

- This project was submitted as evidence of programming skills, file handling, and basic GUI development in Python.
- The code and structure reflect the standards and requirements of the course at the time of delivery.
- No guarantee of production use or future updates.
- Feel free to explore, improve, or adapt this project for academic purposes.

---

## Credits

Developed by Miguel Hernández  
Collaborator: Fernanda Lizzete Rivera  
University project – [Course name and university, optionally add here]

---

## License

This repository is provided for academic and personal portfolio purposes.
