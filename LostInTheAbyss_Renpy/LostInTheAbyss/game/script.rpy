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
    window hide
    pause 3
    with fade
    jump PS1
    return

label PS1:
    window show
    "*beep beep beep*"
    window hide
    pause 1.5
    window show
    aoi "-gasp!"
    window hide
    scene bg_bunk
    with fade
    pause 2.0
    window show
    "(Aoi, drenched in sweat, sat up in his bunk clutching the edge of the mattress.)"
    "(He looked down at his hands—they were trembling. His wedding ring caught the dim light, the cool metal pressing into his skin like a reminder.)"
    aoi "Emi... I didn't let you go..."
    window hide
    pause 1.5
    window show    
    "Aoi closed his eyes, steadying his breathing. He knew he wouldn’t sleep again that night."
    scene black
    with fade
    "“You’ll let them go too.”"
    aoi "..."
    jump PS3
        
    return

label PS3
    pause 2.0
    "(The briefing room buzzed with faint murmurs as the Sub/merge crew gathered for their final meeting before the descent. The lights were dim, the screen at the front displaying an artist’s impression of a submerged metropolis, its spires stretching eerily toward the ocean’s surface. Despite the sense of awe the image inspired, the atmosphere was heavy with tension.)"
    "(Aoi Nishihara sat quietly at the back, his fingers gripping a cup of coffee gone cold. His sharp eyes, lined with dark circles, flicked across the room, scanning his crewmates. They were some of the best in their fields, but he wondered if even their expertise could prepare them for what lay ahead.)"
    "(At the front of the room, Chief Daichi stood tall, his presence commanding the room's attention. His voice carried a calm confidence, but there was an edge to it, a kind of hunger that Aoi couldn’t ignore.)"
    scene bg_meetingrm
    with fade
    pause 2.0
    show Daichi
    "Daichi: Ladies and gentlemen, what we’re about to undertake is unprecedented. This isn’t just another expedition—it’s a journey into the unknown. The city we’re about to explore is unlike anything humanity has ever discovered. It’s ancient, untouched, and, most importantly... it’s ours to uncover."
    
    # This ends the game.

    return
