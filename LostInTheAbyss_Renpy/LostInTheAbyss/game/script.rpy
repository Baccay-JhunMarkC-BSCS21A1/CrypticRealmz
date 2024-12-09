# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define aoi = Character("Aoi")
define emi = Character("Emi")
define daichi = Character("Daichi")



# The game starts here.

label start:
    scene black with fade

    pause 3.0
    "*sea hushing*"
    window hide
    pause 3.0
    window show
    aoi "It's cold..."
    aoi "I better head back to the shore."
    window hide
    pause 3.0
    window show
    "*muffled sounds*"
    aoi "??"
    window hide
    pause 3.0
    window show
    "*laughing*"
    "???" "You swim like an old man, you know that?"
    window hide
    pause 3.0
    window show
    aoi "Someone has to be responsible. You get distracted too easily."

    "???" "Responsible, huh? That why you keep postponing our trip? I’m starting to think you don’t want to go."

    aoi "Emi, it’s not that. It’s just—"
    window hide
    pause 1.0
    scene bg_seashore
    with fade
    window show
    emi "Work. Always work. Aoi, we promised. Somewhere by the sea, remember? Just you and me. No distractions."
    pause 3.0
    "Emi approached Aoi with a soft look in her eyes, placing her hand on his."

    emi "Let’s make it happen, okay?"
    window hide
    scene black
    with fade
    window show
    "As Aoi opened his mouth to respond, the sunlight began to fade. The warm, golden glow shifted into cold, blinding headlights. A deafening screech of tires filled the air."
    pause 3.0
    "*Screech*"
    pause 1.5
    aoi "!!!"
    pause 1.55
    emi "Aoi-"
    aoi "Emi! Emi hold on-"
    window hide
    pause 3.0
    window show
    "The car spun violently, the world tilting and crashing around them. Shards of glass sparkled like stars in the darkness. Aoi reached out, his hand searching for hers."

    aoi "*cough* Emi... Emi! Are you okay? Answer me!"
    window hide
    pause 3.0
    window show
    "*Muffled mumbling*"
    window hide
    pause 3.0
    window show
    emi "...you promised Aoi! You promised you wouldn't lose me..."
    pause 1.5
    emi "You let me go- You'll let them go..."
    aoi "Emi!"

    return


    # This ends the game.

    return
