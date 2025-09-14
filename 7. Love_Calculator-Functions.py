# Love Calculator

def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()
    
    true_count = 0
    love_count = 0

    for letter in "true":
        count = combined_names.count(letter)
        true_count += count
        #print(f"{letter.upper()} occurs = {count} times")
    print(f"True score = {true_count}")

    for letter in "love":
        count = combined_names.count(letter)
        love_count += count
        #print(f"{letter.upper()} occurs = {count} times")
    print(f"Love score = {love_count}")

    print(f"Love score for {name1} and {name2} is {str(true_count) + str(love_count)}")

    
calculate_love_score("Anusha Dunaboyina", "Vikas Konduri")
calculate_love_score("Anusha Dunaboyina", "Ayra Konduri")
calculate_love_score("Vikas Konduri", "Ayra Konduri")