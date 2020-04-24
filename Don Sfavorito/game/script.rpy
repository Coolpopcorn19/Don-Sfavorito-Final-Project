# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

$menu_flag

define g = Character("")
define G = Character("Giorno")
define B = Character("Bucciarati")



# The game starts here.

label start:
    play music "audio/track.mp3" #fadeout 1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg lounge
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    G "I have a dream."

    G "Unfortunately, it's a difficult one to achieve."

    G "Also unfortunately, the storyline has not yet been finalized."

    scene bg cellar
    with fade

    G "I've come to realize it would be cool to use Part 5 JoJo names though."

    B "Good idea Giorno!"

    menu:
        g "Sorry to disappoint."

        "Git gud":
            jump choice1_1

        "Sad":
            jump choice1_2



    label choice1_1:
        $menu_flag = True

        g "F"

        jump choice1_done

    label choice1_2:
        $menu_flag = False

        g ":("

        jump choice1_done


label choice1_done:

#continue

    g "Which option did you choose?"

    if menu_flag == True:
         g "Looks like \"Git Gud\" Option was chosen"

    else:
        g "Looks like \"Sad\" Option was chosen"

    g "More story to come next week."

    g "If there turns out to be a peer evaluation, please let me know if you think this format will work for a mafia like story. Character images will not be used,
        and instead backgrounds and music will be used to set the mood and tone of the story."



# This ends the game.

    g "Thanks for playing!"
return
