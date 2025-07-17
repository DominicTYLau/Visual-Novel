# The script of the game goes in this file.

define Rocky = Character("Rocky", color="#a86f3d")       
define Narrator = Character("Narrator", color="#eae6e4") 
define Squirrel = Character("Squirrel", color="#d6a75f") 
define Turtle = Character("Turtle", color="#7bb6a4")     
define Cat = Character("Cat", color="#c87b6f")           
define Remy = Character("Remy", color="#8c7fc4")         


image Rocky normal = "Rocky normal @2.png"
image Rocky confused = "Rocky confused @2.png"
image Rocky hungry = "Rocky hungry @2.png"
image Rocky sniffing = "Rocky sniffing @2.png"
image Rocky crash = "Rocky crash @1.jpg"

image Remy = "Remy @1.png"

image Squirrel = "Squirrel @1.5.png"
image Turtle = "Turtle @1.5.png"
image Cat = "Cat @1.png"

label start:

    play music "audio/nature-walk.mp3" volume 0.5 fadein 1.0 fadeout 1.0

    scene bg forest
    with fade

    show Rocky normal

    Narrator "The forest held its breath, broken only by the whisper of wind through the trees and the faint, persistent whine of distant mosquitoes."
    Narrator "Rocky the Raccoon blinked awake, rubbing the sleep from his eyes."
    Narrator "He’d been dreaming about marshmallows and leftover pizza crusts."

    play sound "audio/belly_growl.mp3" volume 2

    show Rocky hungry

    Rocky "Ugh… I’m starving"

    play sound "audio/yawn.mp3" volume 1

    show Rocky normal

    Narrator "He stretched, yawned, then peeked outside. But something felt… off."

    Rocky "Remy? … Remy??"

    show Rocky sniffing

    Narrator "He sniffed the air. Looked around. Nothing but trees and his own paw prints. The cozy spot beside him was now empty."
    Narrator "No response. His friend was gone."
    Narrator "And so was the bag of chips they’d stolen last night."
    Narrator "Crumbs led out of the log and vanished into the bush."

    Rocky "He wouldn’t leave without me. Not without sharing the last chip…"

    show Rocky normal

    Narrator "A gust of wind rattled the leaves. Rocky’s ears twitched. Something was out there."
    Narrator "Hungry. Alone. A little worried. Rocky did what any sensible raccoon would do: he set off into the woods to find food and to find his best friend"
    jump choice_one


label choice_one:

    Rocky "What should I do first?"

    menu:
        "Follow chip crumbs trail to the river":
            jump choices1_a
        "Check behind the campsite dumpster":
            jump choices1_b
        "Go sniffing near the old fox den":
            jump choices1_c


label choices1_a:
    scene bg riverforest
    with fade
    play music "audio/forest-river.mp3" volume 0.5 fadein 1.0 fadeout 1.0

    show Rocky confused

    Narrator "(river surrounded by forest)"
    Narrator "Rocky follows a trail of chip crumbs down a small hill, paws crunching softly against the forest floor. Twigs snap. The further he walks, the louder the rushing sound becomes. Maybe not danger, but something familiar. Comforting."
    Narrator "Soon, the thick canopy parts, revealing a gentle river winding through the trees like a silver ribbon. The water glimmers in the late-day sun, casting streaks of orange and gold across the ripples."
    Narrator "Dragonflies dance above the surface. A frog croaks once and plops into the shallows. Rocky stops at the edge, nose twitching."

    Rocky "This is where we always came to wash our paws after digging through garbage… and after marshmallow raids…"

    Narrator "He looks down at the wet paw prints on the rocks near the bank. Fresher than the chip crumbs."

    Rocky "You were definitely here Remy… but where’d you go?"

    play sound "audio/belly_growl.mp3" volume 0.7

    show Rocky hungry

    Narrator "His stomach growls again, more insistent now. He scans the area: the remains of an old picnic site to the left, a narrow log bridge crossing the river straight ahead, and a winding trail that follows the current downstream to the right."

    menu:
        "Cross the Wobbly Log Bridge":
            jump log_bridge
        "Follow a Fishy Smell Downstream":
            jump turtle_path


