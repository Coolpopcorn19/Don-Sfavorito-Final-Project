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
default choice4var = 0
default choice5var = 0
default choice6var = 0
default choice7var = 0
default choice8var = 0
default choice9var = 0


#DECLARE TRANSFORMS HERE

transform left:
    xalign 0.0
    yalign 1.0
transform midleft:
    xalign 0.25
    yalign 1.0
transform center:
    xalign 0.5
    yalign 1.0
transform midright:
    xalign 0.75
    yalign 1.0
transform right:
    xalign 1.0
    yalign 1.0

#DECLARE CHARACTERS HERE


define g = Character("") #USED FOR GIORNO'S INTERNAL THOUGHTS
define G = Character("Giorno") #USED FOR GIORNO'S DIALOGUE


define M = Character("Mista")
define A = Character("Abbacchio")
define F = Character("Fugo")
define D = Character("Dio")
define Q = Character("???")
define J = Character("Joseph")
define W = Character("Waitress")
define O = Character("Moretti")

#GAME START

label start:

#START SCENE 1

    play music "audio/track1.ogg" fadeout 1

    scene bg hospital2
    show giorno normal at left
    with fade


    g "I hold my dying father’s hand."
    g "He looks at me with his kind and now weak eyes, his grip on my hand tightens."

    D "I never wanted this for you, all I ever wanted… was to give my kid some nice shit."
    D "I wanted to show him that you don’t have to be a braniac to provide a-"

    g "He coughs hard, a terrible wheeze fills the room."

    D "-provide a decent fuckin’ life for ya family."

    g "His gaze lowers to the hospital blanket he lays under."
    g "My father, Dio Costa, is... was... a capo of the vicious Josuke Moretti."
    g "I never wanted for anything in my entire life, and it was thanks to this man laying before me."
    g "He lays here with stage 4 liver cancer. I always knew he drank too much, but I never felt it my place to say anything."
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

        g "I see tears start to well in his eyes slightly."

        D "You’re a good fuckin kid, and that makes this even harder."

        jump choice1_done

label choice1_2:
        $choice1var = 2

        g "He chuckles weakly, but I can see the heartbreak on his face."

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
    stop music fadeout 1

    play music "audio/track2.ogg" fadeout 1

    scene bg courtyard
    show giorno normal at left
    with fade

    g "I go through all the boring but heartbreaking shit required after someone you love dies."
    g "It was in his will to be cremated, so I respect that. There is no funeral, just a wake."
    g "The only people who show, aside from myself, is my sister that became a lawyer off of Dads money, then disavowed him, and his crew."
    g "I share some nice words with her. I know her going straight was everything your dad wanted for her, even if it cost them their relationship."
    g "I share two rounds of drinks with her while I reminisce about the past."
    g "She has two drinks that are far two blue and fruity for my taste. I have two Rum and Cokes."
    g "It's a bit childish for my taste, but I figure today is about the past, so might as well."
    g "I let my sister drive home without commenting about driving drunk. Its her fathers funeral, I know the grief will be sobering enough to keep her safe."
    g "Once I finish my conversation, I see my father's old crew begin to slowly surround me. They silently gesture for me to enter a car."

    show giorno normal at center with move

#CHOICE 4
menu:
        "*Follow their lead and enter silently*":
            jump choice4_1

        "\"Sorry boys, but I practice stranger danger.\" *Grin*":
            jump choice4_2


label choice4_1:
        $choice4var = 1

        jump choice4_done

label choice4_2:
        $choice4var = 2

        M "Well its a good thing we ain’ strangers."

        show mista normal behind giorno with dissolve:
            xalign 0.70
            yalign 1.00

        g "A man about my age slings his arm around me."
        g "He’s young with short black hair and pretty damn handsome."



        M "We’re friends of your father. Real good friends."

        g "He grins back at you."

