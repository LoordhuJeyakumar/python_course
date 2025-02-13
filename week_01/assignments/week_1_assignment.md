## Week 1 Assignment: Python Fundamentals - New Problems

**Objective:**

This assignment is designed to comprehensively assess your understanding of Python fundamentals learned in Week 1. It focuses on applying your knowledge of:

- Variables and Data Types
- Operators (Arithmetic, Comparison, Logical, Assignment)
- Input and Output operations
- Conditional Statements (`if`, `elif`, `else`)
- Loops (`for`, `while`)

**Instructions:**

1.  **Solve all five problems described below.** Write a Python program for each problem.
2.  **Write clean, readable, and well-commented code.** Explain your logic within the code using comments to make it easy to understand.
3.  **Thoroughly test your programs.** Use various inputs, including normal cases and potential edge cases, to ensure your code functions correctly in all expected scenarios.
4.  **Organize your solutions.** Create a separate Python file for each problem (e.g., `problem1.py`, `problem2.py`, `problem3.py`, `problem4.py`, `problem5.py`).
5.  **Submit all `.py` files** as your solution. You might be asked to submit them as a ZIP archive. _(Instructor will specify the exact submission method)_.

**Problems:**

**Problem 1: Unit Converter - Length**

Write a Python program to convert length units. The program should:

1.  **Ask the user to choose the input unit** from the following options:
    - 1.  Kilometers (km)
    - 2.  Miles (miles)
    - 3.  Meters (m)
    - 4.  Feet (feet)
          Display these options to the user with numbers for easy selection.
2.  **Take the numerical length value as input** from the user.
3.  **Ask the user to choose the output unit** from the same options (Kilometers, Miles, Meters, Feet) as above.
4.  **Perform the unit conversion** based on the chosen input and output units. Use the following conversion factors:
    - 1 kilometer = 0.621371 miles
    - 1 mile = 1.60934 kilometers
    - 1 meter = 3.28084 feet
    - 1 foot = 0.3048 meters
    - (You can handle direct conversions like km to m, miles to feet, etc. as combinations of these factors, or use more conversion factors if you prefer).
5.  **Print the converted length** in a user-friendly sentence, showing both the original value and unit, and the converted value and unit.

    **Example Interaction:**

    ```
    Choose input unit:
    1. Kilometers
    2. Miles
    3. Meters
    4. Feet
    Enter your choice (1-4): 1
    Enter length in Kilometers: 100
    Choose output unit:
    1. Kilometers
    2. Miles
    3. Meters
    4. Feet
    Enter your choice (1-4): 2
    100.0 Kilometers is equal to 62.1371 Miles.
    ```

**Problem 2: Password Strength Checker (Basic)**

Write a Python program to perform a basic check on the strength of a user-entered password. The program should:

1.  **Ask the user to enter a password.**
2.  **Check the password against the following criteria:**
    - **Minimum length:** Password must be at least 8 characters long.
    - **Contains digits:** Password must contain at least one digit (0-9).
    - **Contains letters:** Password must contain at least one letter (a-z or A-Z).
3.  **Based on the checks, provide feedback to the user:**

    - If the password meets all criteria, print "Password is strong."
    - If the password does not meet a criterion, print specific messages indicating which criteria are not met (e.g., "Password is too short.", "Password must contain at least one digit.", "Password must contain at least one letter."). You can print multiple messages if multiple criteria are not met.

    **Example Interaction:**

    ```
    Enter your password:  WeakPwd
    Password is too short.
    Password must contain at least one digit.

    Enter your password:  StrongPassword123
    Password is strong.

    Enter your password:  NoDigitsOrLetters!
    Password must contain at least one digit.
    Password must contain at least one letter.
    ```

**Problem 3: Average of User Inputs**

Write a Python program that calculates the average of numbers entered by the user. The program should:

1.  **Ask the user how many numbers they want to enter.** Take this count as an integer input.
2.  **Use a loop to repeatedly ask the user to enter each number.** The loop should run for the number of times specified by the user in step 1.
3.  **Keep a running sum of all the numbers entered.**
4.  **After all numbers are entered, calculate the average** by dividing the sum by the count of numbers.
5.  **Print the calculated average** in a user-friendly format.

    **Example Interaction:**

    ```
    How many numbers do you want to average? 4
    Enter number 1: 10
    Enter number 2: 20
    Enter number 3: 30
    Enter number 4: 40
    The average of the 4 numbers is: 25.0
    ```

**Problem 4: Prime Number Checker**

Write a Python program to check if a given number is a prime number. The program should:

1.  **Ask the user to enter a positive integer.**
2.  **Determine if the entered number is a prime number.**
    - A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
    - You can check for divisibility from 2 up to the square root of the number for efficiency, but for simplicity in Week 1, you can check divisibility from 2 up to the number - 1.
3.  **Print a message indicating whether the number is prime or not.**

    **Example Interaction:**

    ```
    Enter a positive integer: 17
    17 is a prime number.

    Enter a positive integer: 20
    20 is not a prime number.

    Enter a positive integer: 2
    2 is a prime number.

    Enter a positive integer: 1
    1 is not a prime number (by definition, prime numbers are greater than 1).
    ```

**Problem 5: Text-Based Adventure - Choose Your Path (Simple)**

Create a very simple text-based adventure starter. The program should:

1.  **Present a scenario to the user.** For example: "You are standing at a crossroads in a dark forest. There are two paths in front of you: one to the left and one to the right."
2.  **Offer the user two choices** as input (e.g., "left" or "right", or "1" for left and "2" for right).
3.  **Based on the user's choice, print a different outcome.**
    - For example, if the user chooses "left", you might print: "You take the left path and find a hidden cave."
    - If the user chooses "right", you might print: "You take the right path and encounter a friendly traveler."
