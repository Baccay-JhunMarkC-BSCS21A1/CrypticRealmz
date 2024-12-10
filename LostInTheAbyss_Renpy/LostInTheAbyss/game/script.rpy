# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image Daichi = "Daichi_Suit.png"
image Aoi = "Aoi_Suit.png"

transform ShakeEffect():
    on show:
        xpos 0 ypos 0
        linear 0.05 xpos 10 ypos -10
        linear 0.05 xpos -10 ypos 10
        linear 0.05 xpos 5 ypos -5
        linear 0 xpos 0 ypos 0

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

    window hide
    hide Miyu
    hide Aoi
    pause 3.0
    window show
    "(As the submarine powered up, the hum of the engines filled the cabin. Daichi stood at the helm, addressing the crew one final time.)"

    pause 1.0
    show Daichi
    daichi "Remember—this is history in the making. Whatever we find down there, it will be worth it."

    "(The submarine began its descent, the surface light fading into darkness. Aoi sat by a viewport, watching the ocean swallow them whole. The weight of the abyss pressed against the glass, and the shadows seemed to shift.)"
    "..."
    hide Daichi
    window hide
    scene black
    with fade
    pause 2.0
    "(In the silence, Aoi’s thoughts returned to Emi, her voice faint and distant in his mind.)"
    pause 3.0
    emi "You’ll come back, won’t you?"
    pause 1.0
    window hide
    jump C1S1A
    return

label C1S1A:
    with fade
    aoi "Depth reading... three thousand meters and descending. Everyone, gear check."
    pause 3.0
    scene bg_submarine
    with fade
    pause 3.0
    show Daichi
    window show
    daichi "We’re on track, everyone. Remember, this is the opportunity of a lifetime. A glimpse into the unknown. Not everyone is brave enough for this journey."
    pause 3.0
    hide Daichi
    "(The team was scattered throughout the cramped sub. Each member had their own role to play, each with their own thoughts racing as the darkness outside deepened, swallowing them whole.)"
    "(The city below was still a mystery to most of them, a place no one had ever returned from—or so the legends claimed.)"
    pause 3.0
    show Miyu at left
    miyu "*whispering to herself* Let’s just hope it’s worth it..."
    "(Satoshi, the engineer, sat hunched over a set of diagnostics, his brow furrowed in concentration as he scanned the readouts.)"
    show Satoshi at right
    satoshi "Power’s stable. Nothing’s cracked… yet."
    show Kawa
    kawa "*grins* Only because I made those adjustments. We’ll get there in one piece."
    window hide
    pause 3.0
    hide Miyu
    hide Satoshi
    hide Kawa
    window show
    "(Aoi took a deep breath, scanning the team. This was it—the moment they had all been waiting for, the descent into the unknown.)"
    "(But even as the words of assurance left their mouths, he couldn’t shake the nagging sense of unease gnawing at him.)"
    pause 3.0
    show Aoi at left
    aoi "Remember, once we’re down there, communication with the surface will be difficult."
    aoi "Remember, once we’re down there, communication with the surface will be difficult. Takiyo, can we keep a stable link?"
    show Takiyo at right
    takiyo "Stable enough..."
    takiyo "Stable enough... but I’d prefer not to test it too much."
    show Daichi
    daichi "Oh, we’re prepared. Let’s show the world what they’ve been missing beneath these waters."
    "(Aoi felt the weight of his words, the hollow sense of foreboding growing heavier with each passing second. He couldn't shake the feeling that they were venturing into something far darker than they anticipated."
    menu:
        "What if we can’t make it back?":
            jump C1S1B1
        "I want a full status report, now.":
            jump C1S1B2
    return

label C1S1B1:
    aoi "... what if this is all too much? What if we can’t make it back?"
    window hide
    pause 3.0
    
    window show
    daichi "Aoi, trust me. We’re doing what no one else has dared. And we will succeed. The world will remember us for this. We’re not backing out now. Not when we’re so close."
    window hide
    pause 3.0
    hide Daichi
    hide Aoi
    hide Takiyo
    window show
    "(Aoi felt his pulse quicken. Daichi’s words should have been reassuring, but something about them set him on edge. He didn’t trust this mission, not entirely, and the creeping unease gnawed at his gut."
    window hide
    jump C1S2A
    return

label C1S1B2:
    pause 3.0
    window show
    aoi "We need to make sure every system is double-checked. I want a full status report, now."
    hide Takiyo
    show Satoshi at right
    "(Satoshi looked up from his console, irritation flickering in his eyes. He had his own doubts about the mission, but pushing the team for more checks in the middle of the descent seemed like overkill.)"
    show Satoshi at right
    pause 3.0
    satoshi "Aoi, we’re fine. Relax. We’ve run these systems a hundred times. Everything’s working as it should."
    show Daichi
    pause 3.0
    daichi "This is no time for hesitation. We’re going in. You either trust us, or you don’t. We’ve prepared for this. All systems are go. No turning back."
    hide Daichi
    hide Aoi
    hide Satoshi

    "(Aoi swallowed hard, the weight of Daichi’s words sinking in. They were deep underwater now, descending further into the abyss. The familiar, comforting sound of the surface was already a distant memory.)"
    "(He couldn’t afford to show weakness, but a lingering voice inside him screamed that something was terribly wrong.)"
    window hide
    jump C1S2A

    return

