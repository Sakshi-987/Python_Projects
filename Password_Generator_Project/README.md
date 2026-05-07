# 🔐 Random Password Generator using Python

A secure and customizable Random Password Generator built using Python fundamentals.  
This project generates strong and unpredictable passwords based on user-defined preferences such as password length, inclusion of numbers, and special characters.

The project was developed to strengthen core Python concepts including:
- functions
- loops
- condition handling
- string manipulation
- randomization
- boolean logic
- user input handling

---

# 🚀 Features

- 🔑 Generates random and secure passwords
- 📏 Custom minimum password length support
- 🔢 Option to include numeric characters
- ✨ Option to include special characters
- 🎯 Ensures required conditions are satisfied before generating the final password
- 🛡️ Uses safer real-world special characters
- ⚡ Beginner-friendly and lightweight project

---

# 🛠️ Technologies Used

- Python
- `random` module
- `string` module

---

# 📂 Project Structure

```text
Random_Password_Generator/
│
├── password_generator.py
└── README.md
```

---

# ⚙️ How It Works

1. User enters:
   - minimum password length
   - whether numbers should be included
   - whether special characters should be included

2. The program creates a valid character set based on user preferences.

3. Random characters are selected using Python’s `random.choice()` method.

4. The generated password is checked to ensure:
   - required length is satisfied
   - number condition is fulfilled (if enabled)
   - special character condition is fulfilled (if enabled)

5. Once all conditions are satisfied, the final password is displayed.

---

# 🔍 Concepts Implemented

This project demonstrates several important Python concepts:

## ✅ Functions
Used to modularize password generation logic.

## ✅ Randomization
Implemented using:
```python
random.choice()
```

to generate unpredictable passwords.

## ✅ String Handling
Used Python’s `string` module for predefined character sets:
```python
string.ascii_letters
string.digits
```

## ✅ Boolean Logic
Used flags such as:
```python
has_numbers
has_special
meets_criteria
```

to validate password requirements.

## ✅ Loops & Conditions
Used loops and conditional statements to ensure all password constraints are satisfied before returning the final password.

---

# 📸 Example Output

```text
Enter the minimum-length password you need to set: 8
Do you want to include numbers in your password (y/n)? y
Do you want to include special-characters in your password (y/n)? y

Generated Password: A@7kP#2q
```

---

# 🧠 Challenges Faced

During development, several practical issues were solved:

- Ensuring password randomness
- Validating required conditions correctly
- Managing dynamic character sets
- Handling boolean logic accurately
- Avoiding weak predictable passwords

These helped improve understanding of Python logic building and problem-solving.

---

# 📈 Future Improvements

Planned upgrades for future versions:

    An improved version designed based on real-life password policies, ensuring:

    ✔ At least one lowercase letter
    ✔ At least one uppercase letter
    ✔ At least one digit
    ✔ At least one special character
    ✔ Fixed password length
    ✔ Strong randomness using secure methods

---

# 🎯 Learning Outcome

This project helped in understanding:
- Python fundamentals
- Randomized logic implementation
- Input validation
- Real-world password generation concepts
- Boolean condition handling
- Clean code structuring

---

# 📌 Author

**Sakshi Sahu**  
B.Tech CSE Student | Java(DSA) & Python | Full Stack Development | Learning SpringBoot & System Design