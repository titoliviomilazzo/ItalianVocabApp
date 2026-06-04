import sys
import os

# Add scripts directory to path to import enrich_util
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import enrich_util

updates = {
  101: {
    "meaning": "성수 (가톨릭)",
    "story": "1. Entering a church quietly. 2. Dipping fingers into a small marble basin. 3. Making the sign of the cross. 4. Feeling a sense of peace and reverence."
  },
  102: {
    "meaning": "취득하다, 획득하다",
    "story": "1. Studying hard for a certification exam. 2. Taking the final test with focus. 3. Receiving a certificate in the mail. 4. Hanging the new qualification on the wall."
  },
  103: {
    "meaning": "취득, 획득",
    "story": "1. A company looking at a smaller rival. 2. Shaking hands on a big deal. 3. Signs changing on the building front. 4. The company processing the new acquisition."
  },
  104: {
    "meaning": "구입하다, 사다",
    "story": "1. Seeing a nice shirt in a shop window. 2. Checking the price tag. 3. Paying with a credit card at the counter. 4. Walking out happily with a shopping bag."
  },
  105: {
    "meaning": "구입, 구매",
    "story": "1. Browsing online for a new laptop. 2. Clicking the 'Buy Now' button. 3. A package arriving at the doorstep. 4. Unboxing the new purchase excitedly."
  },
  106: {
    "meaning": "군침",
    "story": "1. Walking past a bakery smelling of fresh bread. 2. Seeing a delicious cake in the window. 3. Mouth starting to water uncontrollably. 4. Buying a slice to satisfy the craving."
  },
  107: {
    "meaning": "곡예사",
    "story": "1. A circus tent full of people. 2. A performer walking on a high wire. 3. Doing a somersault in mid-air. 4. Landing perfectly to applause."
  },
  108: {
    "meaning": "날카로운, 예리한",
    "story": "1. A detective looking at a clue. 2. Noticing a tiny detail everyone missed. 3. Connecting the dots with sharp intelligence. 4. Solving the mystery brilliantly."
  },
  109: {
    "meaning": "적응시키다, 개작하다",
    "story": "1. A book becoming very popular. 2. A director writing a script based on it. 3. Filming scenes for a movie. 4. The story adapted for the big screen."
  },
  110: {
    "meaning": "어댑터",
    "story": "1. Holding a plug that doesn't fit the socket. 2. Finding a travel adapter in the bag. 3. Plugging the device into the adapter. 4. The charging light turns on successfully."
  },
  111: {
    "meaning": "적합한, 알맞은",
    "story": "1. Looking for clothes for a hiking trip. 2. Trying on sturdy boots. 3. Checking if they are waterproof and comfortable. 4. Buying exactly the suitable gear."
  },
  112: {
    "meaning": "담당자, 직원",
    "story": "1. A machine breaks down in a factory. 2. Calling the maintenance staff. 3. The assigned employee arrives with tools. 4. Fixing the problem quickly."
  },
  113: {
    "meaning": "작별 (영원한)",
    "story": "1. A ship leaving the harbor. 2. Waving a handkerchief from the dock. 3. Tears in eyes as the ship disappears. 4. Saying a final goodbye to a loved one."
  },
  114: {
    "meaning": "심지어, 무려",
    "story": "1. Expecting a small gift. 2. Opening the box to find car keys. 3. Disbelief that it's such a huge present. 4. Being overwhelmed by the generosity."
  },
  115: {
    "meaning": "덧셈, 추가",
    "story": "1. Writing numbers on a blackboard. 2. Using a plus sign between them. 3. Counting on fingers to check. 4. Writing the correct sum at the bottom."
  },
  116: {
    "meaning": "장식하다",
    "story": "1. An empty Christmas tree in the room. 2. Hanging colorful balls and tinsel. 3. Placing a star on the very top. 4. Turning on the lights to see it sparkle."
  },
  117: {
    "meaning": "달게 하다, 부드럽게 하다",
    "story": "1. Drinking bitter black coffee. 2. Grimacing at the taste. 3. Adding a spoonful of sugar. 4. Enjoying the sweet and smooth drink."
  },
  118: {
    "meaning": "길들이다",
    "story": "1. A wild horse running within a fence. 2. A trainer approaching slowly with food. 3. The horse letting the trainer touch it. 4. Riding the tamed horse gently."
  },
  119: {
    "meaning": "잠들다",
    "story": "1. Reading a book in bed at night. 2. Eyelids getting heavy. 3. Detailed book dropping from hands. 4. Smiling peacefully in deep sleep."
  },
  120: {
    "meaning": "잠든",
    "story": "1. Looking at a baby in a crib. 2. The baby is perfectly still and quiet. 3. Tiptoeing out of the room. 4. Whispering 'He is asleep'."
  },
  121: {
    "meaning": "떠맡기다, 기대다",
    "story": "1. A heavy backpack on the floor. 2. Picking it up with a groan. 3. Shouldering the burden for a hike. 4. Walking up the mountain with the weight."
  },
  122: {
    "meaning": "몸에 지니고, ~위에",
    "story": "1. Searching pockets frantically. 2. Realizing the keys are not there. 3. Patting the jacket pocket. 4. Finding the keys right on oneself."
  },
  123: {
    "meaning": "똑바로 하다",
    "story": "1. A picture frame hanging crookedly. 2. Noticing it looks wrong. 3. Nudging it gently to the left. 4. Stepping back to see it perfectly straight."
  },
  124: {
    "meaning": "조정하다, 적응시키다",
    "story": "1. The salary is too low for the cost of living. 2. Asking the boss for a raise. 3. The boss agreeing to adjust the pay. 4. Seeing the new, fair amount on the check."
  },
  125: {
    "meaning": "적절한",
    "story": "1. Preparing for a formal dinner. 2. choosing a tie and jacket. 3. Checking the mirror. 4. Looking adequate for the occasion."
  },
  126: {
    "meaning": "딱 달라붙는",
    "story": "1. Buying a cycling outfit. 2. Putting on the spandex shirt. 3. It fits tight against the skin to reduce wind drag. 4. Riding fast with aerodynamic gear."
  },
  127: {
    "meaning": "달라붙다, 가입하다",
    "story": "1. A sticker not staying on the wall. 2. Applying strong glue to the back. 3. Pressing it firmly for a minute. 4. Now it adheres perfectly."
  },
  128: {
    "meaning": "가입, 동의",
    "story": "1. Reading a petition for a cause. 2. Signing a name on the list. 3. Showing support for the movement. 4. The group growing with new memberships."
  },
  129: {
    "meaning": "지금",
    "story": "1. A clock showing 12:00. 2. Stomach rumbling loudly. 3. Deciding to eat lunch immediately. 4. Eating a sandwich right now."
  },
  130: {
    "meaning": "청소년",
    "story": "1. A boy looking in the mirror. 2. Seeing acne and a changing face. 3. Listening to loud music in headphones. 4. Hanging out with friends at school."
  },
  131: {
    "meaning": "청소년기",
    "story": "1. Looking at old childhood photos. 2. Comparing with current teenage self. 3. Dealing with mood swings and growth. 4. A transformative time of life."
  },
  132: {
    "meaning": "사용하다",
    "story": "1. Holding a complex tool. 2. Reading the manual on how to use it. 3. Operating the machine carefully. 4. Successfully finishing the job."
  },
  133: {
    "meaning": "숭배하다, 매우 좋아하다",
    "story": "1. A fan seeing their idol on stage. 2. Screaming and waving hands. 3. Having posters all over the wall. 4. Absolutely adoring the singer."
  },
  134: {
    "meaning": "입양하다, 채택하다",
    "story": "1. Visiting an animal shelter. 2. Seeing a lonely puppy in a cage. 3. Signing papers to take it home. 4. The puppy playing happily in its new house."
  },
  135: {
    "meaning": "입양, 채택",
    "story": "1. A couple wanting a child. 2. Going through a long legal process. 3. Finally holding their new baby. 4. Celebrating the adoption with family."
  },
  136: {
    "meaning": "아드리아 해의",
    "story": "1. Looking at a map of Italy. 2. Pointing to the east coast. 3. Swimming in the blue sea near Venice. 4. Enjoying the Adriatic coast summer."
  },
  137: {
    "meaning": "성인, 어른",
    "story": "1. A child measuring height against a wall. 2. Years passing by quickly. 3. Start paying taxes and working. 4. Fully grown up as an adult."
  },
  138: {
    "meaning": "항공의, 공기의",
    "story": "1. Looking up at the sky. 2. Seeing a plane leave a white trail. 3. Watching an air show with stunts. 4. Admiring the aerial maneuvers."
  },
  139: {
    "meaning": "비행기",
    "story": "1. Waiting at the boarding gate. 2. Walking down the jet bridge. 3. Taking a seat near the window. 4. The plane taking off into clouds."
  },
  140: {
    "meaning": "비행기 (Aeroplano)",
    "story": "1. A child playing with a toy plane. 2. Making zooming noises. 3. Throwing a paper airplane. 4. Dreaming of being a pilot."
  },
  141: {
    "meaning": "공항",
    "story": "1. Dragging suitcases through sliding doors. 2. Checking the departure board. 3. Going through security check. 4. Buying duty-free items before flight."
  },
  142: {
    "meaning": "무더위",
    "story": "1. A hot summer day with no wind. 2. Character sweating profusely. 3. Trying to fan face with a paper. 4. The air feeling heavy and muggy."
  },
  143: {
    "meaning": "내밀다, (창밖을) 보다",
    "story": "1. Hearing a noise outside. 2. Opening the window shutters. 3. Leaning out to see the street. 4. Waving to a friend down below."
  },
  144: {
    "meaning": "굶주리게 하다",
    "story": "1. A cruel king taxing the village. 2. Farmers having no food left. 3. People looking very thin and weak. 4. The village suffering from starvation."
  },
  145: {
    "meaning": "배고픈",
    "story": "1. Stomach growling loudly like a beast. 2. Dreaming of a giant burger. 3. Running to the fridge. 4. Creating a massive sandwich to eat."
  },
  146: {
    "meaning": "애쓰다, 숨이 차다",
    "story": "1. Running late for a bus again. 2. Sprinting down the street. 3. Panting heavily to catch breath. 4. Barely making it onto the bus."
  },
  147: {
    "meaning": "숨이 찬, 괴로워하는",
    "story": "1. Finishing a marathon race. 2. Bending over with hands on knees. 3. Face red and sweaty. 4. Analyzing the breathless state."
  },
  148: {
    "meaning": "호흡 곤란, 고민",
    "story": "1. Stress piling up at work. 2. Feeling a tightness in the chest. 3. Taking deep breaths to calm down. 4. Trying to relieve the anxiety."
  },
  149: {
    "meaning": "일, 거래, 물건",
    "story": "1. Two businessmen talking in an office. 2. Negotiating terms of a contract. 3. Shaking hands on the deal. 4. Both looking satisfied with the business."
  },
  150: {
    "meaning": "매혹적인",
    "story": "1. Walking into a mysterious old library. 2. Seeing endless rows of ancient books. 3. Feeling the magic in the air. 4. Captivated by the fascinating atmosphere."
  },
  151: {
    "meaning": "매혹하다",
    "story": "1. A magician on stage. 2. Performing an impossible trick. 3. The audience watching with open mouths. 4. Totally fascinating the crowd."
  },
  152: {
    "meaning": "지치게 하다",
    "story": "1. Carrying heavy boxes up stairs. 2. Doing it for hours without break. 3. Legs starting to shake. 4. Collapsing on the sofa, exhausted."
  },
  153: {
    "meaning": "전혀, 조금도",
    "story": "1. Asking if someone is tired. 2. The person jumping with energy. 3. Shaking head vigorously 'No'. 4. Not tired at all."
  },
  154: {
    "meaning": "단언하다, 주장하다",
    "story": "1. A witness in a court room. 2. Raising a hand to swear truth. 3. Speaking clearly and firmly. 4. Turning a statement into a fact."
  },
  155: {
    "meaning": "단언, 확언",
    "story": "1. A debate between two people. 2. One makes a strong point. 3. Nodding head in agreement. 4. A positive affirmation of the truth."
  },
  156: {
    "meaning": "잡다, 이해하다",
    "story": "1. A ball flying through the air. 2. Reaching out a hand quickly. 3. Catching the ball firmly. 4. Understanding the concept perfectly."
  },
  157: {
    "meaning": "얇게 썰다",
    "story": "1. A loaf of fresh bread on a board. 2. Holding a serrated knife. 3. Cutting even, thin slices. 4. Serving the bread in a basket."
  },
  158: {
    "meaning": "얇게 썬 (햄 등)",
    "story": "1. Ordering prosciutto at the deli. 2. The machine slicing the meat thin. 3. Receiving a paper packet. 4. Making a sandwich with the cold cuts."
  },
  159: {
    "meaning": "애정",
    "story": "1. A mother looking at her child. 2. Smiling with warmth in her eyes. 3. Giving a gentle kiss on the forehead. 4. A moment of pure affection."
  },
  160: {
    "meaning": "걸린, 침범된",
    "story": "1. A doctor examining a patient. 2. Diagnosing a flu virus. 3. The patient looking weak in bed. 4. Suffering from the illness."
  },
  161: {
    "meaning": "다정한",
    "story": "1. A puppy jumping on its owner. 2. Licking the face happily. 3. Wagging tail furiously. 4. A very affectionate welcome."
  },
  162: {
    "meaning": "애착을 가진",
    "story": "1. Holding an old teddy bear. 2. Remembering childhood days. 3. Refusing to throw it away. 4. Deeply attached to the memory."
  },
  163: {
    "meaning": "나란히 놓다, 돕다",
    "story": "1. A new employee looking lost. 2. A senior mentor sits next to them. 3. Showing how to do the work side-by-side. 4. Working together as a team."
  },
  164: {
    "meaning": "신뢰, 위탁",
    "story": "1. Planning a rock climbing trip. 2. Checking the safety ropes. 3. Trusting the partner to hold the line. 4. Complete reliance on the equipment."
  },
  165: {
    "meaning": "맡기다, 위탁하다",
    "story": "1. Leaving for a vacation. 2. Giving house keys to a neighbor. 3. Asking them to water plants. 4. Entrusting the home to their care."
  },
  166: {
    "meaning": "날카로운",
    "story": "1. Testing a knife on a tomato. 2. It cuts effortlessly without squashing. 3. Looking at the gleaming edge. 4. A perfectly sharp blade."
  },
  167: {
    "meaning": "~하도록, ~하기 위해",
    "story": "1. Studying late into the night. 2. Drinking coffee to stay awake. 3. Doing all this so that... 4. Passing the exam with a high score."
  },
  168: {
    "meaning": "임대하다, 빌리다",
    "story": "1. Looking at vacation homes online. 2. Choosing a villa by the sea. 3. Identifying the rental price. 4. Booking the house for a week."
  },
  169: {
    "meaning": "임대료, 집세",
    "story": "1. Checking the calendar for the 1st of the month. 2. Writing a check for the landlord. 3. Delivering the envelope. 4. Paying the monthly rent."
  },
  170: {
    "meaning": "익사하다, 잠기다",
    "story": "1. Dropping a phone in a pool. 2. Watching it sink to the bottom. 3. It catches too much water. 4. The phone is ruined (drowned)."
  },
  171: {
    "meaning": "채우다, 쇄도하다",
    "story": "1. A store announcing a big sale. 2. Doors opening at 9 AM. 3. Hundreds of people rushing in. 4. The shop is instantly crowded."
  },
  172: {
    "meaning": "가라앉다",
    "story": "1. A toy boat in the bathtub. 2. A hole appears in the hull. 3. Taking on water rapidly. 4. Sinking to the bottom of the tub."
  },
  173: {
    "meaning": "프레스코화",
    "story": "1. Looking up at a church ceiling. 2. Seeing angels painted on wet plaster. 3. Admiring the vivid colors after centuries. 4. A masterpiece of art history."
  },
  174: {
    "meaning": "직면하다, 대처하다",
    "story": "1. A giant monster blocks the path. 2. The hero drawing a sword. 3. Not running away, but standing firm. 4. Facing the challenge bravely."
  },
  175: {
    "meaning": "훈제하다",
    "story": "1. Hanging fresh salmon in a shed. 2. Lighting a wood fire below. 3. Aromatic smoke filling the room. 4. The fish turning golden and delicious."
  },
  176: {
    "meaning": "아프리카의",
    "story": "1. A map of the African continent. 2. Pictures of savannahs and lions. 3. Traditional tribal masks. 4. Cultural symbols of Africa."
  },
  177: {
    "meaning": "수첩, 다이어리",
    "story": "1. Having too many appointments. 2. Opening a leather planner. 3. Writing down dates and times. 4. Organizing the schedule perfectly."
  },
  178: {
    "meaning": "요원, 대리인",
    "story": "1. A person in a black suit and sunglasses. 2. Talking into a wrist radio. 3. Moving stealthily through a crowd. 4. A secret agent on a mission."
  },
  179: {
    "meaning": "대리점, 여행사",
    "story": "1. Walking into a travel agency. 2. Seeing posters of tropical beaches. 3. Agent booking a flight ticket. 4. Planning the perfect holiday."
  },
  180: {
    "meaning": "걸다, 잠그다",
    "story": "1. Putting on a seatbelt in a car. 2. Pulling the strap across chest. 3. Hearing a 'click' sound. 4. Safely fastened for the ride."
  },
  181: {
    "meaning": "형용사",
    "story": "1. Writing the word 'Cat'. 2. Thinking it's too simple. 3. Adding 'Happy' and 'Fluffy' before it. 4. Now it's a 'Happy Fluffy Cat'."
  },
  182: {
    "meaning": "업데이트, 갱신",
    "story": "1. Computer screen showing a loading bar. 2. 'Installing updates 30%'. 3. Waiting patiently. 4. System restarting with new features."
  },
  183: {
    "meaning": "갱신하다",
    "story": "1. Looking at an old resume. 2. Adding the latest job experience. 3. Changing the formatting. 4. The CV is now up to date."
  },
  184: {
    "meaning": "우회하다, 속이다",
    "story": "1. A road blocked by construction. 2. Driver finding a side street. 3. Going around the obstacle. 4. Rejoining the main road later."
  },
  185: {
    "meaning": "추가하다, 더하다",
    "story": "1. Making a soup that tastes bland. 2. Sprinkling some salt and pepper. 3. Stirring the pot. 4. Now the flavor is enhanced."
  },
  186: {
    "meaning": "고치다, 수리하다",
    "story": "1. A bicycle with a flat tire. 2. Using a patch kit and pump. 3. Inflating the tire again. 4. The bike is ready to ride."
  },
  187: {
    "meaning": "필사적으로 잡다",
    "story": "1. Hanging from a cliff edge. 2. Fingers gripping the rock tightly. 3. Not looking down. 4. Clinging on for dear life."
  },
  188: {
    "meaning": "악화시키다",
    "story": "1. Having a small cough. 2. Walking out in the rain without a coat. 3. Coughing much louder now. 4. The cold has gotten worse."
  },
  189: {
    "meaning": "공격하다",
    "story": "1. A cat walking peacefully. 2. A dog running at it barking. 3. The cleaning hissing in defense. 4. An aggressive encounter."
  },
  190: {
    "meaning": "공격, 침략",
    "story": "1. Watching a nature documentary. 2. A lion stalking a zebra. 3. The sudden pounce. 4. The wild attack in action."
  },
  191: {
    "meaning": "공격적인",
    "story": "1. A driver honking loudly in traffic. 2. Shouting out the window. 3. Cutting off other cars. 4. Driving with aggressive behavior."
  },
  192: {
    "meaning": "유복한",
    "story": "1. Living in a large mansion. 2. Having servants and luxury cars. 3. Wearing expensive clothes. 4. Enjoying a wealthy lifestyle."
  },
  193: {
    "meaning": "민첩한",
    "story": "1. A ninja moving through shadows. 2. Jumping over a high wall. 3. Landing silently on feet. 4. Agile and quick movements."
  },
  194: {
    "meaning": "편안함, 여유",
    "story": "1. Sitting in a first-class seat. 2. Stretching legs fully. 3. Sipping champagne. 4. Traveling with great ease."
  },
  195: {
    "meaning": "행동하다",
    "story": "1. Seeing someone drop their wallet. 2. Not ignoring it. 3. Picking it up and running after them. 4. Acting quickly to return it."
  },
  196: {
    "meaning": "흔들다, 휘젓다",
    "story": "1. Holding a bottle of orange juice. 2. Seeing pulp at the bottom. 3. Shaking it vigorously. 4. Now it's mixed and ready to drink."
  },
  197: {
    "meaning": "흥분, 동요",
    "story": "1. A crowd waiting for a concert. 2. People shouting and pushing. 3. The anticipation building up. 4. A state of high agitation."
  },
  198: {
    "meaning": "마늘",
    "story": "1. Peeling a white clove. 2. Chopping it finely. 3. Sizzling it in olive oil. 4. The kitchen smelling of delicious garlic."
  },
  199: {
    "meaning": "어린 양",
    "story": "1. A green meadow in spring. 2. A white fluffy lamb. 3. Bleating softly 'Baa'. 4. Following its mother sheep."
  },
  200: {
    "meaning": "바늘",
    "story": "1. Holding a torn shirt. 2. Threading a thin metal needle. 3. Stitching the fabric carefully. 4. The tear is repaired invisibly."
  }
}

if __name__ == "__main__":
    vocab_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "data", "vocab.json")
    print(f"Updating vocab at: {vocab_path}")
    enrich_util.update_vocab(vocab_path, updates)