menu:

        "*Remain silent*":

            M "I knew ya’d get it."

            g "He guides me slightly forcefully into the car."

            hide giorno normal with moveoutright
            hide mista normal with moveoutright

            g "My mind is distracted by thoughts of my father."
            g "I don’t like Mista, I find his light hearted behavior disrespectful at a wake."
            g "I remain silent despite his chatter for the entire drive."

            jump choice4_done

        "\"You mean employees don’t ya boys?\"":
            $trueMobster += 1;

            show mista normal at right with move
            show giorno normal at left with move

            g "Mista looks at the rest of the gang a touch confused, but then re-locks with my gaze."

            M "Uh… yeah, I guess."

            g "I smile."

            G "Good! I wouldn’t want any confusion about who’s in fucking charge."

            g "My tone changes as I swear and I see them pay attention accordingly."
            g "I open the door of the car that they were guiding me towards, and I enter."
            g "Mista enters around the opposing side."

            hide giorno normal with moveoutleft
            hide mista normal with moveoutright


            g "I don’t care where they’re taking me, all that matters is that they’ll listen."

            jump choice4_done


#CONTINUE
label choice4_done:
    stop music fadeout 1

    play music "audio/track3.ogg" fadeout 1

    scene bg casino
    with fade

    show giorno normal at left
    show mista normal at midleft behind giorno
    show fugo normal at midright
    show abbacchio normal at right behind fugo


    g "Mista and the rest of the gang led me into the back room of a casino."
    g "I'm a touch shocked at how young the crew is."
    g "The oldest member stands at the back of the room, I figure he’s in his late 20s."

    hide mista with dissolve
    hide fugo with dissolve


    g "He stands disinterested and borderline disgusted, but his gaze remains straight ahead, unwilling to meet mine."
    g "Based on my fathers notes, his name is Abbacchio. I’d compare him to a rook."
    g "He’s noteworthy for having taken several stash houses during the 2009 Cappelli takeover."
    g "There’s no doubt about his skills, but he’s got the grace of a bull and half as much patience."

    Q "Giorno!"

    g "I was snapped out of my thoughts by a familiar voice."

    hide abbacchio with dissolve

    show joseph normal at center behind giorno with dissolve

    G "Joseph! God is it good to see a familiar face."

    show joseph normal at midleft with move

    g "He closed the gap from his seat to me and hugged me."

    J "It’s good to see you too Gio, I feel fuckin’ terrible about pops."

    g "Joseph was my cousin, but ever since his father died on “company business” and his family moved in with us, he’s basically been my brother."

    G "Yeah me too Jojo."

    g "The scrawny man who had been laying on the couch since I entered spoke up."

    show fugo normal at right with dissolve

    Q "Jojo?"

    g "He cackled to himself and went back to cleaning his fingers with a pocket knife."

#CHOICE 5
menu:
         "\"I feel like using a knife to clean your nails probably ends up doing more harm than good.\"":
            jump choice5_1

         "\"You got a problem?\"":
            jump choice5_2

label choice5_1:
        $choice5var = 1

        Q "Glad I asked."

        g  "My fathers crew was about as welcoming as I remember."
        jump choice5_done

label choice5_2:
        $choice5var = 2
        Q "Not at the moment no."
        jump choice5_done

#CONTINUE
label choice5_done:

    J "Fugo show a little respect, he’s about to be the newest Capo."

    g "A sharp voice cut through the room."

    show abbacchio normal at midright with dissolve

    A "He’s not ANYTHING until Moretti approves him."

    J "Yeah that’s cuz you don’t know him, this kids mind is like a steel trap."
    J "Ain’t that right Gio?"

#CHOICE 6
menu:
        "\"Wait Capo?\"":
            jump choice6_1

        "\"Snap snap, goes the trap.\"":
            jump choice6_2

label choice6_1:
        $choice6var = 1

        g "Abbachio leaned his hand on his thigh and groaned."

        A "Mista, you didn’t fill him in?"

        show mista normal at center with dissolve

        M "Moretti called in a half hour ago, said he wanted to talk to the kid himself."
        jump choice6_done

