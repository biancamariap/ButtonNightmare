# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bianca", who_color="#faa5f5")
define m = Character("Mariie", who_color="#b0e9f0")
define a = Character("Adi", who_color="#f8ed90")
define om = Character("Other Mother", who_color="#000000")

image book animated:
    "book.jpg"
    pause 1.0
    "book1.jpg"
    pause 1.0
    "book2.jpg"
    pause 1.0
    "book3.jpg"
    pause 1.0
    "book4.jpg"
    pause 1.0
    "book5.jpg"
    pause 1.0
    "book6.jpg"
    pause 1.0
    repeat

# The game starts here.
label splashscreen:
    scene black
    with Pause(1)
    play music "audio/elegant_logo.mp3"
    show text "{i}{size=45}{color=#ffffff}Artwork and story reinterpretation belong to...{/color}{/size}{/i}" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show text "{i}{size=45}{color=#ffffff}Nagy Adrian, Pîrvu Bianca & Trașcă Maria {/color}{/size}{/i}" with dissolve
    with Pause(2)

    hide text with dissolve

    return

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black
    show book animated
    play music "audio/enigmatic.mp3" fadeout 0.5 fadein 0.5
    "{i}{size=45}This visual novel was inspired by the Coraline book and movie.{/size}{/i}"
    "{i}{size=45}Hope you'll enjoy!{/size}{/i}"

    scene bg pink
    with fade

    #INTRO
    "Adi, Bianca and Mariie are 3 brothers who just moved into the Pink Palace apartment complex with their mother."

    show bianca at center
    with dissolve

    show mariie at right with dissolve:
        xzoom -1

    show adi at left
    with dissolve

    "However, things start to get creepy when they discover a hidden little door inside their livingroom."
    #stop music fadeout 1.0
  #SCENA 3
    scene bg closeddoor
    with fade
    "You will have to help the kids discover what is behind the door and guide them through their new adventure."
    "You will be faced with difficult choices."
    "Be wise. Be Brave. Be tricky."
    show bianca at left
    with dissolve

    play sound "audio/knock.mp3"

    menu:

        b "Should we look for a key to open this little door?"

        "Yes, let's look for the key!":

            jump look

        "No, let's forget about it.":

            jump dontlook

label dontlook:
    scene bg closeddoor
    with fade
    play sound "audio/failt.mp3"
    "{i}Oh, no, you should've tried harder. Better luck next time!{/i}"

    scene black
    with dissolve

    "{i}Bad Ending{/i}."

    return


label look:
    scene bg closeddoor
    show mariie at right with dissolve
    show mariie:
        linear 1.0 xalign 0.0
    menu:

        m "Where should we look first?"

        "I think the kitchen is a good place to start!":

            jump kitchen

        "Maybe it's in the bathroom.":

            jump bathroom

label bathroom:
    scene bg bathroom
    with fade
    show adi at left
    with dissolve
    show adi:
        linear 1.0 xalign 1.0
        xzoom -1
    a "I looked everywhere, it's not in here!"
    menu:

        a "Should we look through the kitchen?"

        "Definitely!":

            jump kitchen



 #SCENA 4
label kitchen:
    scene bg kitchen
    with fade
    show adiwow at right with dissolve:
        xzoom -1
    play sound "audio/keys.mp3"

    show bkey with dissolve:
        xzoom 0.5
        yzoom 0.5
        ease 1.0 truecenter

    a "I found the key! It has a peculiar shape. It must be it."



 #SCENA 5
    scene bg pinktunnel
    with fade
    play music "audio/tunel.mp3" fadeout 1.0 fadein 1.0
    "Hooray, the kids unlocked the door which revealed a peculiar looking tunnel. Be clever, the journey has only just begun."
    show bianca at left
    with dissolve
    menu:

        b "I’m kind of scared. Should we stay here?"

        "No way! Let's go on an adventure!":

            jump drawingroom

        "Yes, let's forget about it.":

            jump stay

label stay:
    scene bg pinktunnel
    with fade
    play sound "audio/failt.mp3"
    "{i}Oh, don't be so faint-hearted. Better luck next time!{/i}"
    scene black
    with dissolve

    "{i}Bad Ending{/i}."

    return


#SCENA6
label drawingroom:
    scene bg drawingroom
    with fade
    "The kids travelled through the tunnel but ended up in the same place."
    show bianca at right
    with dissolve
    show bianca:
        linear 1.0 xalign 0.5
        xzoom -1
    show adiwow at right
    with dissolve
    show adiwow:
        linear 1.0 xalign 0.0
    a "I don’t get it, we’re still in the same room that we just left."
    show mariiehappy at left
    with dissolve
    show mariiehappy:
        linear 1.0 xalign 1.0

    m "That's curious..I smell something good, lets check the kitchen."


#SCENA 7
    scene bg kitchen
    with fade
    play music "audio/enigmatic.mp3" fadeout 1.0 fadein 1.0
    show othermother at center
    with dissolve

    show mariieangry at left
    with dissolve
    show mariieangry:
        linear 1.0 xalign 1.0
        xzoom -1
    m "Mom..What happened to your eyes?"
    show adiwow at right
    with dissolve
    show adiwow:
        linear 1.0 xalign 0.0
    a "Our mother doesn’t have b..b..b…."

    show othermother:
        xzoom -1
    om "Buttons! I'm your other mother, silly!"
    om "Everyone has one. We're like the better version of your mother."
    show othermother:
        xzoom 1
    om "You're in a parallel world, so to speak, a better world...Come join me for dinner now!"


