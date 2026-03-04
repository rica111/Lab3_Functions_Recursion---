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
# [CELL 4] PARAMETRIC PROCESSING

def user_summary(title, *scores, **info):
    print(f"=== {title} ===")

    total = sum(scores)
    average = total / len(scores)

    print("Scores:", scores)
    print("Total:", total)
    print("Average:", round(average, 2))

    for k, v in info.items():
        print(f"{k}: {v}")

    return average

# Example call
avg = user_summary(
    f"{LAST_NAME} Academic Report",
    SEED_DIGIT * 10,
    ID_SUM,
    NAME_LENGTH * 5,
    id=STUDENT_ID,
    surname=LAST_NAME
)