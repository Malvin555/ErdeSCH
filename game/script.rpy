# Main Character
default player_name = "Player"
default player_gender = "male"

define p = Character("[player_name]", color="#FFFFFF")
default ate_breakfast = False


# Class Members and Characters
define l = Character("Lyni", color="#F4A261")       # Soft orange
define d = Character("David", color="#76C7F2")      # Sky blue
define ti = Character("Tito", color="#5DADE2")      # Blue
define by = Character("Bayu", color="#58D68D")      # Green
define rz = Character("Rizky", color="#48C9B0")     # Aqua
define tn = Character("Tisna", color="#F1948A")     # Light red
define ru = Character("Rustam", color="#AF7AC5")    # Violet
define sd = Character("Sudipa", color="#7DCEA0")    # Mint
define ga = Character("Gus Alit", color="#85C1E9")  # Soft blue
define sj = Character("Sujana", color="#F5B041")    # Amber
define al = Character("Adly", color="#82E0AA")      # Fresh green
define dd = Character("Dode", color="#F7DC6F")      # Yellow
define va = Character("Valliant", color="#F08080")  # Coral red
define hk = Character("Haikal", color="#45B39D")    # Dark aqua
define ml = Character("Marlon", color="#5B5EA6")    # Deep blue
define c = Character("Candra", color="#E59866")     # Earthy brown
define se = Character("Semadi", color="#48C9B0")    # Aqua green
define a = Character("Athaa", color="#F67280")      # Soft pink
define ar = Character("Artha", color="#A569BD")     # Purple
define g = Character("Gio", color="#F8C471")        # Warm yellow
define rl = Character("Rizkyla", color="#EC7063")   # Salmon red
define ch = Character("Chelsea", color="#BB8FCE")   # Lavender
define sh = Character("Shelin", color="#FAD7A0")    # Light peach
define ad = Character("Adinda", color="#F1948A")    # Soft coral
define nt = Character("Natasya", color="#A3E4D7")   # Teal mint
define vk = Character("Viska", color="#F9E79F")     # Cream yellow

# Other Characters
define u = Character("???", color="#ffcccc")
define t = Character("Teacher", color="#ffc8c8")  # Teacher character
define narrator = Character(None)  # For narration

# Images Characters
image boy = "images/main/boy/lyni-05.png"


image girl = "images/main/girl/clara-01.png"
image girl2 = "images/main/girl/clara-02.png"
image girl3 = "images/main/girl/clara-03.png"
image girl4 = "images/main/girl/clara-04.png"
image girl5 = "images/main/girl/clara-05.png"
image girl6 = "images/main/girl/clara-06.png"
image girl7 = "images/main/girl/clara-07.png"
image girl8 = "images/main/girl/clara-08.png"
image girl9 = "images/main/girl/clara-09.png"
image girl10 = "images/main/girl/clara-10.png"
image girl11 = "images/main/girl/clara-11.png"
image girl12 = "images/main/girl/clara-12.png"
image girl13 = "images/main/girl/clara-13.png"
image girl14 = "images/main/girl/clara-14.png"
image girl15 = "images/main/girl/clara-15.png"
image girl16 = "images/main/girl/clara-16.png"
image girl17 = "images/main/girl/clara-17.png"
image girl18 = "images/main/girl/clara-18.png"
image girl19 = "images/main/girl/clara-19.png"
image girl20 = "images/main/girl/clara-20.png"
image girl21 = "images/main/girl/clara-21.png"
image girl22 = "images/main/girl/clara-22.png"
image girl23 = "images/main/girl/clara-23.png"
image girl24 = "images/main/girl/clara-24.png"
image girl25 = "images/main/girl/clara-25.png"
image girl26 = "images/main/girl/clara-26.png"
image girl27 = "images/main/girl/clara-27.png"
image girl28 = "images/main/girl/clara-28.png"


image silhouetter = "images/silhouette/Silhouette-1.png"

# Home Backgrounds
image bedroom = "images/backgrounds/home/single bedroom.jpg"
image home = "images/backgrounds/home/entrance.jpg"
image kitchen = "images/backgrounds/home/dining_kitchen.jpg"
image outside = "images/backgrounds/home/outside1.jpg"

# School Backgrounds
image frontschool = "images/backgrounds/school/smp_front_day1.png"
image classroom_outside = "images/backgrounds/school/smp_classroom4_day2.png"

# Transforms
transform char_scaled:
    zoom 0.7
    center

