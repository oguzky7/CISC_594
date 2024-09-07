Oguz Kaan Yildirim 
Veys Diyar Yurtsever
CISC 594 Version Control Assignment

# Simpletron Simulator

The Simpletron is a hypothetical computer that runs programs written in Simpletron Machine Language (SML). This project allows you to enter SML instructions, load them from a file, or execute predefined tasks to test different features of the Simpletron.

## Getting Started

1. **Clone the Repository:**
   ```
   git clone https://github.com/oguzky7/CISC_594.git
   cd CISC_594
   ```

2. **Running the Program:**
   You can run the Simpletron in several modes:

   - **Manual Program Entry:**
     ```
     python main.py
     ```
     Enter your SML instructions manually. Each instruction should be a 4-digit signed integer. Enter `-99999` to stop entering the program and start execution.

   - **Load Program from File:**
     ```
     python main.py
     ```
     Choose to load `program2.txt` or `program3.txt` when prompted.

   - **Run Predefined Tasks:**
     - **Task 1:** Run the program for the first task.
       ```
       python task1.py
       ```
     - **Task 2:** Run the program for the second task.
       ```
       python task2.py
       ```
     - **Task 3:** Run the program for the third task.
       ```
       python task3.py
       ```

3. **Help Command:**
   At any point during program entry, type `help` to display detailed instructions and a list of supported operations.

## Running Tests

You can test the Simpletron with predefined tasks:

- **Task 1:** Basic operations test.
  ```
  python task1.py
  ```
- **Task 2:** Intermediate operations test with more complex arithmetic.
  ```
  python task2.py
  ```
- **Task 3:** Advanced operations including branching and loops.
  ```
  python task3.py
  ```

Each task is designed to test specific features of the Simpletron. The output will display the results and a memory dump after execution.
