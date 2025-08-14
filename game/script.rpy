# Main Character
default player_name = "Player"
default player_gender = "male"

define p = Character("[player_name]", color="#FFFFFF")
default ate_breakfast = False

# Relationship and story variables
default malvin_points = 0
default david_points = 0
default tito_points = 0
default athaa_points = 0
default chelsea_points = 0
default academic_points = 0
default social_points = 0
default confidence = 50

# Story flags
default joined_study_group = False
default helped_with_project = False
default attended_school_event = False
default made_best_friend = False

# Class Members and Characters
define mal = Character("Malvin", color="#F4A261")       # Soft orange
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
define ev = Character("Everyone", color="#FFB6")  # Everyone in class
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
    narrator "Let's go!"

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

    $ confidence += 10

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
        $ confidence -= 5

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

    if player_gender == "male":
        show boy at char_scaled_male
        with dissolve
    else:
        show girl at char_scaled_female
        with dissolve

    p "Finally, I found my classroom."
    p "I hope im not late."

    if player_gender == "male":
        hide boy
    else:
        hide girl

    narrator "You take a deep breath and open the classroom door, ready to meet your new classmates."

    jump classroom_day1

label classroom_day1:

    scene black with fade
    pause 1.0
    window hide

    show text "The teacher notices you and asks you to introduce yourself in front of the whole class." with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    t "Welcome to PPLG Class! Please introduce yourself to the class."
    t "Tell us your name and a little about yourself."

    if player_gender == "male":
        show boy at char_scaled_male
        with dissolve
    else:
        show girl at char_scaled_female
        with dissolve

    menu:
        "How do you want to introduce yourself?"

        "Be confident and enthusiastic":
            $ confidence += 15
            $ social_points += 10
            p "Hello everyone! My name is [player_name] and I'm super excited to be here!"
            p "I love programming and can't wait to learn with all of you!"

        "Be modest and polite":
            $ confidence += 5
            $ academic_points += 5
            p "Hello everyone, my name is [player_name]."
            p "I just transferred here and I hope we can all get along well."

        "Be nervous but honest":
            $ confidence -= 5
            p "Um... hi everyone. I'm [player_name]."
            p "I'm a bit nervous but I hope to make friends here."

    pause 1.0

    ev "Welcome, [player_name]!"
    ev "We hope you enjoy your time here."

    narrator "You feel a bit more relaxed as the class welcomes you warmly"

    if player_gender == "male":
        hide boy
    else:
        hide girl

    t "Thank you, [player_name]."
    t "Please take a seat wherever you like."

    narrator "You look around the classroom and see many friendly faces."
    narrator "You notice a few students smiling at you, making you feel welcome."

    menu:
        "Where do you want to sit?"

        "Next to the friendly-looking guy in the middle":
            jump sit_with_malvin

        "Near the group of students discussing code":
            jump sit_with_study_group

        "By the window, alone":
            jump sit_alone

label sit_with_malvin:
    p "(I'll sit next to that friendly guy, he seems approachable.)"

    narrator "You choose a seat next to a student who seems friendly and welcoming."

    p "Hi there!"

    mal "Hey! I'm Malvin, nice to meet you!"
    mal "You can call me Mal if you want."

    p "Nice to meet you, Malvin. I'm [player_name]."

    $ malvin_points += 10
    $ social_points += 5

    mal "So you're the transfer student! Welcome to our crazy class."
    mal "Don't worry, everyone here is pretty cool once you get to know them."

    p "Thanks, that's reassuring to hear."

    narrator "Malvin seems genuinely friendly and you feel more at ease."

    jump day1_break

label sit_with_study_group:
    p "(Those students seem serious about their studies. Maybe I can learn something.)"

    narrator "You sit near a group of students who are discussing programming concepts."

    d "Oh, hey there! You're the new student, right?"

    p "Yes, I'm [player_name]. Nice to meet you."

    d "I'm David, and this is Tito. We were just talking about our upcoming project."

    ti "Welcome to PPLG! Are you into programming?"

    menu:
        "How do you respond?"

        "Yes, I love coding!":
            $ academic_points += 15
            $ david_points += 10
            $ tito_points += 10
            p "Yes, I love coding! I've been learning for a while now."
            d "That's awesome! You'll fit right in here."

        "I'm still learning":
            $ academic_points += 5
            p "I'm still learning, but I'm really interested in it."
            ti "That's great! We can help each other out."

        "Not really, but I want to learn":
            $ confidence -= 5
            p "Not really, but I chose this major because I want to learn."
            d "No worries, we all started somewhere!"

    jump day1_break

label sit_alone:
    p "(Maybe I should sit by myself first, get a feel for the class.)"

    narrator "You choose a seat by the window, giving yourself space to observe."
    narrator "You watch your classmates interact, trying to understand the class dynamics."

    $ confidence -= 5

    narrator "A girl with a warm smile notices you sitting alone."

    a "Hey, you're the new student, right? I'm Athaa."

    p "Hi, I'm [player_name]. Nice to meet you."

    a "Why are you sitting all alone? Come join us!"

    menu:
        "How do you respond?"

        "I'd love to join you":
            $ athaa_points += 15
            $ social_points += 10
            $ confidence += 10
            p "I'd love to! I was just feeling a bit overwhelmed."
            a "No worries, we've all been there. Come on!"

        "I'm fine here, thanks":
            $ confidence -= 10
            p "I'm fine here, thanks. Just getting used to everything."
            a "Okay, but if you change your mind, we're right over there!"

        "Maybe later":
            $ athaa_points += 5
            p "Maybe later? I'm still adjusting."
            a "Of course! Take your time."

    jump day1_break

