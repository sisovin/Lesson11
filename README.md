# Lesson 11: Scope

## Learn Python fast with some content ideas

Learning Python is a great choice, especially given your interest in web development, mobile app development, and software engineering. Here are some excellent resources to get you started:

**1. LearnPython.org:** This interactive Python tutorial offers free lessons for beginners. It covers topics like variables, loops, functions, and more. You can even get certified after completing the [`tutorials[1]`](https://www.learnpython.org/).

**2. Python Official Documentation:** The official Python documentation provides comprehensive information about the language. Start with the Python Tutorial for beginners and explore further as you gain [`confidence[2]`](https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python).

**3. freeCodeCamp’s Python Courses:**
**- [`Full Course for Beginners`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/):** This YouTube course covers programming basics, including lists, conditionals, strings, and small projects like a calculator and a guessing game.
**- [`The Ultimate Python Beginner’s Handbook`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/)** Dive deeper into Python concepts and explore its growing popularity [`3`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) and [`4`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/).

**REMEMBER:** practice coding regularly, work on small projects, and explore real-world examples.

## What is scope in Python?

In Python, scope refers to the region of a program where a particular variable is accessible. There are four types of scopes in Python:

1. **Local Scope**: The scope of variables defined inside a function. These variables are accessible only within the function.
2. **Enclosing Scope**: The scope of variables in the nearest enclosing function, which is relevant for nested functions.
3. **Global Scope**: The scope of variables defined at the top level of a script or module, or declared global using the `global` keyword. These variables are accessible throughout the module.
4. **Built-in Scope**: The scope of built-in names like `print`, `len`, etc., which are always available in Python.

The LEGB rule (Local, Enclosing, Global, Built-in) determines the order in which these scopes are checked when resolving variable names.

### What is the purpose of using the global keyword in Python?

The `global` keyword in Python is used to declare that a variable inside a function refers to a global variable, i.e., a variable that is defined outside of the function. This allows the function to modify the global variable directly, rather than creating a local variable with the same name.

In the provided code, the `global` keyword is used to indicate that the [`count`] variable inside the [`another`] function refers to the [`count`] variable defined at the top level of the script. This allows the function to increment the global [`count`] variable.

Here is a breakdown of its usage in the code:

```python
def another():
  global count  # This tells Python that we are referring to the global 'count' variable
  count += 1    # Increment the global 'count' variable
  print(count)  # Print the updated value of the global 'count' variable
```

Without the `global` keyword, `count` would be treated as a local variable within the `another` function, and the increment operation would not affect the global `count` variable.

### What is the purpose of using the nonlocal keyword in Python?

The `nonlocal` keyword in Python is used to declare that a variable inside a nested function refers to a variable in the nearest enclosing scope that is not global. This allows the nested function to modify the variable in the enclosing scope.

In the provided code, the `nonlocal` keyword is used to indicate that the [`color`] variable inside the [`greeting`] function refers to the [`color`] variable defined in the [`another`] function. This allows the [`greeting`] function to modify the [`color`] variable in the [`another`] function's scope.

Here is a breakdown of its usage in the code:

```python
def another():
  color = "blue"  # Variable in the enclosing scope
  global count
  count += 1
  print(count)

  def greeting(name):
    nonlocal color  # This tells Python that we are referring to the 'color' variable in the enclosing scope
    color = "red"   # Modify the 'color' variable in the enclosing scope
    print(color)    # Print the updated value of 'color'
    print(name)     # Print the name passed to the function

  greeting("Sisovin")

another()
```

Without the `nonlocal` keyword, `color` would be treated as a local variable within the `greeting` function, and the assignment `color = "red"` would not affect the `color` variable in the `another` function's scope.

### What are the differences between local, global, and nonlocal variables in Python?

In Python, local, global, and nonlocal variables differ in terms of their scope and where they can be accessed or modified:

1. **Local Variables**:

   - **Definition**: Variables defined inside a function.
   - **Scope**: Accessible only within the function where they are defined.
   - **Example**:
     ```python
     def my_function():
         local_var = 10  # Local variable
         print(local_var)
     my_function()
     # local_var is not accessible here
     ```

2. **Global Variables**:

   - **Definition**: Variables defined at the top level of a script or module, or declared global using the `global` keyword inside a function.
   - **Scope**: Accessible throughout the module.
   - **Example**:

     ```python
     global_var = 20  # Global variable

     def my_function():
         global global_var
         global_var += 5  # Modify the global variable
         print(global_var)
     my_function()
     print(global_var)  # Accessible here
     ```

3. **Nonlocal Variables**:

   - **Definition**: Variables defined in the nearest enclosing scope that is not global, typically in nested functions.
   - **Scope**: Accessible and modifiable within nested functions.
   - **Example**:

     ```python
     def outer_function():
         nonlocal_var = 30  # Enclosing scope variable

         def inner_function():
             nonlocal nonlocal_var
             nonlocal_var += 5  # Modify the enclosing scope variable
             print(nonlocal_var)
         inner_function()
         print(nonlocal_var)  # Modified value is accessible here
     outer_function()
     ```

### Summary:

- **Local variables** are confined to the function they are defined in.
- **Global variables** are accessible throughout the module and can be modified inside functions using the `global` keyword.
- **Nonlocal variables** are used in nested functions to refer to variables in the nearest enclosing scope that is not global, allowing modification of those variables.

**Explanation:**
Certainly! Let's break down the code step-by-step:

1. **Global Variables:**

   ```python
   name = "Sisovin"
   count = 1
   ```

   - [`name`] is a global variable initialized with the string `"Sisovin"`.
   - [`count`] is a global variable initialized with the integer `1`.

2. **Function Definition:**

   ```python
   def another():
   ```

   - This defines a function named [`another`].

3. **Local Variable and Global Keyword:**

   ```python
   color = "blue"
   global count
   count += 1
   print(count)
   ```

   - Inside the [`another`] function, a local variable [`color`] is initialized with the string `"blue"`.
   - The `global` keyword is used to indicate that the [`count`] variable refers to the global [`count`] variable.
   - The global [`count`] variable is incremented by `1`.
   - The updated value of [`count`] is printed.

4. **Nested Function Definition:**

   ```python
   def greeting(name):
   ```

   - Inside the [`another`] function, a nested function named [`greeting`] is defined, which takes a parameter [`name`].

5. **Nonlocal Keyword and Variable Modification:**

   ```python
   nonlocal color
   color = "red"
   print(color)
   print(name)
   ```

   - Inside the [`greeting`] function, the `nonlocal` keyword is used to indicate that [`color`] refers to the [`color`] variable in the enclosing [`another`] function.
   - The [`color`] variable is modified to `"red"`.
   - The updated value of [`color`] is printed.
   - The [`name`] parameter passed to the [`greeting`] function is printed.

6. **Calling the Nested Function:**

   ```python
   greeting("Sisovin")
   ```

   - The [`greeting`] function is called with the argument `"Sisovin"`.

7. **Calling the Outer Function:**
   ```python
   another()
   ```
   - The [`another`] function is called.

**Execution Flow:**

- When [`another()`] is called:
  - [`color`] is set to `"blue"`.
  - [`count`] is incremented from `1` to `2` and printed.
  - [`greeting("Sisovin")`] is called:
    - [`color`] is changed to `"red"` and printed.
    - The string `"Sisovin"` is printed.

**Output:**

```
2
red
Sisovin
```

This code demonstrates the use of global and nonlocal keywords to modify variables in different scopes.

**Code Break Down**
Let’s break down the code and understand how recursive functions and scopes are working in this Rock, Paper, Scissors (RPS) game:

**1. Function Definitions:**

- play_rps(): This is the main function that runs the entire game. It contains the game loop, user input handling, and calls other functions.
- decide_winner(player, computer): This function determines the winner based on the player’s and computer’s choices.

**2. Scopes and Variables:**

- The variable game_count is defined outside any function, making it a global variable. It keeps track of the number of games played.
- Inside play_rps(), local variables like playagain, playerchoice, player, computerchoice, and computer are used to manage game state.
- The decide_winner() function has its own local scope with parameters player and computer.

**3. Recursion:**

- The game loop in play_rps() runs as long as playagain is True. When the user chooses to play again (playagain.lower() == "y"), the function calls itself recursively.
- The recursive call happens here: return play_rps().
- Recursion allows the game to continue until the user decides to quit.

**4. Enum:**

- The RPS enum class defines three constants: ROCK, PAPER, and SCISSORS.
- These constants represent the player’s and computer’s choices.

**5. User Interaction:**

- The game displays a menu with options for the user to choose (rock, paper, or scissors).
- The user’s choice is validated, and the game proceeds accordingly.
- The winner is determined using the decide_winner() function.

**6. Game Result and Count:**

- The game result is printed (game_result) based on the player’s and computer’s choices.
- The global game_count is incremented after each game.

**7. Exiting the Game:**

- If the user chooses not to play again (playagain.lower() != "y"), the game - prints a farewell message and exits.

**Overall,** this code demonstrates how recursion can be used to create a simple game loop, manage game state, and allow repeated gameplay. The decide_winner() function encapsulates the logic for determining the winner based on the choices made by the player and the computer. Feel free to explore and modify the code to enhance the game or add additional features! 😊🎮🪁