transform char_scaled_male:
    zoom 0.25
    center

transform char_scaled_female:
    zoom 1.2
    xalign 0.5
    yalign 0.01


transform enter_left:
    zoom 0.7
    xalign -1.0
    yalign 1.0
    linear 0.8 xalign 0.5

transform left_pos:
    zoom 0.7
    xalign 0.25
    yalign 1.0

transform right_pos:
    zoom 0.7
    xalign 0.75
    yalign 1.0

# Label to collect player info
label setup_player:

    scene black with fade

    narrator "Welcome to the game!"

    narrator "Before we begin, tell me your name."

    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Player"

    narrator "Great, [player_name]! Now choose your gender."

    menu:
        "I'm a boy":
            $ player_gender = "male"
        "I'm a girl":
            $ player_gender = "female"

    narrator "All set, [player_name]! Let's get started."

    return

# Start of game
label start:

    call setup_player

    scene black with fade

    narrator "This game will tell you a real story about me and my class."
    narrator "Let’s go!"

    menu:
        "Continue the story":
            jump prologue

        "I don't want to hear your story":
            jump end

label prologue:

    scene black
    window hide

    show text "You are a transfer student enrolling at SMK Triatma Jaya,\njoining the PPLG major..." with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    show text "The story starts now..."  with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    window show
    jump day1

label day1:

    narrator "It's a bright morning in the city."
    narrator "You wake up in your cozy bedroom, ready to start a new day."

    scene bedroom with fade
    if player_gender == "male":
        show boy at char_scaled_male
        with fade
    else:
        show girl at char_scaled_female
        with fade

    narrator "You stretch and yawn, feeling the warmth of the sunlight streaming through your window."

    p "Ahhhh... what a nice sleep!"
    p "I feel refreshed and ready to take on the day."

    narrator "You stretch and get out of bed, feeling the excitement of your first day at school."
    p "I should get ready for school."

    narrator "You quickly get dressed and head downstairs for breakfast."

    if player_gender == "male":
        hide boy
    else:
        hide girl

    if player_gender == "male":
        show boy at char_scaled_male
        with vpunch
    else:
        show girl8 at char_scaled_female
        with vpunch

    p "Im hungry, I hope mom made something good for breakfast."

    pause 1.0

    menu:
        "What should I do?"

        "🍳 Go eat breakfast":
            $ ate_breakfast = True
            jump day1_kitchen

        "🏫 Just go to school":
            $ ate_breakfast = False
            jump day1_go_to_school
        
label day1_kitchen:
    scene kitchen with fade

    narrator "The aroma of breakfast fills the air as you enter the kitchen."

    if player_gender == "male":
        show boy at char_scaled_male
        with dissolve
    else:
        show girl10 at char_scaled_female
        with dissolve

    p "Breakfast smells delicious today!"

    if player_gender == "male":
        show boy at char_scaled_male
        with dissolve
    else:
        show girl3 at char_scaled_female
        with dissolve
    p "I can't wait to meet my new classmates."
    
    jump day1_go_to_school

label day1_go_to_school:
    scene home with fade
    pause 1.0

    if ate_breakfast:
        scene home with fade
        narrator "After a hearty breakfast, you grab your bag and head out the door feeling energized."

        if player_gender == "male":
            show boy at char_scaled_male
            with vpunch
        else:
            show girl15 at char_scaled_female
            with vpunch

        p "Time to go to school!"

    else:
        scene outside with fade
        narrator "You head out on an empty stomach, hoping you'll survive until lunch."

        if player_gender == "male":
            show boy at char_scaled_male
            with vpunch
        else:
            show girl5 at char_scaled_female
            with vpunch

        p "I hope I can find something to eat at school."

    jump day1_school

label day1_school:
    scene black
    window hide

    show text "You arrive at SMK Triatma Jaya, feeling a mix of excitement and nervousness." with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    show text "You see many students chatting and laughing, making new friends." with dissolve

    scene frontschool with fade

    narrator "You take a deep breath and step into the school grounds."

    if player_gender == "male":
        show boy at char_scaled_male
        with dissolve
    else:
        show girl at char_scaled_female
        with dissolve
    p "This is it, my new school!"

    scene black with fade
    pause 1.0
    window hide 

    show text "You look around, trying to find your classroom." with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    scene classroom_outside with fade

    narrator "You spot your classroom and walk towards it, feeling a bit anxious"


label end:

    scene black with fade

    narrator "Alright, maybe next time."

    return
