# Higher or Lower
import random

celebs = {
    "Cristiano Ronaldo": ["Footballer", "Portugal", 664_000_000],
    "Beyonce": ["Musician", "United States", 309_000_000 ],
    "Virat Kohli": ["Cricketer", "India", 273_000_000],
    "Selena Gomez": ["Musician", "United States", 417_000_000 ],
    "Zendaya": ["Actress", "United States", 177_000_000],
    "Dwayne Johnson": ["Actor & Wrestler", "United States", 392_000_000],
    "Kim Kardashian": ["Media Personality", "United States", 355_000_000],
    "Elon Musk": ["Businessman", "United States", 45_000_000],
    "Priyanka Chopra": ["Actress", "India", 91_500_000],
    "LeBron James": ["Basketball Player", "United States", 158_000_000],
    "Lionel Messi": ["Footballer", "Argentina",506_000_000],
    "Ariana Grande": ["Musician & Actress", "United States", 374_000_000],
}

score = 0
A = random.choice(list(celebs.keys()))
print(A)

def compare_followers(A, B):
       
    print(f"Compare A: {A}, a {celebs[A][0]}, from {celebs[A][1]}.")
    print("vs")
    print(f"Compare B: {B}, a {celebs[B][0]}, from {celebs[B][1]}.")

    answer = input("Who has more followers? 'A' or 'B': ").upper()

    if (answer == "A" and celebs[A][2] > celebs[B][2]) or (answer == "B" and celebs[A][2] < celebs[B][2]):
        return True
        
    
    else:
        return False
        
while True:
    B = random.choice(list(celebs.keys()))
   
    while B == A:
        B = random.choice(list(celebs.keys()))
    
    if compare_followers(A, B):
        score += 1
        print(f"You're right! Current score: {score}")

        # Set correct cele as A for next round
        if celebs[A][2] > celebs[B][2]:
            A = A

        else:
            A = B

    else:
        print(f"You're wrong! Current score: {score}")
        break

# Updated Game logic with unique comparisions 

"""
import random

celebs = {
    "Cristiano Ronaldo": ["Footballer", "Portugal", 664_000_000],
    "Beyonce": ["Musician", "United States", 309_000_000],
    "Virat Kohli": ["Cricketer", "India", 273_000_000],
    "Selena Gomez": ["Musician", "United States", 417_000_000],
    "Zendaya": ["Actress", "United States", 177_000_000],
    "Dwayne Johnson": ["Actor & Wrestler", "United States", 392_000_000],
    "Kim Kardashian": ["Media Personality", "United States", 355_000_000],
    "Elon Musk": ["Businessman", "United States", 45_000_000],
    "Priyanka Chopra": ["Actress", "India", 91_500_000],
    "LeBron James": ["Basketball Player", "United States", 158_000_000],
    "Lionel Messi": ["Footballer", "Argentina", 506_000_000],
    "Ariana Grande": ["Musician & Actress", "United States", 374_000_000],
}

score = 0
used_celebs = set()
A = random.choice(list(celebs.keys()))
used_celebs.add(A)

while True:
    # Pick a new celeb not already used
    remaining = list(set(celebs.keys()) - used_celebs)
    if not remaining:
        print(f"🎉 You've guessed all correctly! Final score: {score}")
        break

    B = random.choice(remaining)

    print(f"\nCompare A: {A}, a {celebs[A][0]} from {celebs[A][1]}")
    print("VS")
    print(f"Compare B: {B}, a {celebs[B][0]} from {celebs[B][1]}")

    answer = input("Who has more followers? Type 'A' or 'B': ").upper()

    if (answer == "A" and celebs[A][2] > celebs[B][2]) or (answer == "B" and celebs[B][2] > celebs[A][2]):
        score += 1
        print(f"✅ You're right! Current score: {score}")
        winner = A if celebs[A][2] > celebs[B][2] else B
        A = winner
        used_celebs.add(B)
    else:
        print(f"❌ You're wrong! Final score: {score}")
        break
"""

        



