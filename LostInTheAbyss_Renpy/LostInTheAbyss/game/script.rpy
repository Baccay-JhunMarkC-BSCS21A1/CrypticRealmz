# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image Daichi = "Daichi_Suit.png"
image Aoi = "Aoi_Suit.png"

define aoi = Character("Aoi")
define emi = Character("Emi")
define daichi = Character("Daichi")
define miyu = Character("Miyu")
define satoshi = Character("Satoshi")
define kawa = Character("Kawa")
define kenji = Character("Kenji")
define hana = Character("Hana")
define gen = Character("Gen")
define takiyo = Character("Takiyo")

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
    show Emi
    emi "Work. Always work. Aoi, we promised. Somewhere by the sea, remember? Just you and me. No distractions."
    pause 3.0
    "Emi approached Aoi with a soft look in her eyes, placing her hand on his."

    emi "Let’s make it happen, okay?"
    hide Emi
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
    jump PS2
        
    return

label PS2:
    pause 2.0
    "(The briefing room buzzed with faint murmurs as the Sub/merge crew gathered for their final meeting before the descent.)"
    "(The lights were dim, the screen at the front displaying an artist’s impression of a submerged metropolis, its spires stretching eerily toward the ocean’s surface.)"
    "(Despite the sense of awe the image inspired, the atmosphere was heavy with tension.)"
    "(Aoi Nishihara sat quietly at the back, his fingers gripping a cup of coffee gone cold. His sharp eyes, lined with dark circles, flicked across the room, scanning his crewmates.)"
    "(They were some of the best in their fields, but he wondered if even their expertise could prepare them for what lay ahead.)"
    "(At the front of the room, Chief Daichi stood tall, his presence commanding the room's attention. His voice carried a calm confidence, but there was an edge to it, a kind of hunger that Aoi couldn’t ignore.)"
    scene bg_meetingrm
    with fade
    pause 2.0
    show Daichi
    daichi "Ladies and gentlemen, what we’re about to undertake is unprecedented. This isn’t just another expedition—it’s a journey into the unknown. The city we’re about to explore is unlike anything humanity has ever discovered."
    daichi"It’s ancient, untouched, and, most importantly... it’s ours to uncover."
    "(The screen shifted to show sonar scans of the submerged city, its sprawling ruins faint but unmistakable.)"
    daichi "Our government has invested heavily in this mission because of what this city could mean for science, history... and perhaps even our survival."
    daichi "If the materials we’ve detected are as advanced as they seem, this could redefine our understanding of ancient civilizations—and of humanity itself."
    hide Daichi
    scene black
    with fade
    window hide
    pause 3.0
    window show
    "(The murmurs grew louder as the implications of Daichi’s words settled over the crew. The stakes weren’t just professional—they were monumental.)"
    "(Aoi leaned back in his chair, his jaw tightening as Daichi spoke. He had been handpicked for this mission, not just for his technical expertise but for his level-headedness under pressure.)"
    "(But no amount of training could quell the unease gnawing at him.)"
    "(His thoughts drifted to the application form he had filled out months ago—the only thing that had kept his mind occupied since...)"
    "(Since the accident.)"
    window hide
    jump PS3
    return