4.  **For each choice, add one more layer of choice and outcome.** So, if they chose "left" and found a cave, you could then ask: "Do you enter the cave (yes/no)?" and provide different outcomes for "yes" and "no." Similarly, for the "right" path, you could offer choices based on encountering the traveler.
5.  **The adventure should have at least two levels of choices** (the initial choice, and then one choice based on each initial path). Keep it very simple for Week 1, focusing on demonstrating `input()` and conditional statements to create branching narratives.

    **Example Interaction (Example scenario only, you can design your own story):**

    ```
    You are standing at a crossroads in a dark forest. There are two paths in front of you: one to the left and one to the right.
    Choose your path (left/right): left
    You take the left path and find a hidden cave.
    Do you enter the cave? (yes/no): yes
    You bravely enter the cave and discover a chest full of gold! Congratulations, you win!

    --- (Another run) ---
    You are standing at a crossroads in a dark forest. There are two paths in front of you: one to the left and one to the right.
    Choose your path (left/right): right
    You take the right path and encounter a friendly traveler.
    Do you talk to the traveler? (yes/no): no
    You ignore the traveler and continue on your way. You reach a dead end and have to turn back. Game Over.
    ```

**Submission Instructions:**

Please submit your Week 1 Assignment via GitHub using Pull Requests. Follow these steps carefully:

1.  **Access your Forked Repository:**

    - You should have already forked the main course repository. Access your forked repository on GitHub. If you haven't forked it yet, please do so now, following the instructions provided by your instructor.

2.  **Navigate to the `assignments` Folder:**

    - In your forked repository, navigate to the existing **`assignments`** folder at the root level.

3.  **Create Your Assignment Folder:**

    - Inside the `assignments` folder, create a new folder named **`[Your Name]-assignment`**, replacing `[Your Name]` with your first name or preferred identifier (e.g., `john-assignment`, `sara-assignment`, `learner123-assignment`). **Use lowercase for your folder name and avoid spaces.**
    - Your folder structure should now look like this:

      ```
      assignments/
          [Your Name]-assignment/
              (Your Python files will go here)
          (Other learner's assignment folders might be here)
      ```

4.  **File Naming and Placement:**

    - For each problem in the Week 1 Assignment, create a separate Python file (`.py`).
    - Name your files according to the problem number (or a descriptive name if you prefer, but problem numbers are recommended for consistency):
      - Problem 1: `Problem1.py` (or `unit_converter.py`, etc.)
      - Problem 2: `Problem2.py` (or `password_checker.py`, etc.)
      - Problem 3: `Problem3.py` (or `average_calculator.py`, etc.)
      - Problem 4: `Problem4.py` (or `prime_checker.py`, etc.)
      - Problem 5: `Problem5.py` (or `text_adventure.py`, etc.)
    - Place these `.py` files inside the folder you created in step 3, **`[Your Name]-assignment`**.

5.  **Code Content:**

    - Ensure each `.py` file contains the Python code for the corresponding problem from the Week 1 Assignment.
    - Make sure your code is well-commented to explain your approach and logic.
    - Test your code thoroughly to verify it works correctly.

6.  **Commit and Push to your Fork:**

    - Using Git commands, **add**, **commit**, and **push** your assignment folder and files to **your forked repository**.
    - From the root of your local repository, you can use commands like:
      - `git add assignments/[Your Name]-assignment/*` (to stage all files in your assignment folder)
      - `git commit -m "Submit Week 1 Assignment - [Your Name]"` (Commit message - replace `[Your Name]` with your identifier)
      - `git push origin main` (or `git push origin master`, depending on your repository setup and branch)
    - Commit regularly as you work on the assignment, not just at the very end.

7.  **Create a Pull Request (PR):**

    - Once you have pushed your `[Your Name]-assignment` folder to your forked repository on GitHub, go to **your forked repository** on the GitHub website.
    - You should see a button to "Create Pull Request" (or "Compare & pull request"). Click this button.
    - Ensure the Pull Request is targeting the **`main`** (or `master`) branch of the **original course repository** (not your fork). GitHub usually defaults to this correctly, but double-check.
    - Give your Pull Request a descriptive title, such as "Submission - Week 1 Assignment - [Your Name]".
    - In the Pull Request description, you can briefly mention what you have submitted or any notes for the instructor (optional).
    - Click "Create Pull Request".

8.  **Submission Confirmation:**

    - After creating the Pull Request, your assignment is submitted. You can verify by checking the Pull Requests tab in the original course repository to see if your PR is listed.

9.  **Deadline: [3 Days]**

    - **Deadline:** Please submit your Week 1 Assignment by **Monday, [Date - next Monday] at 11:59 PM [Your Time Zone]**. **Submissions after this time will not be accepted.**
    - Given the fast-paced nature of the bootcamp and the 3-day submission window, we strongly advise you to **start working on the assignment early in the week and manage your time effectively.**

10. **Seeking Assistance:**
    - We are here to support your learning. If you encounter any challenges or have questions while working on the assignment, please **don't hesitate to reach out to your instructor or teaching assistants as soon as possible**. Early questions are highly encouraged, especially with this shorter submission timeframe.

**Tip for Success:** To make the most of the 3-day submission window, we recommend reviewing the assignment problems as soon as they are released and starting to work on them incrementally throughout the week, rather than trying to complete everything in one go close to the deadline.

**Good luck with your Week 1 Assignment!** This assignment is a chance to showcase your problem-solving skills using the Python fundamentals you've learned. Remember to review the notes and exercises from Week 1 if you need a refresher. Don't hesitate to ask for help if you encounter significant difficulties.