label C1S2A:
    scene black
    with fade
    pause 3.0
    "(The submarine continued its descent, the dark water pressing in on all sides. Aoi's gaze shifted to the faint, flickering outline of the cursed city in the distance, a shadowy silhouette rising from the ocean floor.)"
    "(The deeper they went, the more the atmosphere seemed to thicken, the air growing heavy with the weight of the curse that loomed over the city.)"
    "(The quiet tension was broken by a sudden jolt, causing the crew to grip their seats. The sub groaned in protest, and a few of the monitors blinked out of sync. Aoi’s heart skipped a beat.)"
    window hide
    with fade
    show bg_submarine at ShakeEffect
    pause 0.3
    hide bg_submarine
    scene bg_submarine
    pause 1.0
    "Team" "?!"
    show Aoi at left
    aoi "What the hell was that?!"
    show Kawa at right
    "(Kawa quickly checked his console, his fingers flying over the keys.)"
    kawa "Nothing to worry about, just a minor fluctuation in pressure. We’re fine."
    hide Aoi
    hide Kawa
    scene black
    with fade
    pause 3.0
    "(A sharp, eerie sound reverberated throughout the sub, like something scraping against the hull. The team froze, eyes wide, as the distant shadows of the city drew closer, the feeling of isolation pressing down on them.)"
    "(The descent continued, and the city loomed larger, an ancient presence rising from the dark, its secrets waiting to be uncovered—at a cost no one yet understood.)"
    "???" "At last, we're almost done... Wait for me, just a little more. Please..."
    pause 3.0
    "(The submarine jolted again, this time harder, and the lights flickered wildly. The crew exchanged anxious glances, their tension rising as the hull groaned.)"
    menu:
        "Something’s wrong.":
            jump C1S2B1
        "We need to stay calm.":
            jump C1S2B2
    return

label C1S2B1:
    scene bg_submarine
    show Aoi
    window show
    aoi "This is not just a pressure issue. Something’s wrong. Takiyo, check the communications. Now."
    show Takiyo at right
    takiyo "(frantically typing)"
    takiyo "(frantically typing) I... I can’t get a stable link. We’re almost cut off completely."
    pause 3.0
    show Daichi at left
    daichi "We’re fine. Don’t panic. This is all part of the descent."
    window hide
    hide Takiyo
    hide Daichi
    pause 3.0
    window show
    aoi "We're in uncharted territory now. This city, whatever it is, has to be the source of these disturbances."
    hide Aoi
    show Kawa
    pause 0.5
    "(Kawa started typing furiously, muttering to himself.)"
    kawa "If we lose comms completely, we're in deep trouble. We’re already too far down. If something happens to the sub, we’re on our own."
    hide Kawa
    jump C1S3A
    return
label C1S2B2:
    scene bg_submarine
    show Aoi at left
    aoi "We need to stay calm. We’re trained for this."
    pause 3.0
    "(Satoshi slammed a fist on his console, visibly frustrated.)"
    show Satoshi at right
    satoshi "Calm?"
    satoshi "Calm? Are you kidding? We’re at the mercy of this sub’s integrity! We don’t know what we’re dealing with down here."
    show Daichi
    daichi "Stop panicking. We came here for a reason. We’ll face whatever’s down there together. No turning back."
    window hide
    hide Aoi
    hide Satoshi
    hide Daichi
    pause 3.0
    window show
    "(The sub groaned again, this time with a metallic screech that sent shivers down everyone’s spine.)"
    aoi "This is no longer a simple expedition. This is a fight for survival."
    jump C1S3A
    return
label C1S3A:  
    scene bg_submarine
    pause 2.0
    "(The lights dimmed as they passed beneath an overhang in the city, casting a foreboding shadow over the crew. The city's outline was now clearer, revealing eerie structures that seemed both ancient and unnaturally preserved.)"
    "(Aoi couldn’t shake the feeling that they weren’t just exploring. They were intruding on something. The air was thick, heavy with an unspoken presence.)"
    window hide
    pause 1.5
    show Kawa at left
    window show
    kawa "The pressure here is off the charts. We’re close to the bottom. I’m not sure how much longer we can stay this deep."
    show Takiyo
    takiyo "We don’t have much choice. We need to gather whatever data we can before we’re forced to turn back."
    show Aoi
    aoi "Keep the systems running. Satoshi, check for any signs of damage."
    window hide
    pause 1.5
    window show
    kawa "Everything seems stable, for now. But I’m not liking this. It’s too quiet... too unnatural."
    window hide
    scene black
    with fade
    pause 3.0
    "(As they continued to descend further into the abyss, Aoi’s grip tightened on the armrests. Every instinct in him screamed that something was wrong.)"
    aoi "*whispers* Daichi... what if we should turn back? What if we're making a mistake?"
    daichi "Aoi, we're not leaving now. Not after everything we’ve come this far for. There’s no turning back."
    "(Aoi’s heart raced as the darkness around them deepened. There was something ancient in the depths, something waiting.)"
    pause 3.0
    aoi "(What are we awakening down here?)"
    pause 5.0
    jumo C2S1A

    return
label C2S1A:
    
    return