label day1_break:
    scene black with fade
    pause 1.0
    window hide

    show text "Class ends, and it's break time. Students start mingling and chatting." with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    narrator "During break, you have a chance to interact with more classmates."

    if malvin_points > 0:
        mal "Hey [player_name], want me to introduce you to everyone?"

        menu:
            "What do you say?"

            "Yes, that would be great!":
                $ social_points += 15
                $ malvin_points += 10
                jump meet_everyone

            "Maybe just a few people for now":
                $ social_points += 5
                jump meet_some_people

            "I'd rather explore on my own":
                $ confidence += 5
                jump explore_alone

    elif david_points > 0 or tito_points > 0:
        d "Want to see our current project? We're working on something cool."

        menu:
            "What do you say?"

            "I'd love to see it!":
                $ academic_points += 15
                $ joined_study_group = True
                jump see_project

            "Maybe later, I want to meet more people first":
                $ social_points += 10
                jump meet_everyone

    elif athaa_points > 0:
        a "Come on, let me introduce you to my friends!"

        menu:
            "What do you say?"

            "Okay, let's go!":
                $ athaa_points += 10
                $ social_points += 10
                jump meet_girls_group

            "I'm still a bit shy":
                $ confidence -= 5
                jump shy_interaction

    else:
        jump explore_alone

label meet_everyone:
    narrator "Malvin enthusiastically introduces you to the whole class."

    mal "Everyone, this is [player_name], our new classmate!"

    # Meet various classmates
    by "Hey there! I'm Bayu. Welcome to our chaotic but fun class!"
    rz "I'm Rizky. If you need help with anything, just ask!"
    tn "Tisna here. Hope you like it here!"

    if player_gender == "female":
        ch "Hi! I'm Chelsea. Finally, another girl in our class!"
        sh "I'm Shelin. We should hang out sometime!"
        $ chelsea_points += 10

    narrator "You feel welcomed by everyone's friendliness."
    $ social_points += 20
    $ confidence += 15

    jump day1_end

label meet_some_people:
    narrator "Malvin introduces you to a smaller group of his close friends."

    mal "These are my buddies - David, Tito, and Bayu."

    d "Nice to meet you properly! I think we sat near each other earlier."
    ti "Welcome to the group!"
    by "Hope you're ready for some fun times!"

    $ malvin_points += 5
    $ david_points += 5
    $ tito_points += 5
    $ social_points += 10

    jump day1_end

label see_project:
    narrator "David and Tito show you their current programming project."

    d "We're building a simple web application for our assignment."
    ti "It's a student management system. Want to help us with it?"

    menu:
        "What do you say?"

        "I'd love to help!":
            $ academic_points += 20
            $ helped_with_project = True
            $ david_points += 15
            $ tito_points += 15
            p "I'd love to help! This looks really interesting."
            d "Awesome! We could use fresh ideas."

        "I'm not sure I'm skilled enough yet":
            $ academic_points += 5
            p "I'm not sure I'm skilled enough to help yet."
            ti "Don't worry, we can teach you as we go!"

        "Maybe I can learn by watching":
            $ academic_points += 10
            p "Maybe I can learn by watching you work?"
            d "Of course! Observation is a great way to learn."

    jump day1_end

label meet_girls_group:
    narrator "Athaa introduces you to her group of friends."

    a "Girls, meet [player_name], our new classmate!"

    if player_gender == "female":
        ch "Finally! Another girl! I'm Chelsea."
        sh "I'm Shelin. We definitely need to stick together in this tech class!"
        ad "Adinda here. Welcome to the sisterhood!"
        $ chelsea_points += 15
    else:
        ch "Hi there! I'm Chelsea. Nice to have you in our class."
        sh "I'm Shelin. Hope you don't mind hanging with us girls sometimes!"
        ad "I'm Adinda. Welcome!"
        $ chelsea_points += 10

    $ athaa_points += 10
    $ social_points += 15

    jump day1_end

label shy_interaction:
    narrator "You feel a bit overwhelmed by all the new faces."

    p "I'm still feeling a bit shy. Maybe I need more time to adjust."

    a "That's totally understandable. New environments can be overwhelming."
    a "How about we just chat, just the two of us?"

    $ athaa_points += 15
    $ confidence += 5

    narrator "Athaa's understanding nature makes you feel more comfortable."

    jump day1_end

label explore_alone:
    narrator "You decide to explore and observe the class dynamics on your own."
    narrator "You notice different groups: the tech enthusiasts, the social butterflies, the quiet studious ones."

    p "(Everyone seems to have found their place already. I wonder where I'll fit in.)"

    narrator "As you observe, you overhear interesting conversations about projects, games, and school events."

    $ confidence += 10
    $ academic_points += 5

    jump day1_end

label day1_end:
    scene black with fade
    pause 1.0
    window hide

    show text "The first day comes to an end. You reflect on your experiences." with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    narrator "As you pack your things, you think about your first day."

    if social_points >= 15:
        p "(I think I made some good connections today. Everyone seems really friendly.)"
    elif academic_points >= 15:
        p "(I'm excited about the academic side of this class. There's so much to learn.)"
    else:
        p "(It was a bit overwhelming, but I think I'll adjust with time.)"

    narrator "Tomorrow is another day, and you're curious about what it will bring."

    jump day2

