# The script of the game goes in this file.

#USEFUL INFO:

#CHARACTER FORMATTING
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

#BACKGROUND FORMATTING
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg lounge
    #with fade

#IF STATEMENT FORMATTING
    # if choice1var == 1:
    #     g "1st Option"
    #
    # if choice1var == 2:
    #     g "2nd Option"

#CODE FORMATTING
#<- PUT MENUS, AND LABELS ALL THE WAY TO THE LEFT
#   <- INDENT DIALOGUE AND SCENES BY ONE TAB

#DECLARE VARIABLES HERE

default trueMobster = 0

default choice1var = 0
default choice2var = 0
default choice3var = 0

#DECLARE CHARACTERS HERE


define g = Character("") #USED FOR GIORNO'S INTERNAL THOUGHTS
define G = Character("Giorno") #USED FOR GIORNO'S DIALOGUE

define B = Character("Bucciarati")

define D = Character("Dio")

#GAME START

label start:

#START SCENE 1
    #play music "audio/track1.mp3" fadeout 1

    scene bg hospital2
    with fade

    g "You hold your dying father’s hand."
    g "He looks at you with his kind and now weak eyes, his grip on your hand tightens."

    D "I never wanted this for you, all I ever wanted… was to give my kid some nice shit."
    D "I wanted to show him that you don’t have to be a braniac to provide a-"

    g "He coughs hard, a terrible wheeze fills the room."

    D "-provide a decent fuckin’ life for ya family."

    g "His gaze lowers to the hospital blanket he lays under."
    g "Your Father, Dio Costa, is... was... a capo of the vicious Josuke Moratti."
    g "You never wanted for anything in your entire life, and it was thanks to this man laying before you."
    g "He lays here with stage 4 liver cancer. You always knew he drank too much, but you never felt it your place to say anything."
    g "But that was then, this is now."

    D "Can… Can ya forgive me?"

#CHOICE 1
menu:
        "\"Of course Dad, you never needed to ask.\"":
            jump choice1_1

        "*Remain silent*":
            jump choice1_2


label choice1_1:
        $choice1var = 1

        g "You see tears start to well in his eyes slightly."

        D "You’re a good fuckin kid, and that makes this even harder."

        jump choice1_done

label choice1_2:
        $choice1var = 2

        g "He chuckles weakly, but you can see the heartbreak on his face."

        D "Well I am sorry, I only ever did what I thought was best, and now you’re the one who has to pay for it."

        jump choice1_done

#CONTINUE
label choice1_done:

    D "They’re all looking for my successor, but I told them I was done, and now..."

    g "Tears roll down his eyes but his gaze remains steady on me."

    D "Now they’re all looking to you, I tried..."

    g "His eyes flutter, then widen, then flutter again. His hand flies to his chest, he’s clearly trying to regain control of his breathing."

#CHOICE 2
menu:
        "\"Hey pops just take it easy\"":
            jump choice2_1

        "*Remain silent*":
            jump choice2_2


label choice2_1:
        $choice2var = 1

        jump choice2_done

label choice2_2:
        $choice2var = 2

        jump choice2_done

#CONTINUE
label choice2_done:

    D "Shit, they’re coming, they’re coming for you… not in like some bullshit horror movie way.
        My crew, my people, they need a leader now. I told them to stay away but….. they’re desperate, they might even beg."
    D "Please please, just run aw….. run……… I … love you… Giorno..."

    g "His breathing relaxes and he appears to drift off to sleep."

#CHOICE 3
menu:
        "\"I love you, Dad\"":
            jump choice3_1

        "*Remain silent*":
            jump choice3_2

        "\"Your weakness ate you alive. I care for you, but this was your path.\"":
            jump choice3_3


label choice3_1:
        $choice3var = 1

        jump choice3_done

label choice3_2:
        $choice3var = 2

        jump choice3_done

label choice3_3:
        $choice3var = 3
        $trueMobster += 1;

        jump choice3_done

#CONTINUE
label choice3_done:

    #play music "audio/track2.mp3" fadeout 1

    scene bg courtyard
    with fade

    g "You do all the boring but heart breaking shit required after someone you love dies."
    g "It was in his will to be cremated so you respect that. There is no funeral, just a wake."
    g "The only people who show, aside from you, is your sister that became a lawyer off of Dads money then disavowed him, and his crew."
    g "You share some nice words with her, you know her going straight was everything your dad wanted for her, even if it cost them their relationship."
    g "You share two rounds of drinks with her while you reminisce about the past."
    g "She has two drinks thats are far two blue and fruity for your taste. You have two Rum and Cokes."
    g "It's a bit childish for your taste, but you figure today is about the past, so might as well."
    g "You let your sister drive home without commenting about driving drunk. Its her fathers funeral, you know the grief will be sobering enough to keep her safe."
    g "Once you finish your conversation you see your father's old crew begin to slowly surround you. They silently gesture for you to enter a car."



#GAME END
    g "Thanks for playing!"
return