label PS3:
    scene bg_submarinebay
    with fade
    pause 3.0
    window show
    "(The submarine bay was alive with activity as the Sub/merge crew gathered for their final briefing. The hulking mass of the submarine loomed over them, its sleek design both awe-inspiring and imposing.)"
    "(Floodlights bathed the dock in a cold, sterile glow, illuminating the faces of the 14-member team. Despite the air of professionalism, tension crackled beneath the surface.)"
    "(Daichi, the chief of the expedition, stood front and center, his posture rigid and commanding. His sharp, calculating eyes scanned the team as they assembled. Each member carried their own expertise—and their own burdens.)"
    show Daichi at left
    daichi "Ladies and gentlemen, this is it. We are standing on the brink of history. What lies below isn’t just a city—it’s a key to understanding civilizations far older than we ever imagined."
    daichi "But make no mistake, this mission is not without risks. Once we descend, the ocean will test us. The city will test us. I expect each of you to perform your roles with precision and discipline."
    "(His words hung in the air, heavy with unspoken implications.)"
    "(Miyu stepped forward, her calm demeanor and compassionate voice a contrast to Daichi’s cold authority.)"
    window hide
    show Daichi at left
    show Miyu at right
    pause 3.0
    window show
    miyu "If anyone feels uncertain, now’s the time to speak. This mission is dangerous. There’s no shame in stepping back."
    "(No one moved. Aoi watched as her words lingered, the crew exchanging glances. He caught Rikona’s expression—her analytical eyes scanning the submarine’s hull as though calculating its odds of survival.)"
    show Daichi at left
    window hide
    hide Miyu
    hide Daichi
    pause 1
    "(Satoshi and Kawa adjusted their tool belts, their banter subdued for once.)"
    pause 0.5
    show Satoshi at left
    window show
    satoshi "This baby’s solid. We’ll keep her running no matter what."
    pause 0.5
    show Kawa at right
    kawa "*smirks*, Unless, of course, something bites through her first.s"
    window hide
    hide Satoshi
    hide Kawa
    pause 0.5
    show Kenji at left
    window show
    "Kenji, the team’s security expert, rolled his eyes and tapped his holstered harpoon gun."
    kenji "If something bites, I’ll make sure it regrets it."
    window hide
    hide Kenji
    pause 0.5
    show Hana at right
    window show
    "Hana, the marine biologist, couldn’t hide her excitement despite the somber atmosphere. Her wide eyes darted toward the holographic projection of the submerged city."
    hana "Do you think we’ll find life down there? New species, maybe? I’ve been dreaming of this since grad school."
    pause 0.5
    show Gen at left
    "(Gen, the diver specialist, crossed his arms with a wry grin.)"
    gen "Let’s hope whatever we find doesn’t dream of eating us."
    window hide
    hide Gen
    hide Hana
    pause 2.0
    window show
    "(The room chuckled nervously, but Takiyo, the communications specialist, remained focused on her tablet, running diagnostics.)"
    show Takiyo at right
    takiyo "Surface comms are stable for now, but don’t expect miracles once we’re under. The ocean doesn’t like to play nice."
    hide Takiyo
    window hide
    scene black
    with fade
    jump PS4
    return

label PS4:
    pause 3.0
    "(Aoi stayed quiet, observing the crew. They were a mix of personalities—brilliant, resourceful, and occasionally clashing. But beneath the banter, he could sense the tension in their movements, the weight of the unknown pressing on them all.)"
    "(His own thoughts drifted to Emi, her memory never far from his mind. He touched the photograph tucked inside his suit’s chest pocket—a small gesture of connection to a world that felt increasingly distant.)"
    window hide
    pause 3.0
    window show
    "???" "-hara. Nishihara. Hey Mr. Nishihara-"
    daichi "-you’re the calm in the storm. Make sure you stay that way."
    "(Aoi met his gaze and nodded.)"
    window hide
    pause 3.0
    window show
    aoi "Always."
    window hide
    jump PS5
    return
label PS5:
    scene bg_submarinebay
    with fade
    pause 1.0
    show Daichi
    window show
    "(Daichi turned to the holographic projection of the submerged city, his tone shifting to one of clinical precision.)"
    daichi "Our initial scans show the city is spread across five major sectors, with the central spire being our primary target. It’s where we’ll find the artifacts that could redefine history."
    daichi "Navigating the ruins won’t be easy. Toshiko, you’ll lead the mapping effort. We can’t afford to get lost."
    daichi "Hideyo, you’ll work with Rikona to decode inscriptions and study the ruins. The rest of you know your roles. Stick to them."
    "(His gaze swept over the team, lingering on Haruto, who stood silently at the edge of the group.)"
    hide Daichi
    scene black
    jump PS6
    return

label PS6:
    pause 1.5
    scene bg_submarine
    with fade
    pause 1.5
    window show
    "(As the crew filed into the submarine one by one, their conversations quieter now. The enormity of what lay ahead was finally sinking in. Aoi stood at the hatch, watching as each member disappeared inside. Miyu paused beside him.)"
    show Miyu at right
    miyu "Are you ready for this?"
    show Aoi at left
    aoi "*hesitant* I don’t think anyone can be ready for something like this. But we’ll get through it."
    "(Miyu smiled faintly, then climbed aboard. Aoi followed, the cold metal of the hatch sealing behind him like a tomb.)"
    
    return