label day2:
    scene black
    window hide

    show text "Day 2 - Getting More Comfortable" with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    scene bedroom with fade

    narrator "You wake up feeling more confident about your second day."

    if player_gender == "male":
        show boy at char_scaled_male
        with fade
    else:
        show girl2 at char_scaled_female
        with fade

    if ate_breakfast:
        p "Yesterday went well. I should definitely eat breakfast again."
        $ ate_breakfast = True
        jump day2_school
    else:
        p "I was pretty hungry yesterday. Maybe I should eat breakfast today."

        menu:
            "What do you do?"

            "Eat breakfast this time":
                $ ate_breakfast = True
                $ confidence += 5
                jump day2_school

            "Skip breakfast again":
                $ ate_breakfast = False
                $ confidence -= 5
                jump day2_school

label day2_school:
    scene frontschool with fade

    narrator "You arrive at school feeling more familiar with the environment."

    if player_gender == "male":
        show boy at char_scaled_male
        with dissolve
    else:
        show girl3 at char_scaled_female
        with dissolve

    p "I wonder what today will bring."

    narrator "As you enter the classroom, you notice your classmates are already engaged in various activities."

    if malvin_points >= 10:
        mal "Hey [player_name]! Good morning!"
        p "Morning, Malvin!"
        $ malvin_points += 5

    if david_points >= 10:
        d "Morning! Ready for another day of coding?"
        p "Definitely!"
        $ david_points += 5

    if athaa_points >= 10:
        a "Good morning, [player_name]! How are you feeling today?"
        p "Much better, thanks for asking!"
        $ athaa_points += 5

    narrator "The teacher announces a special project that will determine much of your semester grade."

    t "Class, today I'm announcing our major semester project."
    t "You'll be working in groups of 3-4 to create a complete web application."
    t "Choose your groups wisely - this will be 40%% of your final grade."

    narrator "Students immediately start forming groups. This is a crucial decision."

    menu:
        "Which group do you want to join?"

        "Join Malvin's social group" if malvin_points >= 10:
            jump join_malvin_group

        "Join David and Tito's academic group" if david_points >= 10 or tito_points >= 10:
            jump join_study_group

        "Join Athaa's balanced group" if athaa_points >= 10:
            jump join_athaa_group

        "Try to form your own group":
            jump form_own_group

        "Wait and see who needs a member":
            jump wait_for_group

label join_malvin_group:
    narrator "You approach Malvin's group, which includes some of the most social students."

    mal "Hey [player_name]! Want to join our group?"
    by "Yeah, come join us! We're going to have fun with this project."
    rz "We might not be the most technical, but we'll figure it out together!"

    $ malvin_points += 20
    $ social_points += 15

    p "I'd love to join you guys!"

    narrator "Your group is formed: You, Malvin, Bayu, and Rizky."
    narrator "This group has great chemistry but might struggle with the technical aspects."

    jump project_planning

label join_study_group:
    narrator "You approach David and Tito's group, known for their academic excellence."

    d "Perfect timing, [player_name]! We were hoping you'd join us."
    ti "We could really use someone with fresh perspectives."

    if helped_with_project:
        d "Especially since you already helped us with our last project!"
        $ academic_points += 10

    $ david_points += 20
    $ tito_points += 20
    $ academic_points += 20

    p "I'm excited to work with you both!"

    narrator "Your group is formed: You, David, Tito, and one more member they recruit."
    narrator "This group has strong technical skills but might lack creativity."

    jump project_planning

label join_athaa_group:
    narrator "You approach Athaa's group, which seems to have a good balance of skills."

    a "I was hoping you'd join us! We have a great mix of people."

    if player_gender == "female":
        ch "Yes! Girl power in tech!"
        $ chelsea_points += 15
    else:
        ch "Great to have you with us!"
        $ chelsea_points += 10

    $ athaa_points += 20
    $ social_points += 10
    $ academic_points += 10

    p "This seems like a perfect fit!"

    narrator "Your group is formed: You, Athaa, Chelsea, and Shelin."
    narrator "This group has balanced skills and good communication."

    jump project_planning

label form_own_group:
    narrator "You decide to be proactive and form your own group."

    p "Hey everyone, I'm looking to form a group. Anyone interested?"

    $ confidence += 15

    if confidence >= 60:
        narrator "Your confidence attracts several interested classmates."

        ru "I'd like to join your group!"
        sd "Me too! You seem like a natural leader."
        ga "Count me in!"

        $ social_points += 20
        $ academic_points += 10

        narrator "Your group is formed with Rustam, Sudipa, and Gus Alit."
        narrator "This diverse group has potential but will need strong leadership."

    else:
        narrator "You struggle to attract members due to your low confidence."

        p "Um... anyone want to join my group?"

        narrator "After some awkward moments, a few classmates take pity on you."

        dd "I'll join you."
        va "Sure, why not."

        $ confidence -= 10

        narrator "Your group is formed, but the dynamic feels forced."

    jump project_planning

label wait_for_group:
    narrator "You decide to wait and see which group needs an extra member."

    $ confidence -= 5

    narrator "As groups form around you, you realize you might end up in a random group."

    t "Alright, let me assign the remaining students to groups that need members."

    narrator "You end up in a group with students you haven't interacted with much."

    hk "Guess we're teammates now. I'm Haikal."
    ml "Marlon here. Let's make the best of it."
    c "I'm Candra. Hope we can work well together."

    $ academic_points += 5

    narrator "This group is a wildcard - you'll need to work hard to build chemistry."

    jump project_planning

