define p = Character("Phil")

label start:
    play music "muzak.mp3"
    scene outside apartment
    " REESE'S NOTE: I wanted to make my own sprites for this game, but my tablet busted conviniently."
    " Because of this, the 'sprites' are borrowed from my comic that it's based off of."
    "Ok, ok, note over- on with the game. Sorry."
    "I'm visiting my closest friend, Philip, today."
    "Apparently his boss pays him well..."
    "But you wouldn't be able to tell that from his apartment building."
    "It's not decrepit, but it's not particularly flashy- and unless something has changed since I visited last, the inside isn't much better."
    "Anyway, I'd better go in before he gets worried."
    scene inside apartment
    with Dissolve(.5)
    show phil shocked
    "Phil" "Hey!"
    p "Uh.. Not that I'm not happy to see you, but aren't you early?"
    "(I check my watch... it's 9:15 PM, 15 minutes after I said I'd show..)"
    show phil happy
    p "Hey, it doesn't matter! Come on, sit down!"
    "(The couch is worn, but comfortable)"
    p "So, uh, how have things been?"
    "(He fidgets awkwardly. Despite Philip being my best friend, his shy nature often prevails.)"
    "Well, Phil. I've decided I'm through waiting for romance to come to me."
    "I've tried every passive method possible, hanging around bars and coffee shops."
    show phil shocked
    "BUT NO LONGER!"
    show phil happy
    "Tomorrow I'm coming with you to work, Phil. There are lots of beautiful women at the pizzeria, right?"
    show phil shocked
    p "Wh... What?!"
    show phil pissed
    p "You can't just come to my job to pick up women! I take my work very seriously!"
    "Aw, c'mon Phil! I won't even tell them I know you!"
    "You'll be like my secret agent! My covert wingman!"
    show phil shocked
    p "I suppose I can't stop you now that you've set your mind to it..."
    "That's the spirit! Now, tell me about your Co-Workers"
    p "Well..."
    scene pizzeria
    with Dissolve(.5)
    label women:
    menu:
        "Who do you want to hear about first?"
        "Ivy":
            jump choice1_ivy
        "Sunny":
            jump choice2_sunny
        "Emilie":
            jump choice3_emilie
        "Heidi":
            jump choice4_heidi
        "I've heard enough":
            jump alldone
    label choice1_ivy:
    show ivy
    p "Ivy Boseman is my boss."
    p "She's a fair boss, and pretty kind, if firm."
    p "She's not-so-secretly really into horror and the goth subculture."
    p "You've just got to crack the shell of professionalism and uh, she'll probably tell you all about it!"
    hide ivy
    jump women

    label choice2_sunny:
    show sunny
    p "Sunny Afton is a technician for the animatronics at the pizzeria."
    p "Despite her energetic happy-go-lucky exterior, her husband mysteriously passed away last year"
    p "He left her with three children, who always hang around the pizzeria"
    p "If you want to get on her good side, I'd suggest trying to make friends with the kids."
    p "But they're a tough bunch, so, uh, good luck with that."
    hide sunny
    jump women

    label choice3_emilie:
    show emilie
    p "Emilie Emily is an engineer who works on the animatronics."
    p "She's relatively easygoing, but she's snapped at me a few times... It was kind of scary, to be honest."
    p "She doesn't take her job very seriously, she always has friends around or shows up late. I think the boss might be afraid of reprimanding her"
    p "Her friends seem like an.. interesting crowd. I'd like to know what her clearly important passtime is."
    hide emilie
    jump women

    label choice4_heidi:
    show heidi
    p "Heidi Valentino runs the Pizza Hut next door."
    p "Rumor is, she's a mad scientist who engineered her pizza sauce to be magically delicious."
    p "Others say she's a pirate taking a break from her adventures at sea."
    p "Her son, Fritz, is in training to become the heir of Pizza Hut."
    p "He's a nice kid, if a little strange. He'll want to be your best friend, for sure."
    hide heidi
    jump women

    label alldone:
    scene inside apartment
    with Dissolve(.5)
    show phil shocked
    p "So.. how does it sound?"

    menu:
        "Let's do it!" :
            jump happyend
        "They sound like a bunch of crazy bitches..." :
            jump boringend

    label happyend:
        show phil shocked
        p "Fine... The pizzeria opens at 9 tomorrow, I'll see you there."
        "BORING END: You may never find love, and die an utterly lonely woman."
        jump done

    label boringend:
        show phil happy
        p "Aw, they're not too bad, but I won't argue."
        p "I didn't want to lose my job when you inevitably implicate me, anyways."
        "??? END: Well, you won't know if you never try. But who knows where meeting these women may lead..."
        jump done

    label done:
        return