label log_bridge:
    scene bg logbridge
    with fade
    play music "river-with-faraway-bird-sounds-low-water-flowing.mp3" volume 0.3 fadein 1.0 fadeout 1.0

    show Rocky normal

    Narrator "Rocky steps onto the log, tail stiff with concentration."

    Rocky "Steady… steady… You’ve done this before. You got this…"

    Narrator "Halfway across, a squirrel appears on the opposite end."

    show Squirrel
    hide Rocky

    Squirrel "Bridge toll: One snack!"

    show Rocky confused
    hide Squirrel

    Rocky "I don’t even have snacks!"

    show Squirrel
    hide Rocky

    Squirrel "Then I guess you fall!"

    show Rocky normal
    hide Squirrel

    menu:
        "Balance carefully and attempt to cross anyway":
            $ result = renpy.random.choice(["success", "fail"])
            if result == "success":
                Narrator "Rocky breathes deep, focuses, and steps slowly. The squirrel moves aside with a pout."
                Narrator "He makes it across! Under a rock nearby, he finds a mostly-eaten granola bar."
                Rocky "Still good enough for a raccoon!"
            else:
                Narrator "Rocky wobbles, slips — SPLASH!"
                Narrator "He washes up further downstream, soggy but fine."
                Narrator "A bag of popcorn floats nearby. He grabs it and munches."
                Rocky "Soggy popcorn… Not the worst thing I’ve eaten."

        "Bribe the squirrel with something":
            Narrator "Rocky rummages through his fur and offers a shiny button."

            show Squirrel
            hide Rocky

            Squirrel "Hmm... rare, shiny... acceptable."
            Narrator "The squirrel lets him pass and tosses him a peanut as a bonus."
            Rocky "Thanks, weird toll creature."

    jump map_discovery_log


label turtle_path:
    scene bg riverbank
    with fade

    hide Rocky

    Narrator "Rocky tiptoes along the riverbank. A small turtle is flipped on its back, struggling in the mud."

    show Turtle

    Turtle "Help… legs… useless…"

    show Rocky normal
    hide Turtle

    Rocky "Hang on shell buddy!"

    hide Rocky

    Narrator "Rocky flips the turtle over."

    show Turtle

    Turtle "Thank you, noble raccoon. Take this… my lunch."

    hide Turtle

    Narrator "The turtle offers a freshly caught fish wrapped in a lily pad."

    show Rocky hungry

    Rocky "Yippeeee!"

    show Rocky normal
    menu:
        "Eat the fish immediately":
            play sound "audio/eat.mp3" volume 1
            Narrator "Rocky devours the fish in two bites. His energy returns."
            Rocky "Nothing beats fresh river sushi!"
        "Save it for Remy":
            Narrator "Rocky tucks the fish into his bag… somewhere… sort of."
            Narrator "His stomach growls louder, but he keeps walking."
            Rocky "He better appreciate this."

    jump map_discovery_turtle


label map_discovery_log:
    hide Rocky
    Narrator "Rocky stumbles upon a crumpled piece of paper caught under a stone."
    jump map_scene


label map_discovery_turtle:
    hide Rocky
    Narrator "Further along the riverbank, Rocky notices a crumpled paper snagged on a bush near a broken candy wrapper."
    jump map_scene


label map_scene:
    scene bg forest
    with dissolve

    Narrator "He unfurls the paper. It’s a crude, paw-drawn map."

    show Rocky confused

    Rocky "Wait a second… This is our map. The snack map!"

    hide Rocky

    scene bg treemap
    Narrator "A soda bottle drawn next to a tree, a triangle labeled 'SECRET,' and a giant star marked 'TREEHOUSE!!'"

    show Rocky normal
    Rocky "Remy must’ve dropped this… or maybe he left it for me."

    hide Rocky

    Narrator "He looks up. The river path continues, but now it veers uphill toward the woods into the direction of the old hideout."

    jump reunion_ending