label project_planning:
    scene black with fade
    pause 1.0
    window hide

    show text "Your group starts planning the semester project." with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    narrator "Over the next few weeks, you work closely with your group members."
    narrator "Your relationships deepen, and you face various challenges together."

    # Different scenarios based on which group you joined
    if malvin_points >= 30:
        jump malvin_group_story
    elif david_points >= 30 or tito_points >= 30:
        jump study_group_story
    elif athaa_points >= 30:
        jump athaa_group_story
    else:
        jump random_group_story

label malvin_group_story:
    narrator "Working with Malvin's group turns out to be a rollercoaster of fun and challenges."

    mal "Okay team, let's build something awesome! How about a social media app?"
    by "Great idea! We can make it super user-friendly."
    rz "But... do any of us actually know how to build that?"

    p "We'll figure it out as we go!"

    narrator "Your group's enthusiasm is infectious, but technical challenges arise."

    menu:
        "How do you handle the technical difficulties?"

        "Take charge and learn the technical skills":
            $ academic_points += 25
            $ confidence += 20
            $ malvin_points += 15
            p "I'll take the lead on learning the technical stuff and teach you all."
            mal "That's amazing! You're a lifesaver."
            narrator "You spend extra hours learning and become the group's technical leader."

        "Suggest getting help from other groups":
            $ social_points += 15
            $ david_points += 10
            p "Maybe we can ask David's group for some technical advice?"
            mal "Good thinking! Collaboration over competition."
            narrator "Your diplomatic approach strengthens inter-group relationships."

        "Focus on the creative and design aspects":
            $ social_points += 20
            $ malvin_points += 10
            p "Let's focus on making our app's design and user experience amazing."
            by "Yes! We can make it the most beautiful app in class."
            narrator "Your group creates something visually stunning but technically simple."

    jump mid_semester

label study_group_story:
    narrator "Working with the academic group proves to be intellectually stimulating."

    d "Alright team, let's build a comprehensive learning management system."
    ti "We can implement advanced features like AI-powered recommendations."

    p "That sounds challenging but exciting!"

    narrator "Your group dives deep into complex programming concepts."

    menu:
        "How do you contribute to this high-achieving group?"

        "Match their technical intensity":
            $ academic_points += 30
            $ confidence += 15
            $ david_points += 20
            $ tito_points += 20
            p "I'll push myself to keep up with your level. Let's build something incredible."
            d "That's the spirit! Together we can create something professional-grade."
            narrator "You grow tremendously as a programmer, earning respect from your peers."

        "Focus on user experience and testing":
            $ academic_points += 20
            $ social_points += 10
            p "I'll focus on making sure our complex system is user-friendly."
            ti "That's actually crucial. Technical brilliance means nothing if users can't use it."
            narrator "You become the bridge between technical complexity and usability."

        "Handle project management and documentation":
            $ academic_points += 15
            $ social_points += 15
            $ confidence += 10
            p "I'll keep us organized and document everything properly."
            d "Perfect! We need someone to keep track of our progress."
            narrator "Your organizational skills become invaluable to the group's success."

    jump mid_semester

label athaa_group_story:
    narrator "Working with Athaa's balanced group creates a harmonious and productive environment."

    a "Let's build something that's both technically solid and socially meaningful."

    if player_gender == "female":
        ch "How about an app that helps women in tech connect and support each other?"
        $ chelsea_points += 15
    else:
        ch "How about an app that promotes diversity and inclusion in tech?"
        $ chelsea_points += 10

    sh "I love that idea! We can make a real difference."

    p "That's a fantastic concept. Let's do it!"

    $ athaa_points += 15
    $ social_points += 15
    $ academic_points += 15

    narrator "Your group works with passion and purpose, creating something meaningful."

    menu:
        "What's your main contribution to this project?"

        "Lead the technical development":
            $ academic_points += 25
            $ confidence += 20
            p "I'll handle the core programming and architecture."
            a "You're amazing! I knew you had great potential."
            narrator "You become the technical backbone of a socially conscious project."

        "Focus on user research and community building":
            $ social_points += 25
            $ athaa_points += 20
            p "I'll research our target users and build community engagement."
            ch "That's perfect! Understanding our users is crucial."
            narrator "You develop strong skills in user research and community management."

        "Coordinate between technical and social aspects":
            $ academic_points += 15
            $ social_points += 15
            $ confidence += 15
            p "I'll make sure our technical solution truly serves our social mission."
            sh "You're like the heart of our project!"
            narrator "You become skilled at balancing technical and social considerations."

    jump mid_semester

label random_group_story:
    narrator "Working with your randomly assigned group requires extra effort to build chemistry."

    hk "So... what should we build?"
    ml "I'm good with databases."
    c "I can handle frontend design."

    p "Let's figure out how to combine our different strengths."

    narrator "It takes time, but you gradually learn to work together effectively."

    menu:
        "How do you help your group gel together?"

        "Organize team-building activities":
            $ social_points += 20
            $ confidence += 15
            p "How about we hang out outside of class to get to know each other better?"
            hk "That's... actually a good idea."
            narrator "Your initiative helps transform strangers into friends."

        "Focus on clear communication and planning":
            $ academic_points += 15
            $ social_points += 10
            p "Let's establish clear roles and communication channels."
            ml "Finally, someone with organizational skills!"
            narrator "Your structured approach helps the group function smoothly."

        "Find common interests and goals":
            $ social_points += 15
            $ confidence += 10
            p "What do we all care about? Let's build something we're all passionate about."
            c "I never thought about it that way."
            narrator "You help the group discover shared values and motivation."

    jump mid_semester

