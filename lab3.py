# [CELL 1] STUDENT CONFIGURATION

LAST_NAME = "Villarta"
STUDENT_ID = "3364"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(d) for d in STUDENT_ID if d.isdigit())
NAME_LENGTH = len(LAST_NAME)

print("Student:", LAST_NAME)
print("Seed Digit:", SEED_DIGIT)
print("Digit Sum:", ID_SUM)
print("Surname Length:", NAME_LENGTH)
# [CELL 2] FUNCTIONAL ENCAPSULATION

def greet():
    print("=" * 40)
    print(f"System Initialized for: {LAST_NAME}")
    print("=" * 40)

def identity_code():
    code = SEED_DIGIT * NAME_LENGTH
    return code

# Run the functions to test
greet()
print("Identity Code:", identity_code())
# [CELL 3] RECURSIVE FUNCTION

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the recursive function
print("Factorial of Seed Digit:", factorial(SEED_DIGIT))