label choices1_b:
    scene bg campground
    with fade

    hide Rocky    
    Narrator "Rocky creeps silently through thick bushes. The smell of old food and smoke drifts through the air. Ahead lies a quiet campground. Tents are zipped tight, and a faint glow from a dying campfire flickers."

    Narrator "Rocky spots a group of rival raccoons gathered around a rusty dumpster. They’re larger and look tough."

    show Rocky normal
    Rocky "Great… the gang. No way they’ll share snacks with me."

    Narrator "He spots a box of unused fireworks near the picnic tables."

    Rocky "Maybe I can… make a little noise."

    Narrator "He grabs a small firework and lights it with a matchstick he found earlier."

    play sound "audio/firework_boom.mp3"

    Narrator "BOOM! A loud pop and colorful sparks shoot up. The rival raccoons scatter in surprise, chittering and scrambling."

    Rocky "Perfect distraction!"

    hide Rocky
    Narrator "While the rivals are distracted, Rocky sneaks closer to a tent where two humans chat."

    "Human 1" "Did you hear? There’s a fat raccoon raiding the trash down by the campground."
    "Human 2" "Yeah, I saw him last night. Must’ve eaten a whole picnic basket."

    show Rocky normal

    Rocky "That sounds like Remy… He always loved to eat everything in his sight."

    Narrator "Rocky follows a trail past the tents and notices some dark fur snagged on a low branch."

    Rocky "Huh… that looks like Remy’s fur. He’s been here recently."

    Narrator "He pulls a few tufts carefully and stuffs them in his bag."

    Narrator "Near the dumpster, Rocky spots some treasure."

    Narrator "A half-eaten sandwich still wrapped in wax paper. A small bar of chocolate. A half corn dog, still warm from the campfire nearby."

    Rocky "Remy loved corndogs…"

    Narrator "He smiles, careful not to eat it all. He has to save some for his friend."

    hide Rocky
    scene bg campground
    with dissolve

    play music "audio/cricketsx27-campfire-ambient-soundscape.mp3" volume 0.5 fadein 1.0 fadeout 1.0

    Narrator "The last light of day fades, and the campground falls into a soft hush. Crickets begin their chorus. A gentle breeze rustles the tent flaps."

    Narrator "Rocky perches on a log behind the dumpster, inspecting his haul."

    show Rocky hungry

    Rocky "Half a sandwich, a corn dog, and… chocolate. Not bad."

    Narrator "He looks at the chocolate bar and squints at it suspiciously."

    menu:
        "Eat the chocolate":
            jump eat_chocolate
        "Save it for Remy":
            jump save_chocolate

    label eat_chocolate:

        play sound "audio/eat.mp3" volume 1

        Rocky "Eh, one bite won’t hurt."

        "He munches. Immediately, his pupils dilate."

        hide Rocky

        show Rocky normal:
            xoffset 0
            linear 1 xoffset 1800
            xoffset 1800
            linear 1 xoffset 0
            xoffset 0
            linear 1 xoffset 1800
            xoffset 1800
            linear 1 xoffset 600
        


        Rocky "Okay... definitely too much sugar. Too much sugar. Too much..."
 
        scene bg crash

        Rocky "Whoa… I feel like I just drank a whole river of soda."

        scene bg credits
        with dissolve

        centered ""

        return


    label save_chocolate:
        Rocky "He always had a sweet tooth. I’ll save this."

        "He tucks the bar into a leaf pouch tied around his waist."

        Rocky "He better appreciate this. I passed up chocolate for him."
        

        jump trail_beyond_fence


    label trail_beyond_fence:
        scene bg forest
        with fade
        play music "audio/river-with-faraway-bird-sounds-low-water-flowing.mp3" volume 0.5 fadein 1.0 fadeout 1.0

        Narrator "Rocky stands, brushing chip crumbs off his fur. He glances back at the trail of chaos he’s left: fireworks still smoking, raccoon rivals confused, a half-collapsed tent."

        Narrator "Suddenly, a breeze carries a familiar scent... something greasy and sweet."

        show Rocky normal
        Rocky "Is that… funnel cake?"

        Narrator "He turns toward the back edge of the campground and spots a hole in the chain-link fence. Right where a raccoon-sized creature definitely squeezed through."

        Rocky "Remy must’ve slipped out this way… probably waddled."

        Narrator "He squeezed through and followed a dirt path lit by the moon. Along the way, more signs appear: fresh pawprints, a sticky ketchup packet, and finally, an old wooden sign nailed to a tree."

        Narrator "\"TREEHOUSE TRAIL – PRIVATE\""

        Rocky "So he did go home."

        jump reunion_ending