label mid_semester:
    scene black with fade
    pause 1.0
    window hide

    show text "Mid-semester - Relationships Deepen" with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    narrator "As the semester progresses, your relationships with classmates continue to evolve."
    narrator "You face new challenges and opportunities that will shape your final outcomes."

    # School event announcement
    t "Class, there's a school tech festival coming up. Participation is optional but highly encouraged."
    t "It's a great opportunity to showcase your skills and network with industry professionals."

    menu:
        "Do you want to participate in the tech festival?"

        "Yes, definitely!":
            $ attended_school_event = True
            $ confidence += 20
            $ academic_points += 15
            $ social_points += 15
            jump tech_festival

        "Maybe, if my friends are going":
            jump check_friends_festival

        "No, I want to focus on my project":
            $ academic_points += 10
            jump focus_on_project

label tech_festival:
    narrator "You decide to participate in the tech festival, seeing it as a growth opportunity."

    p "I think this festival could be really valuable for all of us."

    # Different responses based on your main relationships
    if malvin_points >= 30:
        mal "If you're going, count me in! It'll be fun."
        $ malvin_points += 10

    if david_points >= 30:
        d "Excellent choice. This kind of exposure is crucial for our careers."
        $ david_points += 10

    if athaa_points >= 30:
        a "I'm so proud of you for taking this step!"
        $ athaa_points += 10

    narrator "At the festival, you meet industry professionals and other students from different schools."
    narrator "Your confidence grows as you present your work and network with others."

    $ confidence += 25
    $ academic_points += 20
    $ social_points += 20

    jump late_semester

label check_friends_festival:
    narrator "You decide to see what your friends are doing before making a decision."

    if malvin_points >= 20:
        mal "I'm thinking about it. Want to go together?"
        menu:
            "What do you say?"
            "Yes, let's go together!":
                $ attended_school_event = True
                $ malvin_points += 15
                jump tech_festival
            "Actually, let's skip it":
                $ malvin_points += 5
                jump focus_on_project

    elif david_points >= 20:
        d "I'm definitely going. You should come too - it's a great learning opportunity."
        menu:
            "What do you say?"
            "You convinced me!":
                $ attended_school_event = True
                $ david_points += 15
                jump tech_festival
            "I'll pass this time":
                $ david_points -= 5
                jump focus_on_project

    elif athaa_points >= 20:
        a "I'm going! It would be so much fun if you came too."
        menu:
            "What do you say?"
            "Okay, let's do it!":
                $ attended_school_event = True
                $ athaa_points += 15
                jump tech_festival
            "Maybe next time":
                $ athaa_points += 5
                jump focus_on_project
    else:
        narrator "None of your close friends seem particularly interested."
        jump focus_on_project

label focus_on_project:
    narrator "You decide to focus entirely on your semester project."

    p "I think I should put all my energy into making our project the best it can be."

    narrator "While others are at the festival, you spend extra time perfecting your group's work."
    narrator "Your dedication doesn't go unnoticed by your group members."

    $ academic_points += 25
    $ confidence += 10

    # Group members appreciate your dedication
    if malvin_points >= 20:
        mal "Thanks for putting in the extra work while we were having fun!"
        $ malvin_points += 10

    if david_points >= 20:
        d "Your dedication to excellence is admirable."
        $ david_points += 10

    if athaa_points >= 20:
        a "You're so committed! I really admire that about you."
        $ athaa_points += 10

    jump late_semester

label late_semester:
    scene black with fade
    pause 1.0
    window hide

    show text "Late Semester - Final Challenges" with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    narrator "As the semester nears its end, you face final challenges that will determine your outcomes."
    narrator "Your project is almost complete, and relationships have solidified."

    # A crisis occurs that tests your character
    narrator "Suddenly, a major problem arises with your group's project just days before the deadline."

    if malvin_points >= 30:
        mal "[player_name], our project has a major bug and I accidentally deleted some of our work!"
        mal "I'm so sorry! What do we do?"

    elif david_points >= 30:
        d "We have a critical system failure. Our database is corrupted."
        d "We need to decide: start over or try to salvage what we can."

    elif athaa_points >= 30:
        a "Our main feature isn't working properly, and we're running out of time."
        a "I'm really stressed about this. What should we do?"

    else:
        hk "Our project is falling apart. Nothing is working right."
        ml "Maybe we should just accept a lower grade."

    menu:
        "How do you handle this crisis?"

        "Take charge and work through the night to fix it":
            $ confidence += 30
            $ academic_points += 25
            jump crisis_leadership

        "Rally the team and divide the work":
            $ social_points += 25
            $ confidence += 20
            jump crisis_teamwork

        "Stay calm and find a creative solution":
            $ academic_points += 20
            $ confidence += 15
            jump crisis_creativity

        "Accept the situation and do your best":
            $ confidence += 10
            jump crisis_acceptance

label crisis_leadership:
    narrator "You step up as a leader in the crisis."

    p "Don't panic, everyone. I'll take charge and we'll fix this together."
    p "I'll work through the night if I have to. We're not giving up."

    narrator "You spend the entire night debugging, rewriting code, and recovering data."
    narrator "Your determination inspires your group members to push harder too."

    if malvin_points >= 30:
        mal "I can't believe you're doing all this for us. You're incredible!"
        $ malvin_points += 25
        $ made_best_friend = True

    elif david_points >= 30:
        d "Your leadership under pressure is remarkable. I have so much respect for you."
        $ david_points += 25
        $ made_best_friend = True

    elif athaa_points >= 30:
        a "You're amazing! I don't know what we would have done without you."
        $ athaa_points += 25
        $ made_best_friend = True

    narrator "Through your leadership, the project is saved and becomes even better than before."

    jump semester_end