#SCENA 8
    scene bg table
    with fade
    show othermother at center
    with dissolve

    show adi at left
    with dissolve

    show mariie at right with dissolve:
        xzoom -1

    show bianca with dissolve:
        yalign 1.0 xalign 0.8
        xzoom -1
    with dissolve
    play sound "audio/plates.mp3"
    m "That was delicious!"
    hide adi
    show adiwow at left
    a "Our mother never cooks like that!"
    show othermother:
        xzoom -1
    om "You can stay here forever if you want. There’s only one little thing you have to do…"
    stop sound

#SCENA SUPLIMENTARA
    scene bg buttons at Zoom((1280, 720), (0, 0, 800, 600), (225, 150, 400, 300), 1.0)
    scene bg buttons at Zoom((1280, 720), (225, 150, 400, 300), (0, 0, 1280, 720), 1.0)
    play music "audio/carnavalcreepy.mp3" fadeout 1.0 fadein 1.0
    "In order to stay here... the kids have to sew buttons into their eyes."

#SCENA 9
    scene bg buttons
    show biancasad at center
    with dissolve

    show adisad at left
    with dissolve

    show mariiesad at right
    with dissolve

    menu:

        b "Should we sew buttons into our eyes? I have a bad feeling about it.."

        "No way! Let's go home.":

            jump home

        "Yes, of course!":

            jump buttons

label buttons:
    scene bg buttons
    with fade
    show othermother at center
    with dissolve
    om "You fools, now you're going to stay here and I will {i}love{/} you forever!"

    scene black
    with dissolve
    play sound "audio/failt.mp3"
    "{i}Oh no! What have you done? Now the kids are trapped!{/i}"
    "{i}Bad Ending{/i}."

    return


label home:
    scene bg buttons
    play music "audio/enigmatic.mp3" fadeout 0.5 fadein 0.5
    show adi at right
    with dissolve
    show adi:
        linear 1.0 xalign 0.0
        xzoom -1
    a "I think we need more time to decide.."

    show mariie at left
    with dissolve
    show mariie:
        linear 1.0 xalign 1.0
    m "We’re tired now, we'll go to sleep and think on it.."


#SCENA10
    scene bg bedroom
    with fade
    play sound "audio/floors.mp3"
    show adiwow at right
    with dissolve
    show adiwow:
        linear 1.0 xalign 0.0
    a "Bianca, why aren't you sleeping?"

    show biancasad at center with dissolve:
        xzoom -1
    b "Shh, wake up Mariie and let's sneak out till the other mother catches us. I want to go home!"
    stop sound

#SCENA11
    scene bg drawingroom
    with fade
    play music "audio/tobetribale.mp3" fadeout 0.5 fadein 0.5
    play sound "audio/tocuri.mp3"
    show othermotherangry at left with dissolve:
        linear 1.0 xalign 0.5

    om "And where do you thing you're going?"
    stop sound
    show mariiesad at left
    with dissolve
    show mariiesad:
        linear 1.0 xalign 1.0

    show adiangry at left
    with dissolve
    show adiangry:
        linear 1.0 xalign 0.9

    show biancasad at left
    with dissolve
    show biancasad:
        linear 1.0 xalign 0.8


    a "Let us go, witch!"
    show othermotherangry with dissolve:
        xzoom -1
    om "I just want to love you.."

    show mariiesad with dissolve:
        xzoom -1
    m "What can we do, guys?"
    show othermotherangry:
        linear 1.0 xalign 0.0
    om "I have an idea! I love games. How about you answer a riddle for me?"
    om "If you answer correctly, I promise to let you go back to your boring lives.."
    show adiangry with dissolve:
        xzoom -1
    show biancasad with dissolve:
        xzoom -1
    b "We'll do it!"
    menu:

        om "Flat as a leaf, round as a ring. Has two eyes, can't see a thing. What is it?"

        "A button.":

            jump run

        "A coin.":

            jump dontupset

label dontupset:
    scene black
    with dissolve
    play sound "audio/failt.mp3"
    "{i}Oh no! What have you done? Now the kids are trapped forever!{/i}"
    "{i}Bad Ending{/i}."
    return



#SCENA12
label run:
    scene bg drawingroom

    show othermother at left:
        xzoom -1
    show mariie at right:
        xzoom -1

    show adi:
        yalign 1.0 xalign 0.9
        xzoom -1

    show bianca:
        yalign 1.0 xalign 0.8
        xzoom -1

    om "Oh no! You think you're so smart...Go now, till I don't change my mind!"
    show bianca:
        yalign 1.0 xalign 0.8
        xzoom 1
    b "Quick, through the door!"

#SCENA suplimetara
    scene bg closeddoor
    with fade
    play music "audio/enigmatic.mp3" fadeout 0.5 fadein 0.5
    show bianca at left with dissolve:
        linear 1.0 xalign 0.5
    pause 1.0

    show adi at right
    with dissolve
    show adi:
        linear 1.0 xalign 0.0
    a "Lock the door now!"
    play sound "audio/unlockdoor.mp3"
    show mariie at left
    with dissolve
    show mariie:
        linear 1.0 xalign 1.0
    m "We're safe! Lets go find our real mother. She'll never believe us!"
    stop sound

#SCENA13
    scene black
    with dissolve
    play sound "audio/success.mp3"
    "{i}Congrats, brave soul, you helped the kids in this adventure.{/i}"
    "{i}Watch out for the other mother, however, and for people with buttons instead of eyes.{/i}"
    "{i}Good Ending{/i}."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # This ends the game.

    return
