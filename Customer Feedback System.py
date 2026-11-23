try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if not name or not feedback:
        raise ValueError("Name or feedback cannot be empty!")

    print("\nThank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)

except ValueError as error:
    print("Error:", error)

finally:
    print("Feedback system execution completed.")