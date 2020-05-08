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
default choice10var = 0


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
#define K = Character("Jojo")
define S = Character("Sophia")



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
    g "He lays here, dying of lead poisoning. Due to his line of work, he must surely have been exposed to toxic conditions over the years."
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

    scene bg courtyard5
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

            hide giorno normal
            hide mista normal
            with moveoutright

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
    show giorno normal at left
    show mista normal at midleft behind giorno
    show fugo normal at midright
    show abbacchio normal at right behind fugo
    with fade


    g "Mista and the rest of the gang led me into the back room of a casino."
    g "I'm a touch shocked at how young the crew is."
    g "The oldest member stands at the back of the room, I figure he’s in his late 20s."

    hide mista
    hide fugo
    with dissolve


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

    hide giorno
    hide joseph
    hide fugo
    with moveoutleft

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
        g "and i walked away from the game never to be seen again......"
        return
#CONTINUE
label choice9_done:
    O "Good luck then Giorno."

    g "He gestured with his hands out of the door."
    g "It might’ve been a good idea to say something nice then but all I could do was leave fast."
    g "Joseph and Fugo followed quickly after me. I guess they we’re trying to give the impression of unity."
    g "They must have been loyal to my father, but maybe that’s just something I want to believe."

    hide giorno with moveoutleft

    stop music fadeout 1

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
    g "The clock on the dashboard read 6:47. Quickest 7 hours of my life."
    g "This afternoon I was begging for a miracle, now I’d be killing someone while they’re begging for the same thing."
    g "I could have left though, from here on out, Its all or nothing."
    g "The drive proceeded in silence. While we were arriving I realized what piece Moretti would be; the king."
    g "He might be a great leader but his individual strength was remarkably weak."
    g "Relying on cruelty over tactics has left him with an incredible blind spot. But he was the man giving ME the orders."
    g "I began to think about my own weaknesses before my attention was pulled back to reality. "
    g "Without me even realizing it the rest of the drive had proceeded."

    stop sound fadeout 1

    J "Well..."

    F "Jesus christ can we stop tip-toeing around this? He knows what’s gonna happen so let’s just test his metal and let him mourn in peace."

    G "I agree, today has felt ungodly long."

    J "Sorry."

    g "Joseph looked at me with a touch of shame in his face, I gave him a small smile back."
    g "Its nothing personal Jojo, I just want to get this over with."


    play music "audio/track4.ogg" fadeout 1

    scene bg garage1
    show giorno normal at right
    show fugo normal at left
    with fade

    g "I got out of the car to see a red brick building with a large metal sliding garage."
    g "It appeared to be some sort of warehouse. The sun was hanging low over the horizon now, I might have appreciated the colors on a different day."
    g "Fugo started walking to the gate while pulling a pack of classic red Marlboros from his pocket."
    g "He slid a cigarette into his mouth and lit it before fishing a small set of keys from his pants."
    g "He unlocked the door and slid it open."

    scene bg meatlocker1
    with fade

    g "Rows and rows of cow abdomens hung from hooks in the ceiling, and a burst of cold air hit me."
    g "Joseph solemnly walked in, Fugo gestured at me as if to say 'after you'."

    show giorno normal at left
    show fugo normal at right
    show joseph normal at midright behind fugo
    with dissolve

    g "I walked in and the cold became uncomfortable. I followed Jojo while Fugo closed the door behind us."
    g "Vaguely blue fluorescent lights lit the room, their flicker was annoying to me but I had different things on my mind."
    g "Jojo took a left and that’s when I saw her."
    g "Young but no younger than early to mid 20s, she was wearing a shirt with some band I’d never heard of. Her jeans were torn below the left knee rather significantly."
    g "She spoke first."

    Q "Please..."

    g "Fugo’s voice cut like a knife."

    F "SHADDAP! We chase you around for a year and a half, and once we get you it’s,"

    g "Fugo’s tone shifted to something close to Falsetto."

    F "“Oh let’s talk, let’s make a deal, I would never do it again.”"

    J "Fugo relax."

    g "Joseph's tone made it clear that it was an order, not a request."

    F "Whatever man all these coke heads are the same. I mean I like a bump every now and then too, but running from Mob debt? That’s just dumb."

    J "Fugo I swear to God-"

    F "Fine, fine. I’m done."

    g "Fugo's hand slipped under his shirt near the back of his pants and pulled out a pistol. It seemed to be an M1911. He spun it in his hand and held the handle towards me."

    F "Merry Christmas."

    g "I couldn’t help but a scoff a little."

    G "Thanks."

    g "I’d held a lot of guns before, but this one felt heavier, almost as if it shared my burden."

    g "The woman began to sob silently. I moved to stand in front of her."
    g "I lifted my arm, I’d practiced with firearms out of principle but I’d never shot anything with a heart before. Whatever happens I’ll carry the weight."

    hide fugo
    hide joseph
    with dissolve

    show giorno normal at center with move

    #CHOICE 10 ENDINGS
    if trueMobster > 2:

        menu:
                "*Pull the trigger*":
                    jump choice10_1

                "*Lower the gun*":
                    jump choice10_2

                "*Do what's right*":
                    jump choice10_3

        label choice10_1:
                $choice10var = 1

                jump choice10_done

        label choice10_2:
                $choice10var = 2

                jump choice10_done
        label choice10_3:
                $choice10var = 3

                jump choice10_done

    else:

        menu:
                "*Pull the trigger*":
                    jump choice10_4

                "*Lower the gun*":
                    jump choice10_5

        label choice10_4:
            $choice10var = 1

            jump choice10_done

        label choice10_5:
            $choice10var = 2

            jump choice10_done
