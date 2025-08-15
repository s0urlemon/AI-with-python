print("Hello!I am an AI bot.What's your name? :)")
name=input()
print(f"Nice to meet you,{name}!")
print("how are you feeling today?(good or bad)")
mood=input().lower()

if mood=="good":
    print("I'm glad to hear that!")
elif mood=="bad":
    print("I'm sorry to hear that...I hope things get better soon.")
else:
    print("I understand..Sometimes it can be difficult to describe your emotions..")

print(f"It was nice chatting with you {name}.Goodbye!")