label choice6_2:
        $choice6var = 2

        g "I immediately got the distinct feeling that “snap snap goes the trap” was the wrong thing to say."

        show mista normal at center with dissolve

        M " … Anyway"
        jump choice6_done

#CONTINUE
label choice6_done:

    M " Moretti said that that he wants Jo n’ Fugo to come with the kid to Stratiacellis on fourth."

    A "He wants Joseph and Fugo too? You think Moretti’s gonna have em run a-"
    M "Seems like it."

    g "Abbachio’s face seemed to grow pensive for a moment."

    A "Good, no point in starting in the shallow end in this business."

    g "Joseph's warm expression disappeared. Fugo’s smile faded into a stern calm."
    g "I tried to begin reasoning what action would involve the two of them, but I figured I’d find out soon enough."
    g "The silence hung in the air for a few moments."

    J "Come on, bad manners to keep the Don waiting."

    F "That it is."

    g "Fugo kicked his feet off the couch and quickly stood."
    g "He stretched his neck and then his gaze turned to Joseph, who in turn looked at me and gestured towards the door with his head."
    g "I walked out the door and they followed close behind."

    hide giorno with moveoutleft
    hide joseph with moveoutleft
    hide fugo with moveoutleft

    scene bg casino2
    show giorno normal at left
    with fade

    g "As soon as the door closed the sound of Mista's loud voice was immediately silenced by the noise of the Casino."
    g "I spent a lot of years in the lobby here doing homework while my dad worked, but I had only been to the play floor itself a handful of times."
    g "Old men who reeked of booze littered the tables, almost all smoking cigars and smiling wide."
    g "A good deal of them had beautiful women next to them."
    g "When I was younger I actually developed the impression that it was a rather common tradition for fathers to take their daughters to casinos."
    g "Ah the innocence of youth, I manuerved past the cramped hallways of slot machines to the parking lot."

    stop music fadeout 1

    play music "audio/track2.ogg" fadeout 1

    scene bg dodge
    show giorno normal at left
    show joseph normal at midright
    show fugo normal at right behind joseph
    with fade

    F "Alright who’s driving?"

    J "Figured I would."

    g "Fugo smiled and shook his head."

    F "Why am I not at all surprised you’d say that?"

    g "Joseph smiled back and slipped his keys out of his pocket."
    g "I heard the unmistakable beep of a car unlocking and turned to see a cherry red Dodge Charger."
    g "I now understood Joseph's smile was one of pride, bordering on infatuation."
    g "Joseph's eyes met mine and he raised his eyebrows."

    J "Impressed?"

#CHOICE 7
menu:
        "\"Seems like it’d get a lot of parking tickets.\"":
            jump choice7_1

        "\"It’s nice, but in this line of work flash can be a liability.\"":
            $trueMobster += 1;
            jump choice7_2

label choice7_1:
        $choice7var = 1
        jump choice7_done

label choice7_2:
        $choice7var = 2
        J "Its my friggin dream car, its worth it."
        jump choice7_done