label crisis_teamwork:
    narrator "You focus on bringing the team together to solve the problem collectively."

    p "We're all in this together. Let's divide the work and tackle this systematically."
    p "Everyone has strengths - let's use them all."

    narrator "You coordinate the team effort, ensuring everyone contributes their best skills."
    narrator "The collaborative approach not only saves the project but strengthens your bonds."

    $ social_points += 15

    if malvin_points >= 20:
        $ malvin_points += 20
    if david_points >= 20:
        $ david_points += 20
    if athaa_points >= 20:
        $ athaa_points += 20

    narrator "Your team emerges stronger and more united than ever."

    jump semester_end

label crisis_creativity:
    narrator "You approach the problem with creative thinking."

    p "Let's step back and think about this differently. Maybe there's a simpler solution."
    p "What if we pivot our approach entirely?"

    narrator "Your creative problem-solving leads to an innovative solution that's even better than the original plan."
    narrator "Your group's project becomes unique and impressive."

    $ academic_points += 15
    $ confidence += 10

    narrator "Teachers and classmates are impressed by your innovative approach."

    jump semester_end

label crisis_acceptance:
    narrator "You choose to accept the situation with grace."

    p "Sometimes things don't go as planned, and that's okay."
    p "Let's do our best with what we have and learn from this experience."

    narrator "Your mature attitude helps keep the group's morale up."
    narrator "While the project isn't perfect, your group learns valuable lessons about resilience."

    $ confidence += 5
    $ social_points += 10

    jump semester_end

label semester_end:
    scene black with fade
    pause 1.0
    window hide

    show text "End of Semester - Time for Reflection" with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    narrator "The semester has come to an end. It's time to see how your choices have shaped your experience."
    narrator "Your relationships, academic performance, and personal growth will determine your ending."

    # Calculate final outcomes based on points
    if academic_points >= 80 and social_points >= 60 and confidence >= 80:
        jump perfect_ending
    elif made_best_friend and academic_points >= 60:
        jump best_friend_ending
    elif academic_points >= 80:
        jump academic_success_ending
    elif social_points >= 80:
        jump social_butterfly_ending
    elif malvin_points >= 40:
        jump malvin_romance_ending
    elif athaa_points >= 40 and player_gender == "male":
        jump athaa_romance_ending
    elif chelsea_points >= 40 and player_gender == "female":
        jump chelsea_friendship_ending
    elif confidence >= 70:
        jump confident_leader_ending
    elif attended_school_event:
        jump networking_success_ending
    elif helped_with_project:
        jump helpful_friend_ending
    else:
        jump average_ending

# Multiple Endings

label perfect_ending:
    scene black with fade

    show text "Perfect Ending: The Complete Experience" with dissolve
    pause 3.0
    hide text with fade

    narrator "You've achieved something remarkable - excelling in every aspect of your school life."
    narrator "Your academic performance is outstanding, you've built strong friendships, and your confidence has soared."

    t "Congratulations, [player_name]. Your project was exceptional, and your leadership throughout the semester has been inspiring."

    if malvin_points >= 30:
        mal "You're not just my classmate, you're my best friend. Thanks for making this semester amazing!"

    if david_points >= 30:
        d "Working with you has made me a better programmer and person. Let's stay in touch!"

    if athaa_points >= 30:
        a "You've grown so much since that first day. I'm proud to call you my friend!"

    narrator "As you look back on your semester, you realize you've not only succeeded academically but also built lasting relationships and discovered your own potential."

    p "This semester has been incredible. I've learned so much about programming, about friendship, and about myself."
    p "I'm ready for whatever comes next!"

    narrator "You've achieved the perfect balance of academic success, social connections, and personal growth."
    narrator "Your future at SMK Triatma Jaya looks bright, and you're excited for the challenges ahead."

    jump final_reflection

label best_friend_ending:
    scene black with fade

    show text "Best Friend Ending: Unbreakable Bonds" with dissolve
    pause 3.0
    hide text with fade

    narrator "While your academic performance was solid, the real treasure of this semester was the deep friendship you formed."

    if malvin_points >= 40:
        mal "[player_name], you've become like a brother/sister to me. I can't imagine this class without you."
        mal "Whatever happens in the future, we'll always have each other's backs."

        p "Malvin, you made me feel welcome from day one. You're the best friend I could ask for."

        narrator "Your friendship with Malvin has become the foundation of your school experience."

    elif david_points >= 40:
        d "You know, [player_name], I thought this would just be about academics, but you've become my closest friend."
        d "Your dedication and character have inspired me to be better."

        p "David, working with you has pushed me to excel. I'm grateful for your friendship."

        narrator "Your bond with David has grown beyond just academic collaboration into true friendship."

    elif athaa_points >= 40:
        a "[player_name], you've been such an important part of my semester. You're like family to me now."
        a "I hope we stay close no matter where life takes us."

        p "Athaa, your kindness and support have meant everything to me."

        narrator "Your friendship with Athaa has been a source of strength and joy throughout the semester."

    narrator "Sometimes the most valuable thing you can gain from school isn't knowledge, but the people who become part of your life forever."

    jump final_reflection

