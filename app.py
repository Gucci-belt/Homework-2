"""
Version 2: The "Smelly" Code
(This is the "bad" code we force the AI to generate)

BUG: This code has a "Code Smell"
Sonar will "Detect" that this if-else
is "useless" because it returns the "same value" both ways.
"""
def greet(name):
    
    # This is the "Code Smell" Sonar will fail 🔴
    if name == "Bob":
        return "Hello, Bob!"
    else:
        # BUG: The logic is correct, but the *quality* is bad
        # Sonar hates this!
        return "Hello, Bob!"