#CONTINUE
label choice7_done:

    play sound "audio/driving.ogg" fadeout 1

    scene bg car
    with fade

    g "Fugo took shotgun and Joseph told him he needed to take the back seat."
    g "Fugo complained but Joseph insisted."
    g "We drove in silence for a bit until Fugo stuck his head between our seats."

    F "You know what the boss is gonna make ya do right?"

    J "Fugo, the boss said he wanted to do the talking."

    F "Jesus Jo, it's not like he thinks Moretti’s gonna ask him to pick flowers."

    J "Still."

    G "What kind of man is Moretti?"
    g "Fugo chuckled."

    J "A bad man. I mean, shit, most of us are obviously but he’s different, doesn’t really care about the family."

    F "Oi! Careful where you say that. Its a death sentence if Moretti hears you guys saying that."

    g "Fugo Cucinelli's exploits were covered equally well in my dads notebook."
    g "I’d compare him to the knight, he’s erratic and effective."
    g "He’s got a knack for sniffing out and infiltrating drug rings like no other."
    g "He pulls in more cash than any other of my dad’s Lieutenants, if he didn’t speak his mind so often he might be a Capo himself."

    F "Not as if any of those slow fucks could ever get the drop on me."

    J "Yeah I’m sure they wouldn’t gun you down without a second thought."

    F "See Jo? That’s why you’re an asshole, ya got no faith."

    G "You gonna take that Joseph?"

    g "We chuckled for a few moments after that."
    g "But the silence returned and I became fully aware of what we were on our way to do."

    stop sound fadeout 1

    g "After a while Joseph pulled into a parking lot and Fugo became more attentive to our surroundings."

    J "Alright just speak clearly, and confidently, and things’ll be fine."

    F "Yeah and tell a joke."
    J "Fugo, shut the fuck up. Don’t try to be funny."

    G "Yeah I wasn’t planning on it."

    stop music fadeout 1

    play music "audio/track4.ogg" fadeout 1

    scene bg restaurant
    show giorno normal at left
    show joseph normal at midright
    show fugo normal at right behind joseph
    with fade

    g "We got out of the car and walked along the concrete sidewalk into the Restaurant."
    g "Stratiacellis was an incredibly nice restaurant, the kind I would go to back when my Mom was still with us."
    g "We stood in the seating area for only a moment, Fugo put a toothpick in his mouth and locked eyes with the host."
    g "The hosts eyes widened slightly upon noticing Fugo but his twisted into an accommodating smile nonetheless, he walked briskly over to the waitress behind the podium and whispered something to her."
    g "Her eyes widened similarly to how his did at first but she promptly walked up to us and began speaking."

    W "Would you gentlemen like to follow me?"
    F "Gentlemen? Darlin’ I’m flattered."

    g "Joseph audibly scoffed and looked to the waitress."

    J "Lead the way."

    g "She led us up stairs that were placed along the walls of the main dining room."
    g "Chandeliers were posted along the ceiling, softly illuminating the white cloth dining tables."
    g "The seats were packed with people in expensive clothing, but the volume of the room was surprisingly quiet."
    g "The second floor was smaller and had less customers, but appeared to be an even more exclusive part of the restaurant."
    g "The upstairs had light gold paint with paintings of angels and civilizations on the walls."
    g "She was leading us towards a double set of red doors in the center of the back wall."

    scene bg restaurant2
    show giorno normal at left
    with fade

    g "Once we entered it became immediately clear who Don Moretti was."

    show moretti normal at right with dissolve

    g "The white cloth table had only one seat and plate of food, the man behind the dish was slightly withered with a bit of heft to him."
    g "He wore a black pinstripe suit with a red pocket square, despite the fact it looked as if he couldn’t enjoy anything, he ate the pasta with a quiet determination."
    g "Two men in suits stood behind him with their hands held by their waists."
    g "Moretti finished his bite and wiped his mouth with his napkin"

    O "So, Giorno Costa, I’m sure you have some idea why I’ve asked you here today."

    G "My father, Dio, was your Capo. Since he’s now perished I am to be tested as his replacement in accordance with the Roman Codes."

    O "Oh so you know about the codes, I can see he didn’t raise a slouch. Though given where you’ve come from I do have concerns about your back-bone. Not to speak ill of the dead of course."

#CHOICE 8
menu:
        "\“My Father was a great man.\"":
            jump choice8_1

        "\"We all choose this path for different reasons, in my mind his loyalty outweighed his lack of cruelty.\"":
            $trueMobster += 1;
            jump choice8_2

label choice8_1:
        $choice8var = 1
        O "A good man, for sure."
        jump choice8_done

label choice8_2:
        $choice8var = 2
        O "Well put, but a little idealistic."
        jump choice8_done