label academic_success_ending:
    scene black with fade

    show text "Academic Excellence Ending: The Scholar's Path" with dissolve
    pause 3.0
    hide text with fade

    narrator "Your dedication to learning and academic excellence has paid off tremendously."

    t "[player_name], your project was among the best I've seen in years. Your technical skills and innovation are remarkable."
    t "I'm recommending you for advanced placement and special opportunities next semester."

    p "Thank you! All those late nights studying and coding were worth it."

    narrator "Your classmates look up to you as the academic leader of the class."

    d "You've set the bar really high for all of us. Your work ethic is inspiring."
    ti "Can you tutor me next semester? I want to reach your level."

    narrator "While you may not have formed as many close friendships, you've earned respect and admiration for your academic achievements."
    narrator "Your future in the tech industry looks incredibly promising."

    p "I've proven to myself that I can excel in this field. I'm excited to see how far I can go."

    jump final_reflection

label social_butterfly_ending:
    scene black with fade

    show text "Social Success Ending: The Heart of the Class" with dissolve
    pause 3.0
    hide text with fade

    narrator "You've become the social center of your class, beloved by everyone."

    mal "You know what, [player_name]? You're the reason our class feels like a family."
    by "Seriously, you bring everyone together. Class wouldn't be the same without you."

    if player_gender == "female":
        ch "You've been such a great friend to all of us girls. We need to stay in touch!"
        sh "Group chat forever!"

    narrator "Even students from other classes know who you are because of your friendly nature."

    p "I never expected to make so many friends. Everyone here is amazing."

    narrator "While your academic performance was decent, your real achievement was creating connections and bringing joy to others."
    narrator "You've learned that sometimes the most important skills are social ones."

    a "You have this amazing ability to make everyone feel included and valued. That's a rare gift."

    narrator "Your positive impact on the class culture will be remembered long after the semester ends."

    jump final_reflection

label malvin_romance_ending:
    scene black with fade

    show text "Romance Ending: Love in the Classroom" with dissolve
    pause 3.0
    hide text with fade

    narrator "Over the course of the semester, your friendship with Malvin has blossomed into something deeper."

    mal "[player_name], I need to tell you something. This semester has been amazing, not just because of school, but because of you."
    mal "I think... I think I'm falling for you."

    menu:
        "How do you respond?"

        "I feel the same way":
            p "Malvin, I've been feeling the same thing. You make every day brighter."

            mal "Really? I was so nervous to tell you!"

            narrator "You and Malvin decide to explore your romantic feelings while supporting each other academically."
            narrator "Your relationship becomes the talk of the class, but in a sweet, supportive way."

            by "You two are perfect together!"
            rz "Finally! We all saw this coming."

            p "I never expected to find love in programming class, but here we are."

            narrator "Your semester ends with not just academic growth, but the beginning of a beautiful relationship."

        "I value our friendship too much":
            p "Malvin, you mean so much to me, but I think we're better as friends."
            p "I don't want to risk losing what we have."

            mal "I understand. Your friendship is the most important thing to me too."

            narrator "You and Malvin remain close friends, with your bond even stronger after this honest conversation."
            narrator "Sometimes the best relationships are the ones that stay as friendships."

    jump final_reflection

label athaa_romance_ending:
    scene black with fade

    show text "Sweet Romance Ending: A Gentle Love Story" with dissolve
    pause 3.0
    hide text with fade

    narrator "Your connection with Athaa has grown into something beautiful and tender."

    a "[player_name], can we talk privately?"

    narrator "After class, Athaa approaches you with a shy smile."

    a "This semester has been so special, and it's mostly because of you."
    a "You've been so kind, so supportive... I think I've developed feelings for you."

    menu:
        "How do you respond?"

        "I've been hoping you'd say that":
            p "Athaa, I've been feeling the same way. You're incredible."

            a "Really? I was so worried about ruining our friendship!"

            narrator "You and Athaa begin a sweet, supportive relationship built on mutual respect and shared values."

            if chelsea_points >= 20:
                ch "I'm so happy for you both! You're perfect together."

            narrator "Your relationship becomes an inspiration to others in the class."

            p "I feel so lucky to have found someone who understands and supports me like you do."

            narrator "Your semester ends with the promise of a beautiful relationship ahead."

        "I care about you, but as a friend":
            p "Athaa, you're amazing, but I think we're better as friends."
            p "I really value what we have and don't want to complicate it."

            a "I understand. Thank you for being honest with me."

            narrator "Your friendship with Athaa remains strong, built on honesty and mutual respect."

    jump final_reflection

label chelsea_friendship_ending:
    scene black with fade

    show text "Sisterhood Ending: Bonds Beyond the Classroom" with dissolve
    pause 3.0
    hide text with fade

    narrator "Your friendship with Chelsea and the other girls has created a strong support network."

    ch "[player_name], having you in our class has been amazing. Finally, someone who gets it!"
    sh "We girls need to stick together in tech, and you've been the perfect addition to our group."

    if athaa_points >= 20:
        a "Our girl group is unstoppable now!"

    narrator "You've formed a tight-knit group of female friends who support each other in the male-dominated tech field."

    p "I never realized how important it would be to have other girls who understand the challenges we face."

    ch "We're going to change the tech industry, one line of code at a time!"

    narrator "Your friendship group becomes known throughout the school as supportive, smart, and successful."
    narrator "You've found your tribe and created lasting bonds that will support you throughout your career."

    jump final_reflection