label choices1_c:
    scene bg foxden
    with fade

    Narrator "Rocky follows the scent trail past the fox den which is now abandoned, just a mess of overturned dirt and a forgotten slipper. Tiny snack wrappers flutter along the wind, leading out of the forest and toward the glowing horizon."


    show Rocky normal
    Rocky "If Remy went this way, he must’ve been really hungry. The town is like… final boss territory."

    scene bg forest
    with dissolve

    Narrator "He slips through a broken fence and into a quiet suburban neighborhood, where porch lights flicker and the scent of grilled meat lingers in the air."

    scene bg forest
    with fade

    Narrator "Rocky tiptoes behind a house and spots a sleek black cat sunbathing under a garden lamp."
    
    show Cat
    hide Rocky

    Cat "You’re not from around here. Lost?"

    show Rocky normal
    hide Cat

    Rocky "Looking for my best friend. Short, striped, eats like a vacuum."

    show Cat
    hide Rocky

    Cat "Oh. The ball with legs. He passed through. Might know more…"

    Narrator "The cat glances toward a windowsill where a can of tuna sits just out of reach."

    Cat "That’s mine. Knock it down for me and I’ll talk."

    Narrator "Rocky nudges a broom leaning against the wall. It falls. The tuna clatters to the ground."

    Cat "Delightful. He waddled toward the alley. Said he was on a snack quest."

    scene bg forest
    with fade

    hide Cat

    Narrator "Rocky continues along a fence, then freezes as a small dog inside a house locks eyes with him."

    play sound "audio/bark.mp3"

    Narrator "BARK! BARK! BARK!"

    show Rocky confused

    Rocky "Why is it always the tiny ones…"

    Narrator "The sliding door opens. The dog sprints out."

    Narrator "Rocky sprints across the yard, dodges a sprinkler, leaps over a kiddie pool, and ducks into a recycling bin. The dog stands outside, yapping at the lid."

    show Rocky normal

    Rocky "Worst. Neighbourhood. Ever."

    scene bg forest
    with fade

    Narrator "Rocky makes it to a quiet alley behind the town bakery. A soft streetlamp buzzes overhead."

    Narrator "He sees something. A large raccoon hunched beside a tipped-over garbage bin, licking powdered sugar off his paws."

    show Rocky normal

    Rocky "Remy?"

    Narrator "Before he can call out, the raccoon jolts upright, grabs a churro, and waddles through a fence with a faded chalk drawing of a tree and a star."

    Rocky "That’s our mark! The treehouse!"

    scene bg forest
    with fade

    Narrator "Rocky pushes through the hole in the fence and emerges at the forest edge. The lights of the town fade behind him. Crickets chirp. Fireflies flicker."

    Narrator "In the distance, he sees the crooked silhouette of the treehouse they used to call home."

    show Rocky normal

    Rocky "I’m coming, buddy. And you better have saved at least one snack."

    jump reunion_ending
    

label reunion_ending:
    scene bg treehouse
    with fade

    Narrator "Rocky follows the familiar trail and climbs up the rickety ladder. Inside, he finds Remy on a pillow made of chip bags, belly round, churro dust in his fur, holding an empty corndog stick."

    show Rocky normal

    Rocky "Remy…"

    show Remy 
    hide Rocky

    Remy "Rocky?! You found me!"

    show Rocky normal
    hide Remy

    Rocky "You ate everything, didn’t you?"
    
    show Remy
    hide Rocky
    
    Remy "There was a lot of everything."

    Narrator "They laugh. Rocky pulls out a snack he found."

    show Rocky normal
    hide Remy

    Rocky "Well, I saved something for you, at least."

    Narrator "They sit together under the stars."

    scene bg credits
    with dissolve

    centered ""

    return