#CONTINUE
label choice8_done:
    O "His memory is certainly one that’ll stay with me, nonetheless I’ve got the perfect job to see how you stack up. I see you’ve met Joseph and Fugo."

    G "I have."

    O "They’re good men to know, I like to call em’ my cleaners. You know why?"
    O "Because they clean something?"
    O "Technically correct but a poor sport of an answer. Its because if I have a problem, or a mess is made, they clean it up."
    O "Like if some stupid fuck doesn’t give me my money or decides he’s gonna pull the wool over my eyes they can clean em off the face of the earth."

    G "And you want me to help them clean something."

    O "You really should let people finish their own thoughts kid, but yeah, I wanna see how you clean up."

    g "My father, a fuckin Capo, died of lead poisoning."
    g "Between that and this guys attitude I’m figurin Jojo is right about this guy not giving a shit about the family."
    g "Personal Vendettas are bad for business, but some things can’t be forgiven."
    g "Something didn’t add up, so I figured the best thing for this situation was to go along with Moretti for now."

    G "Lucky for you, I clean up nice."

    O "Lucky for me, Hah."

    g "Moretti cracked a smile but it was unnatural."
    g "It almost feels like he’s the type of man who couldn’t grin without looking villainous."

    O "Well fuck it up, and we can test which one of us is lucky."
    O "Being the kid of a Capo might get you an interview, but there’s not even a chance I’d consider some fuckin’ goombah being let into this family."
    O "Joseph, Fugo, you understand how important your assistance in this test is then right?"

    J "Yes Don."

    F "Absolutely."

    O "Then get the fuck outta here, and Giorno if you’re feeling like you can’t do this shit, then leave and never contact us again."
    O "No hard feelings, out of respect for your father we let you go, So whaddya think, this shit really for you?"

#CHOICE 9
menu:
        "\"Yes.\"":
            jump choice9_1

        "\"No.\"":
            jump choice9_2

label choice9_1:
        $choice9var = 1
        O "Good then, don’t let the door hit your ass on the way out"
        jump choice9_done

label choice9_2:
        $choice9var = 2
        #INSERT DIALOGUE HERE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        jump choice9_done
#CONTINUE
label choice9_done:
    O "Good luck then Giorno."

    g "He gestured with his hands out of the door."
    g "It might’ve been a good idea to say something nice then but all I could do was leave fast."
    g "Joseph and Fugo followed quickly after me. I guess they we’re trying to give the impression of unity."
    g "They must have been loyal to my father, but maybe that’s just something I want to believe."

    hide giorno with moveoutleft

    stop music fadeout 1

    #play music "audio/track5.ogg" fadeout 1

    play sound "audio/driving.ogg" fadeout 1

    scene bg car
    with fade

    g "We drove away for a few minutes quietly until Joseph broke the silence."

    J "Hey Giorno… You know where Moretti wants us to take you to right?"

    G "Yes, Joseph."

    g "I know he was just trying to be nice but I was feeling a touch overfraught at the moment."

    J "… And you know that he expects for you to be the-"
    G "YES, Joseph."

    g "Moretti expected me to kill a man, today, the same day as the death of my father."
    g "The clock on the dashboard read 9:47. Quickest 7 hours of my life."
    g "This afternoon I was begging for a miracle, now I’d be killing someone while they’re begging for the same thing."
    g "I could have left though, from here on out, Its all or nothing."
    g "The drive proceeded in silence. While we were arriving I realized what piece Moretti would be; the king."
    g "He might be a great leader but his individual strength was remarkably weak."
    g "Relying on cruelty over tactics has left him with an incredible blind spot. But he was the man giving ME the orders."
    g "I began to think about my own weaknesses before my attention was pulled back to reality. "
    g "Without me even realizing it the rest of the drive had proceeded."

    stop sound fadeout 1

    stop music fadeout 1

    scene bg courtyard
    with fade

    J "Well..."

    F "Jesus christ can we stop tip-toeing around this? His dad died today, maybe" #CONTINUE SCRIPT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#GAME END
    g "You've reached the end of the script for now."
    g "Thanks for playing!"
return
