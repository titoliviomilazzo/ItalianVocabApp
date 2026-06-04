from enrich_util import update_vocab

batch1_data_p3 = {
    51: {
        "meaning": "눈멀게 하다, 눈부시게 하다",
        "story": "1. Walking into a dark cave. 2. Someone suddenly shines a bright flashlight in the face. 3. Character covering their eyes in pain. 4. Seeing only white spots for a few seconds."
    },
    52: {
        "meaning": "접속하다, 출입하다",
        "story": "1. Standing in front of a locked digital door. 2. Typing a secret password on the keypad. 3. A green light flashes 'Access Granted'. 4. The door sliding open to allow entry."
    },
    53: {
        "meaning": "가속하다, 속도를 높이다",
        "story": "1. A car driving slowly on a highway. 2. Stepping hard on the gas pedal. 3. The needle on the speedometer jumping forward. 4. The scenery blurring as the car zooms away."
    },
    54: {
        "meaning": "가속기, 엑셀러레이터",
        "story": "1. A foot wearing a shoe hovering over pedals. 2. Pushing the right pedal down firmly. 3. The engine roaring with power. 4. The car launching forward from the starting line."
    },
    55: {
        "meaning": "가속, 가속도",
        "story": "1. A rocket sitting on a launchpad. 2. Fire blasting from the bottom. 3. The rocket lifting off slowly at first. 4. Breaking the sound barrier with incredible speed."
    },
    56: {
        "meaning": "켜다, 불을 붙이다",
        "story": "1. Sitting in a dark room at night. 2. Finding a candle on the table. 3. Striking a match and touching the wick. 4. The room filling with warm, flickering light."
    },
    57: {
        "meaning": "라이터",
        "story": "1. Holding a small plastic object. 2. Flicking the thumb over the wheel. 3. A small blue flame appearing. 4. Using the flame to light a birthday candle."
    },
    58: {
        "meaning": "암시하다, 넌지시 비추다",
        "story": "1. Two friends talking secretly. 2. One person winking and pointing at a box. 3. The other person looking curious. 4. Character whispering a clue about the surprise inside."
    },
    59: {
        "meaning": "암시, 기미, 흔적",
        "story": "1. A clear blue sky. 2. A single small gray cloud appears. 3. The air getting slightly cooler. 4. The first hint of a storm coming later."
    },
    60: {
        "meaning": "악센트를 주다, 강조하다",
        "story": "1. Reading a list of plain words. 2. Seeing a word with a bold red mark on top. 3. Saying the word louder than the others. 4. Everyone noticing the important word now."
    },
    61: {
        "meaning": "악센트, 강세, 말투",
        "story": "1. A traveler speaking in a foreign land. 2. People looking puzzled by the sound. 3. Character pointing to their mouth and smiling. 4. Realizing they have a charming regional accent."
    },
    62: {
        "meaning": "확인, 검진, 조사",
        "story": "1. A doctor wearing a white coat and glasses. 2. Checking a patient's heartbeat with a stethoscope. 3. Looking at an X-ray result on the screen. 4. Writing a report that everything is healthy."
    },
    63: {
        "meaning": "확인하다, 조사하다",
        "story": "1. Finding a mysterious envelope in the mail. 2. Opening it carefully with a letter opener. 3. Reading the name and address inside. 4. Confirming it belongs to the neighbor."
    },
    64: {
        "meaning": "열렬한, (불이) 켜진",
        "story": "1. A giant bonfire burning in the night. 2. People dancing around the bright flames. 3. Character's eyes reflecting the light. 4. Feeling the intense heat and energy."
    },
    65: {
        "meaning": "접속, 출입, 통로",
        "story": "1. A computer screen asking for a login. 2. Entering the correct username and ID. 3. An icon changing from a lock to a key. 4. Accessing the private files on the desktop."
    },
    66: {
        "meaning": "장신구, 액세서리, 부속물",
        "story": "1. Wearing a plain black dress. 2. Adding a sparkling necklace and a belt. 3. Putting on a matching hat and gloves. 4. Looking complete and stylish in the mirror."
    },
    67: {
        "meaning": "도끼",
        "story": "1. Looking at a fallen log in the yard. 2. Picking up a sharp tool with a wooden handle. 3. Swinging it down with all strength. 4. The log splitting neatly into two pieces."
    },
    68: {
        "meaning": "허용할 만한, 받아들일 수 있는",
        "story": "1. A student handing in a messy paper. 2. The teacher looks at it with a neutral face. 3. Drawing a small green checkmark at the corner. 4. The student sighing with relief that it's okay."
    },
    69: {
        "meaning": "수락하다, 받아들이다",
        "story": "1. Receiving a beautiful gift box. 2. Smiling and saying 'Grazie!'. 3. Opening the lid to see a scarf. 4. Putting the scarf on and accepting the kind gesture."
    },
    70: {
        "meaning": "잡다, 붙들다",
        "story": "1. A fast butterfly flying in the garden. 2. A child running after it with a net. 3. Swishing the net through the air quickly. 4. The butterfly safely caught inside the mesh."
    },
    71: {
        "meaning": "가벼운 병, 병치레",
        "story": "1. A person sneezing 'Etciù!'. 2. Having a slightly red nose. 3. Resting in bed with a bowl of soup. 4. Feeling a bit weak but recovering quickly."
    },
    72: {
        "meaning": "강철",
        "story": "1. Fire glowing in a blacksmith's forge. 2. Hammering a red-hot metal bar. 3. Cooling it in a bucket of water. 4. A strong, unbreakable sword made of shiny steel."
    },
    73: {
        "meaning": "우연한 사고, 뜻밖의 일",
        "story": "1. Walking down a normal sidewalk. 2. A flower pot falls from a balcony nearby. 3. Barely avoiding the falling object. 4. Heart beating fast after the sudden dangerous event."
    },
    74: {
        "meaning": "멸치, 앤초비",
        "story": "1. A small silver fish swimming in a school. 2. Caught in a fisherman's net at sea. 3. Preserved in a jar of salty oil. 4. Placing them on top of a delicious pizza."
    },
    75: {
        "meaning": "아늑한, 친절한, 낙천적인",
        "story": "1. Entering a warm cafe during a blizzard. 2. Finding a soft velvet armchair by the fireplace. 3. The owner serving a hot cocoa with a smile. 4. Feeling perfectly comfortable and safe."
    },
    76: {
        "meaning": "환대, 리셉션",
        "story": "1. Arriving at a grand hotel lobby. 2. A person at the desk welcoming the guest. 3. Handing over a room key on a tassel. 4. Being led to a beautiful suite with a view."
    },
    77: {
        "meaning": "환영하다, 받아들이다",
        "story": "1. Stepping off a plane in a new country. 2. Seeing friends holding a 'Benvenuto' sign. 3. Being greeted with flowers and smiles. 4. Feeling happy and included immediately."
    },
    78: {
        "meaning": "칼로 찌르다",
        "story": "1. A shady character holding a sharp kitchen knife. 2. Sneaking up behind a target in the dark. 3. A sudden lunging motion with the blade. 4. An action scene from a tense detective novel."
    },
    79: {
        "meaning": "수리하다, 정돈하다, 앉히다",
        "story": "1. A wobbly chair with a loose leg. 2. Tightening the screws with a screwdriver. 3. Testing the chair by sitting down carefully. 4. The chair is now stable and perfect to use."
    },
    80: {
        "meaning": "동행하다, 안내하다",
        "story": "1. A small child lost in a large park. 2. A friendly park ranger finds them. 3. Walking hand-in-hand together. 4. Leading the child back to their worried parents."
    },
    81: {
        "meaning": "동의하다, 허락하다",
        "story": "1. Asking a question with a hopeful look. 2. The other person listening and nodding. 3. Signing a document to finalize the deal. 4. Shaking hands to show mutual agreement."
    },
    82: {
        "meaning": "만족시키다, 달래다",
        "story": "1. A child crying for a big teddy bear. 2. A parent buying the bear for the child. 3. The child instantly stopping the tears and hugging the toy. 4. Everyone is happy and peaceful now."
    },
    83: {
        "meaning": "줄이다, 짧게 하다",
        "story": "1. Wearing pants that are much too long. 2. Marking the bottom with a white chalk. 3. Folding and sewing the fabric up. 4. The pants now fit perfectly at the ankles."
    },
    84: {
        "meaning": "일치시키다, (악기를) 조율하다",
        "story": "1. A guitar sounding very out of tune. 2. Turning the tuning pegs slowly. 3. Plucking the strings and checking the sound. 4. Playing a beautiful, perfect chord."
    },
    85: {
        "meaning": "협정, 합의, 조화",
        "story": "1. Two people arguing over a price. 2. Finding a middle ground together. 3. Writing down the final number on a paper. 4. Shaking hands on the successful agreement."
    },
    86: {
        "meaning": "깨닫다, 알아차리다",
        "story": "1. Walking out and realizing the keys are missing. 2. Thinking hard and tapping the chin. 3. Remembering they were left on the fridge. 4. A lightbulb appearing over the head in realization."
    },
    87: {
        "meaning": "달려오다, 모여들다",
        "story": "1. A ice cream truck bell ringing in the street. 2. Children hearing the sound from garages. 3. Everyone running towards the truck at once. 4. A crowd forming to get a cold treat."
    },
    88: {
        "meaning": "옆에 대다, 다가가다, (차를) 세우다",
        "story": "1. Driving a car and seeing a parking spot. 2. Turning the steering wheel gently. 3. Moving the car slowly toward the curb. 4. Stopping the car perfectly inside the lines."
    },
    89: {
        "meaning": "돌보다, 보살피다",
        "story": "1. An old man sitting in a garden chair. 2. A younger person bringing a blanket and tea. 3. Helping the man stand up and walk. 4. Providing kind support and company."
    },
    90: {
        "meaning": "축적하다, 모으다",
        "story": "1. Finding one old coin in the attic. 2. Adding it to a growing stack in a jar. 3. Collecting more over many years. 4. The jar is now overflowing with shiny treasure."
    },
    91: {
        "meaning": "축전지, 배터리",
        "story": "1. A flashlight that won't turn on. 2. Opening the lid to see old batteries. 3. Inserting fresh, powerful energy cells. 4. The light shines incredibly bright again."
    },
    92: {
        "meaning": "정확한, 정밀한, 철저한",
        "story": "1. A watchmaker looking through a lens. 2. Placing tiny gears with a pair of tweezers. 3. Every single movement is perfect and measured. 4. The watch starts ticking with absolute precision."
    },
    93: {
        "meaning": "고발, 비난",
        "story": "1. Seeing a person taking something secretly. 2. Pointing a finger and shouting 'Ladro!'. 3. Calling the authorities on the phone. 4. Presenting the evidence in a courtroom."
    },
    94: {
        "meaning": "비난하다, 고소하다",
        "story": "1. Standing in a police station. 2. Pointing at a suspect behind the glass. 3. Explaining what the suspect did wrong. 4. The suspect looking nervous while being questioned."
    },
    95: {
        "meaning": "(열매가) 익지 않은, 떫은, 미숙한",
        "story": "1. Picking a green apple from a tree. 2. Taking a big bite and making a sour face. 3. The mouth feeling dry and puckered. 4. Realizing the fruit needs more time to ripen."
    },
    96: {
        "meaning": "식초",
        "story": "1. Holding a glass bottle with dark liquid. 2. Smelling the sharp, acidic scent. 3. Pouring a few drops onto a fresh salad. 4. The salad tastes tangy and delicious."
    },
    97: {
        "meaning": "산성의, 신맛이 나는",
        "story": "1. Biting into a fresh yellow lemon. 2. Eyes squeezing shut from the sourness. 3. Dropping a piece of lemon into water. 4. Watching a science experiment with pH paper turning red."
    },
    98: {
        "meaning": "물",
        "story": "1. A desert with hot sand and sun. 2. Finding a clear, cool mountain stream. 3. Cup the hands and drinking deeply. 4. Feeling refreshed and full of life."
    },
    99: {
        "meaning": "수채화",
        "story": "1. Dipping a brush into a jar of water. 2. Mixing blue paint on a white palette. 3. Spreading a light wash across the paper. 4. A beautiful, soft landscape appearing."
    },
    100: {
        "meaning": "수족관, 어항",
        "story": "1. A large glass tank filled with blue water. 2. Colorful tropical fish swimming through coral. 3. A small treasure chest at the bottom. 4. A child pressing their nose against the glass in awe."
    }
}

if __name__ == "__main__":
    update_vocab("assets/data/vocab.json", batch1_data_p3)
