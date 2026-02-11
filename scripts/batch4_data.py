import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import enrich_util

updates = {
  301: {
    "meaning": "더미, 무더기",
    "story": "1. A garage full of old boxes. 2. Clothes piled on a chair. 3. Books stacked in a messy heap. 4. A massive pile of stuff everywhere."
  },
  302: {
    "meaning": "죽이다",
    "story": "1. A detective arriving at a crime scene. 2. Yellow tape around the area. 3. Clues scattered on the ground. 4. Solving a mystery about what happened."
  },
  303: {
    "meaning": "인정하다, 허용하다",
    "story": "1. A student caught cheating on a test. 2. The teacher asking what happened. 3. The student admitting the truth. 4. Accepting the consequences honestly."
  },
  304: {
    "meaning": "행정의",
    "story": "1. An office building with many departments. 2. Workers filing paperwork and forms. 3. A stamp of approval on a document. 4. Administrative work keeping things running."
  },
  305: {
    "meaning": "관리자",
    "story": "1. A person sitting behind a big desk. 2. Managing budgets and schedules. 3. Making important decisions for a company. 4. The administrator keeping order."
  },
  306: {
    "meaning": "행정, 관리",
    "story": "1. A government building with a flag. 2. Officials processing applications. 3. Public services being organized. 4. Administration serving the people."
  },
  307: {
    "meaning": "감탄하다",
    "story": "1. Standing before a famous painting. 2. Eyes wide with wonder. 3. Walking around a beautiful garden. 4. Admiring the beauty of art and nature."
  },
  308: {
    "meaning": "입학, 입장",
    "story": "1. Applying to a prestigious university. 2. Checking the mailbox nervously. 3. Opening the letter: 'You are admitted!' 4. Celebrating the admission with family."
  },
  309: {
    "meaning": "가구를 비치하다",
    "story": "1. An empty apartment with bare walls. 2. Choosing furniture at a store. 3. Assembling a sofa and bookshelf. 4. A fully furnished, cozy home."
  },
  310: {
    "meaning": "암모니아",
    "story": "1. Opening a cleaning product bottle. 2. A strong, sharp chemical smell. 3. Wearing gloves for safety. 4. Using ammonia to clean tough stains."
  },
  311: {
    "meaning": "섬유유연제",
    "story": "1. Taking clothes out of the washer. 2. They feel rough and stiff. 3. Adding fabric softener to the next load. 4. Clothes now soft and fragrant."
  },
  312: {
    "meaning": "쌓아 올리다",
    "story": "1. A child playing with building blocks. 2. Stacking them higher and higher. 3. The tower wobbling dangerously. 4. It crashes into a pile on the floor."
  },
  313: {
    "meaning": "곰팡이가 피다",
    "story": "1. Forgetting bread in the back of the pantry. 2. Finding it weeks later. 3. Green and white mold growing on it. 4. Throwing the moldy bread away."
  },
  314: {
    "meaning": "사랑",
    "story": "1. A heart-shaped box of chocolates. 2. A couple walking hand in hand. 3. A parent hugging their child. 4. Love expressed in many forms."
  },
  315: {
    "meaning": "사랑스러운",
    "story": "1. A couple sharing a warm embrace. 2. Writing love letters to each other. 3. Leaving sweet notes on the fridge. 4. A loving and tender relationship."
  },
  316: {
    "meaning": "넓게, 충분히",
    "story": "1. A topic discussed in great detail. 2. Covering every aspect thoroughly. 3. Widely recognized by experts. 4. Amply documented and researched."
  },
  317: {
    "meaning": "넓은, 광활한",
    "story": "1. A spacious living room with high ceilings. 2. Wide open fields stretching far. 3. A broad boulevard with trees. 4. Plenty of room to move around."
  },
  318: {
    "meaning": "앰프, 증폭기",
    "story": "1. A guitarist plugging into a small amp. 2. Turning the volume knob up. 3. The sound booming through the room. 4. The amplifier making music louder."
  },
  319: {
    "meaning": "무알코올의",
    "story": "1. At a bar looking at the menu. 2. Choosing a non-alcoholic cocktail. 3. A colorful mocktail served in a glass. 4. Enjoying the taste without alcohol."
  },
  320: {
    "meaning": "문맹자",
    "story": "1. A person staring at a letter they received. 2. Unable to read the words. 3. Asking a neighbor for help. 4. Deciding to join a literacy class."
  },
  321: {
    "meaning": "분석",
    "story": "1. A scientist looking at data charts. 2. Breaking down complex numbers. 3. Writing conclusions in a report. 4. A thorough analysis of the results."
  },
  322: {
    "meaning": "분석적인",
    "story": "1. A detective examining clues carefully. 2. Connecting dots on a board. 3. Using logic to solve the case. 4. An analytical mind at work."
  },
  323: {
    "meaning": "분석하다",
    "story": "1. Blood samples in test tubes. 2. Placing them under a microscope. 3. Running tests and comparisons. 4. Analyzing every detail for answers."
  },
  324: {
    "meaning": "유사한",
    "story": "1. Comparing two different smartphones. 2. Similar screen sizes and cameras. 3. Nearly identical features. 4. An analogous experience overall."
  },
  325: {
    "meaning": "파인애플",
    "story": "1. A tropical fruit stand on the beach. 2. A spiky yellow pineapple. 3. Cutting it into juicy rings. 4. The sweet and tangy taste of ananas."
  },
  326: {
    "meaning": "무정부주의자",
    "story": "1. A black flag with a circle-A symbol. 2. Protesters demanding no government. 3. Graffiti on city walls. 4. An anarchist movement in action."
  },
  327: {
    "meaning": "오리",
    "story": "1. A pond in a peaceful park. 2. A mother duck swimming with ducklings. 3. Quacking loudly for bread. 4. Ducks wadgling on the grass."
  },
  328: {
    "meaning": "~도, 역시",
    "story": "1. 'I like pizza.' 'Me too!' 2. Both friends ordering the same dish. 3. Even the waiter agrees. 4. Everyone also loves the dessert."
  },
  329: {
    "meaning": "안코나 출신의",
    "story": "1. A map pointing to Ancona on Italy's coast. 2. The city's port and harbor. 3. Local people enjoying seafood. 4. Proud to be from Ancona."
  },
  330: {
    "meaning": "아직, 다시",
    "story": "1. Asking 'Are we there yet?' in the car. 2. 'Not yet, we need more time.' 3. Waiting for the cookies to bake. 4. Still not ready, but almost!"
  },
  331: {
    "meaning": "닻을 내리다, 고정하다",
    "story": "1. A sailboat arriving at harbor. 2. Dropping the heavy anchor. 3. The chain rattling into the water. 4. The boat securely anchored in place."
  },
  332: {
    "meaning": "추세, 경향",
    "story": "1. A stock market chart on a screen. 2. Prices going up and down. 3. Analysts studying the trend. 4. Tracking the performance over time."
  },
  333: {
    "meaning": "가다",
    "story": "1. Putting on shoes at the door. 2. Walking down the street. 3. Taking a bus to the city. 4. Going wherever life takes you."
  },
  334: {
    "meaning": "가는 길, 편도",
    "story": "1. At the train station ticket counter. 2. 'One way or round trip?' 3. Buying a one-way ticket. 4. The outward journey begins."
  },
  335: {
    "meaning": "반지",
    "story": "1. A jeweler crafting a gold ring. 2. A diamond set in the center. 3. Getting down on one knee. 4. 'Will you marry me?' with the ring."
  },
  336: {
    "meaning": "천사",
    "story": "1. A painting of a figure with wings. 2. A golden halo above the head. 3. Watching over people from above. 4. A guardian angel protecting everyone."
  },
  337: {
    "meaning": "모서리의, 각의",
    "story": "1. A geometry class learning about angles. 2. Measuring a 90-degree corner. 3. An angular shape on the board. 4. Sharp corners everywhere."
  },
  338: {
    "meaning": "모서리, 구석",
    "story": "1. Two streets meeting at an intersection. 2. A cafe on the corner. 3. Turning left at the angle. 4. A cozy corner table inside."
  },
  339: {
    "meaning": "고뇌, 번민",
    "story": "1. A person sitting alone in the dark. 2. Hands covering their face. 3. Feeling a deep sense of dread. 4. Overwhelmed by anguish and worry."
  },
  340: {
    "meaning": "영혼, 마음",
    "story": "1. A person meditating peacefully. 2. A glowing light inside the chest. 3. The spirit feeling free. 4. Connecting with the innermost soul."
  },
  341: {
    "meaning": "동물 (명사)",
    "story": "1. A zoo with many different creatures. 2. Lions, elephants, and monkeys. 3. A dog playing in the park. 4. Animals of all shapes and sizes."
  },
  342: {
    "meaning": "동물의 (형용사)",
    "story": "1. Studying animal behavior in class. 2. Watching a documentary on instincts. 3. Animal instinct driving survival. 4. The animal kingdom's fascinating rules."
  },
  343: {
    "meaning": "활기를 불어넣다",
    "story": "1. A quiet party with nobody dancing. 2. The DJ changing to upbeat music. 3. People starting to dance and laugh. 4. The room now animated and alive."
  },
  344: {
    "meaning": "활기 있는",
    "story": "1. A lively marketplace full of colors. 2. People chatting and bargaining. 3. Musicians playing on the street. 4. An animated and bustling scene."
  },
  345: {
    "meaning": "정신, 용기",
    "story": "1. A soldier preparing for a challenge. 2. Taking a deep breath. 3. Summoning courage from within. 4. 'Coraggio! Have spirit!' someone shouts."
  },
  346: {
    "meaning": "물을 타다, 희석하다",
    "story": "1. A glass of strong juice. 2. Adding water to dilute it. 3. Stirring the weakened mixture. 4. The flavor now watered down."
  },
  347: {
    "meaning": "물을 주다",
    "story": "1. A garden of flowers on a hot day. 2. Filling a watering can. 3. Sprinkling water on each plant. 4. The flowers perking up happily."
  },
  348: {
    "meaning": "안개가 끼게 하다",
    "story": "1. A cold morning with fog rolling in. 2. Glasses fogging up indoors. 3. Car windshield covered in mist. 4. Everything clouded and hard to see."
  },
  349: {
    "meaning": "기념일",
    "story": "1. A couple looking at old wedding photos. 2. A calendar circled on a special date. 3. Celebrating with dinner and cake. 4. Happy anniversary together."
  },
  350: {
    "meaning": "년, 해",
    "story": "1. A calendar showing January 1st. 2. Twelve months passing one by one. 3. Seasons changing through the year. 4. December 31st – another year ends."
  },
  351: {
    "meaning": "매듭짓다",
    "story": "1. A sailor holding a thick rope. 2. Looping it around a post. 3. Pulling it tight into a knot. 4. The rope securely tied."
  },
  352: {
    "meaning": "지루하게 하다",
    "story": "1. Sitting in a long, boring lecture. 2. Eyes getting heavy. 3. Doodling on the notebook. 4. Yawning from pure boredom."
  },
  353: {
    "meaning": "적어두다, 메모하다",
    "story": "1. A professor saying something important. 2. Grabbing a pen quickly. 3. Writing it down in a notebook. 4. Notes ready for later study."
  },
  354: {
    "meaning": "연례의, 매년의",
    "story": "1. An invitation to the annual company party. 2. It happens every year in December. 3. Employees gathering to celebrate. 4. A yearly tradition everyone enjoys."
  },
  355: {
    "meaning": "고개를 끄덕이다",
    "story": "1. Someone asking a yes or no question. 2. Thinking for a moment. 3. Nodding the head slowly. 4. A silent 'yes' without words."
  },
  356: {
    "meaning": "취소하다, 무효화하다",
    "story": "1. Booking a hotel reservation online. 2. Plans changing unexpectedly. 3. Clicking the cancel button. 4. The reservation annulled and refunded."
  },
  357: {
    "meaning": "발표하다, 알리다",
    "story": "1. A CEO standing at a podium. 2. Microphones and cameras ready. 3. 'We are launching a new product!' 4. The big announcement makes headlines."
  },
  358: {
    "meaning": "공고, 발표",
    "story": "1. A bulletin board in a school hallway. 2. A new notice pinned to it. 3. Students gathering to read it. 4. An important announcement for everyone."
  },
  359: {
    "meaning": "냄새를 맡다",
    "story": "1. A dog walking on a trail. 2. Nose down, sniffing the ground. 3. Picking up a scent. 4. Following the smell to find a bone."
  },
  360: {
    "meaning": "익명의",
    "story": "1. A letter with no return address. 2. The author choosing to stay hidden. 3. A donation from an unknown person. 4. An anonymous act of kindness."
  },
  361: {
    "meaning": "불안",
    "story": "1. Waiting for exam results nervously. 2. Heart beating fast. 3. Biting nails and pacing. 4. Anxiety taking over the mind."
  },
  362: {
    "meaning": "불안한, 걱정하는",
    "story": "1. A job interview tomorrow morning. 2. Can't sleep, tossing and turning. 3. Going over answers in the head. 4. Feeling anxious about the outcome."
  },
  363: {
    "meaning": "남극의",
    "story": "1. A map showing the South Pole. 2. Penguins walking on ice. 3. A research base in the snow. 4. The Antarctic cold and beautiful."
  },
  364: {
    "meaning": "안테나",
    "story": "1. A TV antenna on a rooftop. 2. An insect's feelers moving. 3. A satellite dish pointing at the sky. 4. Antennas catching signals everywhere."
  },
  365: {
    "meaning": "미리보기, 시사회",
    "story": "1. A movie poster outside a theater. 2. 'Special preview showing tonight!' 3. Watching the film before its release. 4. An exclusive sneak peek for fans."
  },
  366: {
    "meaning": "앞의, 이전의",
    "story": "1. The front wheels of a car. 2. The anterior part of a building. 3. Something that came before. 4. The previous version of the design."
  },
  367: {
    "meaning": "석회 제거의",
    "story": "1. A faucet with white mineral buildup. 2. Spraying anti-limescale cleaner. 3. Scrubbing the deposits away. 4. A shiny, clean faucet again."
  },
  368: {
    "meaning": "고대, 골동품",
    "story": "1. A dusty old shop full of artifacts. 2. A Roman coin in a glass case. 3. Ancient pottery on the shelf. 4. Treasures from antiquity preserved."
  },
  369: {
    "meaning": "앞당기다, 예상하다",
    "story": "1. A meeting scheduled for Friday. 2. Moving it earlier to Wednesday. 3. Preparing ahead of time. 4. Anticipating the event with excitement."
  },
  370: {
    "meaning": "선불, 미리",
    "story": "1. Arriving at a party 30 minutes early. 2. Being the first one there. 3. Setting up decorations in advance. 4. Prepared well ahead of schedule."
  },
  371: {
    "meaning": "고대의, 오래된",
    "story": "1. The Colosseum standing for thousands of years. 2. Ancient Roman roads still visible. 3. Old manuscripts in a library. 4. History preserved from ancient times."
  },
  372: {
    "meaning": "에피타이저, 전채",
    "story": "1. Sitting at an Italian restaurant table. 2. The waiter bringing bruschetta. 3. Small plates of olives and cheese. 4. Delicious antipasto before the main course."
  },
  373: {
    "meaning": "주름 방지의",
    "story": "1. Looking in the mirror at fine lines. 2. Buying an anti-wrinkle cream. 3. Applying it gently every night. 4. Hoping for smoother, younger skin."
  },
  374: {
    "meaning": "인류학",
    "story": "1. A researcher visiting a remote village. 2. Studying local customs and rituals. 3. Writing notes about human cultures. 4. Anthropology: the study of humanity."
  },
  375: {
    "meaning": "약지 (손가락)",
    "story": "1. Looking at the fingers on a hand. 2. Counting from thumb to pinky. 3. The fourth finger: the ring finger. 4. Where wedding rings are worn."
  },
  376: {
    "meaning": "오히려, 그런데",
    "story": "1. Thinking the weather would be bad. 2. Looking outside: bright sunshine! 3. 'Anzi, it's actually beautiful today.' 4. On the contrary, it's perfect."
  },
  377: {
    "meaning": "노인, 연로한",
    "story": "1. An old man sitting on a park bench. 2. White hair and a walking cane. 3. Telling stories to grandchildren. 4. An elderly person full of wisdom."
  },
  378: {
    "meaning": "~하는 대신에",
    "story": "1. Planning to take the bus. 2. Deciding to walk instead. 3. Enjoying the fresh air. 4. Rather than riding, walking is better."
  },
  379: {
    "meaning": "아오스타 출신의",
    "story": "1. A map of northwestern Italy. 2. The Aosta Valley in the Alps. 3. Snowy mountains and ski resorts. 4. People from Aosta love the mountains."
  },
  380: {
    "meaning": "벌, 꿀벌",
    "story": "1. A yellow and black striped insect. 2. Buzzing from flower to flower. 3. Collecting pollen and making honey. 4. Bees essential for nature."
  },
  381: {
    "meaning": "아페리티보 (식전 음료)",
    "story": "1. Meeting friends at 6 PM. 2. Ordering a Spritz at a cafe. 3. Small snacks served alongside. 4. The Italian aperitivo tradition."
  },
  382: {
    "meaning": "열린, 개방된",
    "story": "1. A door standing wide open. 2. A book opened to the first page. 3. An open field with fresh air. 4. Arms open for a warm hug."
  },
  383: {
    "meaning": "개방, 오프닝",
    "story": "1. Scissors cutting a ribbon. 2. A new store's grand opening. 3. Crowds cheering and entering. 4. The opening of a new chapter."
  },
  384: {
    "meaning": "사도",
    "story": "1. Twelve followers gathered together. 2. Listening to a teacher's words. 3. Spreading the message to the world. 4. The apostles on their mission."
  },
  385: {
    "meaning": "입찰, 도급 계약",
    "story": "1. A city government posting a project. 2. Companies submitting bids. 3. Reviewing proposals and prices. 4. Awarding the contract to the winner."
  },
  386: {
    "meaning": "흐리게 하다, 김이 서리다",
    "story": "1. Stepping into a warm room from the cold. 2. Glasses instantly fogging up. 3. Wiping them with a cloth. 4. Vision clouded and unclear."
  },
  387: {
    "meaning": "장치, 기관",
    "story": "1. A scientist explaining the digestive system. 2. Organs working together as an apparatus. 3. A complex machine with many parts. 4. Every component has a function."
  },
  388: {
    "meaning": "식탁을 차리다",
    "story": "1. Dinner almost ready in the kitchen. 2. Laying a tablecloth on the table. 3. Placing plates, forks, and glasses. 4. The table perfectly set for dinner."
  },
  389: {
    "meaning": "장비, 설비",
    "story": "1. A hospital room full of equipment. 2. Monitors, tubes, and machines. 3. Medical apparatus saving lives. 4. Advanced equipment everywhere."
  },
  390: {
    "meaning": "기구, 장치",
    "story": "1. A telephone ringing on the desk. 2. A TV set in the living room. 3. A dental device in the mouth. 4. Appliances and devices we use daily."
  },
  391: {
    "meaning": "외견상의, 겉보기의",
    "story": "1. A calm ocean surface. 2. But underneath, strong currents. 3. Things are not what they seem. 4. An apparent peace hiding turmoil."
  },
  392: {
    "meaning": "외견상, 보기에는",
    "story": "1. A smiling person at a party. 2. But they look sad when alone. 3. Apparently happy, but really not. 4. Appearances can be deceiving."
  },
  393: {
    "meaning": "외관, 겉모습",
    "story": "1. A beautiful house from the outside. 2. But messy and old inside. 3. Judging only by appearance. 4. Looks can be misleading."
  },
  394: {
    "meaning": "나타나다",
    "story": "1. An empty stage with a curtain. 2. Lights dimming dramatically. 3. A magician suddenly appearing. 4. The audience gasping in surprise."
  },
  395: {
    "meaning": "출현, 발현",
    "story": "1. A ghost story around a campfire. 2. A mysterious figure in the fog. 3. People claiming to see an apparition. 4. A strange appearance in the night."
  },
  396: {
    "meaning": "아파트",
    "story": "1. A tall building with many floors. 2. Each floor has several apartments. 3. Unlocking the door to unit 4B. 4. Home sweet apartment."
  },
  397: {
    "meaning": "소속, 소속감",
    "story": "1. Joining a sports team. 2. Wearing the team jersey proudly. 3. Feeling part of the group. 4. A sense of belonging and identity."
  },
  398: {
    "meaning": "~에 속하다",
    "story": "1. A family crest on an old shield. 2. 'This land belongs to our family.' 3. Heritage passed down for generations. 4. Belonging to something greater."
  },
  399: {
    "meaning": "열중하게 하다",
    "story": "1. A gripping novel on the nightstand. 2. Reading page after page. 3. Unable to put it down. 4. The story passionately captivating."
  },
  400: {
    "meaning": "열중하다, 빠지다",
    "story": "1. Discovering a new hobby: painting. 2. Buying canvases and brushes. 3. Spending every evening painting. 4. Becoming passionately absorbed in art."
  }
}

if __name__ == "__main__":
    vocab_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "data", "vocab.json")
    print(f"Updating vocab at: {vocab_path}")
    enrich_util.update_vocab(vocab_path, updates)