#CONTINUE
label choice10_done:

    if choice10var == 1:

        stop music fadeout 1

        play sound "audio/gunshot.wav"
        with vpunch
        play sound "audio/gunshot.wav"
        with vpunch

        g "I put two in her stomach as close to her spine as I could. The way she stopped completely let me know I hit it, good, at least for it to be painless."

        g "I pulled a handkerchief from my pocket and wiped off the handle. I threw the gun back to Fugo."

        show giorno normal at left with move

        show fugo normal at right
        show joseph normal at midright behind fugo
        with dissolve

        F "It gets easier, never feels good but it gets easier."

        g "Joseph gave me a look of understanding, but I could sense his sadness."

        J "Welcome to the family Gio. It’ll be a lot better having you at my back."

        G "Of course Jojo."

        g "The flicker of the lights was beginning to make me slightly nauseous, or maybe it was the dead girl three feet from me. Either way I began walking away and they followed shortly after."

        F "So boss man is it too early to talk raises?"

        g "I smiled just for a second. Fugos manic positivity made more sense to me now."

        G "Much too early."

        g "Those were the last words spoken between us until we arrived back at the casino."


        play music "audio/track3.ogg" fadeout 1
        scene bg casino
        show giorno normal at left
        with fade

        g "I hugged Joseph and he began his drive back home."
        g "The clock on my phone read 10:27. Jesus this was the quickest 11 hours of my life."
        g "My hand began to shake a little but I willed it to calm down."
        g "I let myself fall into the Boss’s chair as soon as I got in the back."
        g "It was leather with small gold studs. I began to run my finger over them."

        show abbacchio normal at right
        show mista normal at center behind abbacchio
        show fugo normal at midright behind abbacchio
        with dissolve

        A "Fugo, Mista, give me some time alone with the boss will ya?"

        F "Sure man."

        M "O’course."

        hide mista
        hide fugo
        with dissolve

        g "Abbachio walked slowly to a cabinet and pulled out a glass bottle filled with brown liquid. He opened a small metal container and took out two glasses."
        g "He dropped an ice cube in each glass from the same container."
        g "He brought both glasses over to my desk and set one in front of each of us."
        g "He poured the liquid into each container for approximately 4 seconds each."

        A "You like Scotch?"

        G "Not even remotely."

        g "I finished the drink in one pull of the glass."

        A "Hah, want another?"

        G "In a bit. When did you pull the stick out of your ass?"

        A "When you became one of us. I couldn’t trust a child to have my back, and you proved you’ve at least have some stones."
        A "This isn’t an easy path, it's good to know you walk it right. Welcome to the family."

        g "I poured myself a second drink and offered out my glass."

        G "To freedom and the future."

        A "Salud."
        return

    if choice10var == 2:

        stop music fadeout 1

        g "I lowered the gun."
        g "No, no this isn’t my path."
        g "Nobody had the right to kill my father, but he was pushed to death. Nobody has the right to take this womans life either."
        g "Not me, and certainly not Moretti."

        #play music "audio/giorno.ogg" fadeout 1

        show giorno normal at left with move

        show fugo normal at right
        show joseph normal at midright behind fugo
        with dissolve

        G "No, I won’t be Moretti's hitman. I’m not killing some druggie who got in over her head and I’m never gonna follow a man like Moretti. Joseph let her down."

        g "Joseph looked at me with shock."

        J "I ca.. Gio I can’t do that."

        F "HAHAHAHAHAHA LIKE FATHER LIKE SON."

        g "I glared at Fugo."

        F "Wipe that look off your face princess."

        g "Fugo pulled out a pocket knife and began cutting her down."

        F "Your old man, he wasn’t a good mobster, in fact he was kind of a bad one. But that man treated me like a fuckin son."
        F "I wouldn’t be alive if it wasn’t for him. He was a good dad, he was kind of my dad too."
        F "So you get one freebie Giorno, I owe him that much at least."

        Q "Thank you…"

        F "So once I let you down you should go into witness protection. If I catch you in this city after right now I’ll have to cut ya up real bad. You’re gonna leave town, with or without the cops, and you’re gonna do it tonight."

        Q "Yes…"

        g "Joseph hung his head silently. The ropes split and she fell to the floor. Fugo grabbed her arm."

        F "Where are ya going?"

        Q "Out of town."

        F "When are ya going?"

        Q "Tonight."

        F "Got a regular Einstein."

        g "I looked at Joseph and Fugo, they returned my gaze. We got in the car and we didn’t share another word until 20 minutes into the ride back."

        play music "audio/track2.ogg" fadeout 1
        play sound "audio/driving.ogg" fadeout 1
        scene bg carnight
        with fade

        J "Guess I’m taking ya home. Don’t worry, when we tell Moretti you refused we’ll just say we offed her instead."

        G "Thanks Jojo."

        stop sound fadeout 1

        scene bg courtyard5
        show fugo normal at right
        show joseph normal at center behind fugo
        show giorno normal at left
        with fade

        g "Joseph stopped outside my house and I got out."

        J "Let’s grab lunch soon okay?"

        G "Of course."

        g "I started down the walkway when Fugo yelled out to me."

        F "Hey Gio, part of me wishes the same call, enjoy the freedom."

        G "You too."

        g "He smiled widely at me and they drove away. I’m glad I didn’t join, my father only did this out of necessity."

        hide fugo
        hide joseph
        with dissolve

        g "Killing people who just got overwhelmed will never by my style. Besides, I never wanted to be 'Dons Favorito'."
        return

    if choice10var == 3:

        stop music fadeout 1
        play music "audio/giorno.ogg" fadeout 1

        g "I aimed the gun a little higher, I closed my left eye and fired once."

        play sound "audio/gunshot.wav"
        #with hpunch
        g "The ropes unspooled and she fell to the ground."

        show giorno normal at left with move

        show fugo normal at right
        show joseph normal at midright behind fugo
        with dissolve

        F "Dude what the FUCK?"

        G "Relax babe. Jojo, get the car for us."

        J "What?"

        G "Joseph I’m not gonna ask ya twice."

        g "Joseph stared at me for a moment, I returned his gaze. He left after a moment."

        hide joseph with dissolve

        G "Fugo, bum me a smoke."

        g "Fugo stared at me with an open mouth. Then a slight grin grew onto his face, it's good to see he figured it out."

        F "You got it boss."

        show fugo normal at center with move

        g "He handed me the cigarette which I promptly put into my mouth. He fished his lighter out of his pocket and lit it for me."

        G "What’ your name girl?"

        Q "So-Sophia."

        G "Sophia, get the hell outta here, your debts forgiven."

        S "What?"

        G "I said go home, rest up."

        S "What about Mo-Moretti?"

        G "That fucker?"

        g "I ashed my cigarette."

        G "He’s good as dead."

        g "A car honk could be heard outside, I motioned with my head for Fugo to follow me and headed out. Fugo and I promptly entered."

        scene bg carnight
        with fade

        J "Gio I-"

        G "Moretti’s office please, we gotta talk."

        J "I love you man, please don’t-"

        F "Who died and made you Capo? Your boss just gave you an order."

        G "Fugo! You’ll show Joseph some more respect. Now Jo-"

        g "Jojo's eyes stared straight ahead now, unwilling to meet mine and completely determined. Finally."

        J "No problem Boss. Sorry for taking this long."

        G "Hey, it's always Gio for you Jojo."

        g "He smirked now."

        J "Course bro."

        play sound "audio/driving.ogg" fadeout 1

        g "We didn’t say another word the rest of the ride."
        g "I could tell Fugo was steeling himself, Jojo’s focus didn’t break at all."
        g "It was a little surprising honestly. I never knew he had this side to him."
        g "We pulled up outside of Morettis."

        stop sound

        F "Giorno I need that piece. Joseph keeps a spare in the glove compartment."

        G "What, is it lucky?"

        F "It was your dad’s, he gave it to me, he um… he was good to me. So now if I think I might die doing some shit I always use that gun. You’re the boss so o-"

        G "All Yours."

        g "I handed him the gun, I got Fugo a little more now."
        g "I understood now that his manic energy was just something to cope. He was a killer no doubt, but shit he was still a kid."
        g "I popped open the glove compartment and saw a black Beretta. I turned on the safety and slipped it into my belt."

        G "No time like the present."

        g "I got out and slammed the door. I wouldn’t work for Moretti, and I couldn’t let the man who pushed my dad to his death live either."
        g "Success or failure didn’t matter, this was principle."

        scene bg restaurant
        show joseph normal at left
        show giorno normal at center
        show fugo normal at right behind giorno
        with fade

        g "I opened the door to Stratiacellis, it was 9:40 now, only the late diners were still here."
        g "The hostess tried to say something but stopped quickly."
        g "I could hear my heartbeat in my ears, but my expression remained a deadly neutral. I didn’t wanna die, but I also couldn’t help but be a little excited for this."
        g "I saw my father come home every day looking like he had his fuckin’ heart ripped out of chest."
        g "He was a good dad, a bad mobster maybe, but he didn’t deserve to die of lead poisoning, and any Don that respected him wouldn’t have been sending him out on hits at his rank."
        g "By the time I refocused from my thoughts I was up the stairs and outside the door to Moretti's lounge. I pushed open the door and stepped inside."

        define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

        scene bg lounge
        show giorno normal at right
        show moretti normal at left
        with flashbulb

        O "Giorno, I’m sure you must know we have protec-"

        play sound "audio/gunshot.wav"
        with vpunch
        play sound "audio/gunshot.wav"
        with vpunch

        g "I slipped the Beretta out from my waistband and put two in his chest. The men in suits behind him went for their guns but Fugo and Jojo already had their weapons trained on them."

        hide moretti with dissolve
        show giorno normal at midleft with move


        show joseph normal at midright behind giorno
        show fugo normal at right
        with dissolve



        F "EY, RELAX. Come on Donny, think about Max."

        g "This seemed to take the steam out of one of the men that stood behind Moretti, assumably Donny."

        G "Gentlemen I have no intention of firing you, I mean I wouldn't want you guys as my guards of course."

        g "Fugo chuckled."

        G "But really, I’m not here to shake up the whole system. Just think of it as working under new management."

        hide fugo
        hide joseph
        with dissolve

        g "Fugo shared some words with the men, until the tension decreased enough for Jojo and him to lower their weapons."
        g "Of course they weren’t angry, Moretti treated his men like shit. They left pretty quickly and I sat in my new chair."

        show giorno normal at left with move

        g "I breathed out deeply and released the tension from the day. My fatigue hit me all at once."
        g "I sunk into my chair a little lower. I realized then how childish it was to compare us all to chess pieces, this isn’t a game, people die."
        g "In real life, sometimes the way to win is to burn the board. Joseph's voice broke my mind away from my thoughts."

        show joseph normal at center behind giorno
        show fugo normal at right
        with dissolve

        J "So… What’s first on the docket?"

        G "My father needs a funeral, and we could use something to acquaint me with the Capos so we’ll have an Irish wake afterwards."

        F "...He was a good man."

        G "And so he was a poor mobster."

        g "I pulled glasses from the same drawer I saw Moretti pull from earlier. I poured us three glasses of whatever liquid was in the same drawer. This bottle read 'Limoncello'."

        G "But the best fuckin father some mafiosos like us could hope for."

        g "I raised my glass and they did the same."

        G "To our father, to the future."

        J "To Dio! Salud!"

        F "SALUD!"

        hide joseph
        hide fugo
        with dissolve

        show giorno normal at center with move

        g "Don’t worry pops, I’ll use our money to help people out, the mob will become a symbol of hope. I know that sounds insane, but I think it’ll be a mob you could be proud of."
        g "I love you dad, I hope you find more peace in the next life than you did in this one."
        return

#GAME END
    g "Thanks for playing!"
return
