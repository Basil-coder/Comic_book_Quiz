score = 0

print("Welcom to the Comic Quiz, this game will test your wits in the knowledge of the Comicbook Universe... Ready? ")

#Question 1
answer1 = input("Who is the Fastest Speedster in the Comic book Universe? \na. Wally West \nb. Bart Allen \nc. Barry Allen \nAnswer:")
if answer1 == "c":

    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")

    #Question 2
answer2 = input("Who raised the Silver Surfer after his planet was destroyed? \na. Thanos The Titan \nb. The One Above All \nc. Galactus \nAnswer:")
if answer2 == "c":
    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")

    #Question 3
answer3 = input("What race/species is Wanda Maximoff? \na. Mutate \nb. Alien \nc. Other \nAnswer:")
if answer3 == "a":
    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")

  #Question 4
answer4 = input("In the comics, which was the creator of Ultron? \na. Tony Stark \nb. Ant-Man \nc. J.A.R.V.I.S \nAnswer:")
if answer4 == "b":
    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")  

    #Question 5
answer5 = input("Which color Kryptonite PERMANENTLY disables Super-Man's powers? \na. Pink \nb. Blue \nc. Yellow \nAnswer:")
if answer5 == "c":
    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")

    #Question 6
answer6 = input("Batman and Captain America had a hand to hand combat battle in the 2nd DC&Marvel Crossover series, what was the outcome of the battle ? \na. Batman won \nb. Captain America won \nc. Total Draw \nAnswer:")
if answer6 == "c":
    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")

     #Question 7
answer7 = input("Ra's Al Goul trained Batman to do what? \na. Join League of Shadows \nb. Obliterate Gotham City \nc. To Become Batman \nAnswer:")
if answer7 == "c" or answer7== "b":
    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")

     #Question 8
answer8 = input("In the Batman Beyond series, which character went through all the phases of the Bat-Family? \na. Jason Todd \nb. Dick Grayson \nc. Tim Drake \nAnswer:")
if answer8 == "a":
    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")

     #Question 9
answer9 = input("Joker confessed that he had feelings for Harley Quinn, however he ... her to get rid of those feelings. \na. Killed her \nb. Shipped her into space \nc. Married her \nAnswer:")
if answer9 == "b":
    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")

    #Question 10
answer10 = input("Deadshot has been known to have impecably precise aiming, how does he improve his aiming skills over time? \na. Enlisting as a contarct killer \nb. Video games \nc. Shooting range \nAnswer:")
if answer10 == "b":
    score += 1
    print("Correct")
    print("Score:",score)
    print("\n")
else:
    score -= 1
    print("Wrong Bitch!!!")
    print("\n")

    #ScoreTime
if score <= 1:
        print("You are not qualified to be part of the Comic Society, you're a disgrace bro!")
elif score == 5:
        print("The knowledge you've obtained over the years is good young Padawan, but you need more.")
elif score >= 6:
        print("You are worthy of the title Nerd and is allowed to be considered in Comic disputes and discussions.")