label confident_leader_ending:
    scene black with fade

    show text "Leadership Ending: Born to Lead" with dissolve
    pause 3.0
    hide text with fade

    narrator "Your confidence and leadership abilities have made you a natural leader in the class."

    t "[player_name], I've watched you grow into a remarkable leader this semester."
    t "Would you be interested in being class representative next semester?"

    p "I'd be honored to represent our class!"

    narrator "Your classmates unanimously support your leadership."

    ev "You've always looked out for everyone and brought out the best in us!"

    if malvin_points >= 20:
        mal "You helped me become more confident too. You're a natural leader."

    if david_points >= 20:
        d "Your leadership style is collaborative and inspiring. I've learned a lot from you."

    narrator "You've discovered that your true strength lies in bringing out the best in others."

    p "I've learned that leadership isn't about being the smartest or most skilled. It's about helping others succeed."

    narrator "Your semester ends with the recognition that you have the potential to make a real difference in any field you choose."

    jump final_reflection

label networking_success_ending:
    scene black with fade

    show text "Networking Success Ending: Building Bridges" with dissolve
    pause 3.0
    hide text with fade

    narrator "Your participation in the tech festival has opened doors you never expected."

    narrator "A few days after the festival, you receive an unexpected message."

    u "Hello [player_name], I'm a recruiter from a major tech company. I was impressed by your presentation at the festival."
    u "Would you be interested in an internship opportunity?"

    p "I can't believe this! My decision to attend the festival is already paying off."

    narrator "Your classmates are amazed by your opportunity."

    if attended_school_event:
        if malvin_points >= 20:
            mal "That's incredible! I'm so proud of you for taking that risk."

        if david_points >= 20:
            d "Your networking skills are impressive. You've inspired me to put myself out there more."

    narrator "You realize that sometimes the biggest opportunities come from stepping outside your comfort zone."

    p "This semester taught me that taking calculated risks can lead to amazing opportunities."

    narrator "Your future looks bright with new connections and possibilities opening up."

    jump final_reflection

label helpful_friend_ending:
    scene black with fade

    show text "Helpful Friend Ending: The Power of Kindness" with dissolve
    pause 3.0
    hide text with fade

    narrator "Your willingness to help others throughout the semester has created a ripple effect of kindness."

    narrator "As the semester ends, you realize how many people you've helped along the way."

    if helped_with_project:
        d "You know, [player_name], your help early in the semester made all the difference for our group."
        ti "You didn't have to help us, but you did. That says everything about your character."

    narrator "Other classmates approach you with gratitude."

    by "Remember when you helped me understand that difficult concept? I passed because of you."
    rz "You always made time to help, even when you were busy with your own work."

    narrator "Your teacher notices your impact on the class."

    t "Your willingness to help your classmates has created a more collaborative and supportive learning environment."

    p "I've learned that helping others doesn't take away from my own success - it enhances it."

    narrator "You've discovered that kindness and generosity are their own rewards."
    narrator "Your reputation as someone who can be counted on will serve you well in the future."

    jump final_reflection

label average_ending:
    scene black with fade

    show text "Steady Progress Ending: A Solid Foundation" with dissolve
    pause 3.0
    hide text with fade

    narrator "While your semester wasn't filled with dramatic highs or lows, you've built a solid foundation for your future."

    p "I may not have been the top student or the most popular, but I've learned a lot and made some good friends."

    narrator "Your steady, consistent approach has earned you respect from your classmates."

    mal "You're reliable, [player_name]. That's a valuable quality."

    if david_points >= 10:
        d "Your work ethic is solid. You'll do well in this field."

    if athaa_points >= 10:
        a "You're a good friend and a good person. That matters more than grades."

    narrator "Sometimes the most important growth happens quietly, without fanfare."

    t "You've shown consistent improvement throughout the semester. Keep up the good work."

    p "I'm proud of how far I've come. This is just the beginning."

    narrator "Your semester ends with the satisfaction of steady progress and the promise of continued growth."

    jump final_reflection

label final_reflection:
    scene black with fade
    pause 1.0
    window hide

    show text "Final Reflection" with dissolve
    pause 2.5

    hide text with fade
    pause 1.0

    narrator "As you pack up your things on the last day of the semester, you reflect on your journey."

    if player_gender == "male":
        show boy at char_scaled_male
        with dissolve
    else:
        show girl27 at char_scaled_female
        with dissolve

    p "When I first walked into this classroom, I was just a nervous transfer student."
    p "Now I feel like I truly belong here."

    narrator "You think about all the choices you made and how they shaped your experience."

    if ate_breakfast:
        p "Even small choices, like eating breakfast, made a difference in my confidence."

    if joined_study_group:
        p "Joining the study group taught me the value of academic collaboration."

    if attended_school_event:
        p "Participating in the tech festival showed me the importance of taking risks."

    if made_best_friend:
        p "But most importantly, I found a true friend who will be part of my life forever."

    narrator "Your classmates gather around for final goodbyes."

    ev "See you next semester, [player_name]!"
    ev "Don't be a stranger during the break!"

    p "I won't forget any of you. This semester has changed my life."

    narrator "As you walk out of SMK Triatma Jaya for the last time this semester, you feel grateful for the journey."
    narrator "You've grown not just as a student, but as a person."
    narrator "The future is full of possibilities, and you're ready to embrace them all."

    scene black with fade
    pause 2.0

    show text "Thank you for playing!\n\nYour choices shaped [player_name]'s unique story.\n\nTry playing again to discover different paths and endings!" with dissolve
    pause 4.0

    hide text with fade

    return

label end:
    scene black with fade
    narrator "Alright, maybe next time."
    return
