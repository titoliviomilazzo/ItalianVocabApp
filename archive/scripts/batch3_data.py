import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import enrich_util

updates = {
  201: {
    "meaning": "고통, 임종",
    "story": "1. A person lying in a hospital bed. 2. Family members gathered around, holding hands. 3. The heart monitor beeping slowly. 4. A moment of final goodbye."
  },
  202: {
    "meaning": "8월",
    "story": "1. A calendar showing August. 2. People swimming at a crowded beach. 3. Ice cream melting in the hot sun. 4. Fireworks lighting up the summer night."
  },
  203: {
    "meaning": "농업의",
    "story": "1. Wide green fields stretching to the horizon. 2. A tractor plowing the soil. 3. Crops growing in neat rows. 4. A sign reading 'Agricultural Zone'."
  },
  204: {
    "meaning": "농부",
    "story": "1. Waking up at sunrise on a farm. 2. Feeding chickens and collecting eggs. 3. Driving a tractor through a wheat field. 4. Selling fresh produce at a market."
  },
  205: {
    "meaning": "농업",
    "story": "1. An ancient farmer planting seeds by hand. 2. Modern machines harvesting grain. 3. A graph showing crop production. 4. Agriculture feeding the world."
  },
  206: {
    "meaning": "감귤류",
    "story": "1. A basket full of oranges, lemons, and limes. 2. Cutting a grapefruit in half. 3. Squeezing fresh lemon juice. 4. The tangy, refreshing taste of citrus."
  },
  207: {
    "meaning": "날카롭게 하다",
    "story": "1. Holding a dull pencil. 2. Putting it into a sharpener. 3. Turning the crank carefully. 4. A perfectly sharp point ready to write."
  },
  208: {
    "meaning": "뾰족한",
    "story": "1. A mountain peak covered in snow. 2. A cactus with sharp spines. 3. A needle pointing upward. 4. Everything looking sharp and pointed."
  },
  209: {
    "meaning": "화단",
    "story": "1. An empty patch of soil in a garden. 2. Planting colorful flowers in rows. 3. Watering them with a small can. 4. A beautiful flower bed in full bloom."
  },
  210: {
    "meaning": "돕다",
    "story": "1. An elderly person struggling with grocery bags. 2. A young person running over. 3. Carrying the bags to the car. 4. A grateful smile and a 'thank you'."
  },
  211: {
    "meaning": "도움",
    "story": "1. A person stuck in quicksand. 2. Shouting 'Aiuto! Help!' loudly. 3. Someone throwing a rope. 4. Being pulled to safety."
  },
  212: {
    "meaning": "날개",
    "story": "1. A bird spreading its wings wide. 2. An airplane wing seen from a window. 3. A butterfly with colorful wings. 4. The symbol of freedom and flight."
  },
  213: {
    "meaning": "새벽, 여명",
    "story": "1. A dark sky before sunrise. 2. The horizon turning pink and orange. 3. The first rays of sunlight. 4. A new day begins at dawn."
  },
  214: {
    "meaning": "알바니아의, 알바니아인",
    "story": "1. A map of southeastern Europe. 2. Pointing to Albania on the Adriatic coast. 3. The Albanian flag with a double-headed eagle. 4. Historic stone buildings in Berat."
  },
  215: {
    "meaning": "호텔, 여관",
    "story": "1. Arriving at a fancy hotel entrance. 2. Checking in at the reception desk. 3. A bellboy carrying luggage to the room. 4. Relaxing in a comfortable bed."
  },
  216: {
    "meaning": "나무",
    "story": "1. A tiny seed in the ground. 2. A small sapling growing. 3. A tall oak tree with thick branches. 4. Children playing under its shade."
  },
  217: {
    "meaning": "살구",
    "story": "1. An orange fruit hanging from a tree. 2. Picking it gently. 3. Cutting it open to reveal the pit. 4. Tasting the sweet, soft apricot."
  },
  218: {
    "meaning": "앨범",
    "story": "1. Opening a photo album on the table. 2. Seeing childhood pictures. 3. Laughing at funny memories. 4. Adding a new photo to the collection."
  },
  219: {
    "meaning": "알코올",
    "story": "1. A bottle of wine being poured. 2. A beer mug with foam. 3. A 'No drinking and driving' sign. 4. A pharmacy shelf with rubbing alcohol."
  },
  220: {
    "meaning": "어떤, 약간의",
    "story": "1. Looking inside a nearly empty fridge. 2. Finding some leftover cheese. 3. Checking if any milk is left. 4. Making do with what little there is."
  },
  221: {
    "meaning": "알파벳",
    "story": "1. A child's ABC poster on the wall. 2. Pointing at the letter A. 3. Singing the alphabet song. 4. Writing all 26 letters on paper."
  },
  222: {
    "meaning": "해조, 조류",
    "story": "1. Walking along a rocky beach. 2. Seeing green seaweed on the rocks. 3. A diver swimming through underwater kelp. 4. Seaweed used in sushi rolls."
  },
  223: {
    "meaning": "알제리의, 알제리인",
    "story": "1. A map of North Africa. 2. Pointing to Algeria, the largest African country. 3. The Algerian flag (green and white with red star). 4. The Sahara desert landscape."
  },
  224: {
    "meaning": "외계인, 이질적인",
    "story": "1. A flying saucer in the night sky. 2. A green creature stepping out. 3. Raising a hand saying 'We come in peace'. 4. An alien encounter in the movies."
  },
  225: {
    "meaning": "식품의, 식량의",
    "story": "1. Walking through a supermarket aisle. 2. Reading 'Food Products' on a sign. 3. Checking nutritional labels. 4. Filling the cart with alimentary goods."
  },
  226: {
    "meaning": "먹이다, 공급하다",
    "story": "1. A mother bird bringing a worm. 2. Baby birds opening their beaks. 3. Feeding them one by one. 4. The chicks growing bigger each day."
  },
  227: {
    "meaning": "식료품점",
    "story": "1. A small corner shop with a striped awning. 2. Fresh fruits and vegetables displayed outside. 3. The owner greeting customers warmly. 4. Buying bread, cheese, and ham."
  },
  228: {
    "meaning": "영양, 식사",
    "story": "1. A food pyramid diagram. 2. Fruits, veggies, grains, and protein. 3. A balanced meal on a plate. 4. Healthy nutrition for a strong body."
  },
  229: {
    "meaning": "음식, 식품",
    "story": "1. A table full of different dishes. 2. Pasta, salad, bread, and fruit. 3. Choosing what to eat. 4. Food that nourishes the body."
  },
  230: {
    "meaning": "입김, 숨결",
    "story": "1. A cold winter morning. 2. Breathing out and seeing white mist. 3. Fogging up a glass window. 4. Drawing a smiley face in the breath."
  },
  231: {
    "meaning": "묶다, 잠그다",
    "story": "1. Looking down at untied shoes. 2. Bending down. 3. Tying the laces in a bow. 4. Standing up ready to walk."
  },
  232: {
    "meaning": "침수시키다",
    "story": "1. Heavy rain pouring for days. 2. A river overflowing its banks. 3. Streets turning into rivers. 4. Houses flooded up to the windows."
  },
  233: {
    "meaning": "넓히다",
    "story": "1. A narrow road with traffic jams. 2. Construction workers with machines. 3. Adding extra lanes. 4. The widened road flowing smoothly."
  },
  234: {
    "meaning": "경보를 울리다",
    "story": "1. Smoke detected in a building. 2. Someone pulling the fire alarm. 3. A loud siren blaring. 4. Everyone evacuating in an orderly fashion."
  },
  235: {
    "meaning": "경보, 경보기",
    "story": "1. An alarm clock ringing at 7 AM. 2. A car alarm going off in the parking lot. 3. A fire alarm flashing red. 4. All kinds of alarms alerting people."
  },
  236: {
    "meaning": "젖을 먹이다",
    "story": "1. A mother holding a newborn baby. 2. The baby crying for milk. 3. Breastfeeding the infant gently. 4. The baby falling asleep peacefully."
  },
  237: {
    "meaning": "동맹",
    "story": "1. Two medieval kings meeting. 2. Signing a treaty on parchment. 3. Shaking hands firmly. 4. Their armies marching together as allies."
  },
  238: {
    "meaning": "동맹을 맺다",
    "story": "1. Two small companies struggling alone. 2. Discussing a partnership over coffee. 3. Signing a cooperation agreement. 4. Growing stronger together."
  },
  239: {
    "meaning": "동맹국, 동맹한",
    "story": "1. A group of nations around a table. 2. Flags of allied countries displayed. 3. Working together on a common goal. 4. Stronger as united allies."
  },
  240: {
    "meaning": "첨부 파일",
    "story": "1. Writing an email on a computer. 2. Clicking the paperclip icon. 3. Selecting a document to attach. 4. Sending the email with the attachment."
  },
  241: {
    "meaning": "가볍게 하다",
    "story": "1. A backpack that's too heavy. 2. Removing unnecessary books. 3. Taking out the water bottle. 4. The bag feels much lighter now."
  },
  242: {
    "meaning": "기쁨, 즐거움",
    "story": "1. A child running to open birthday presents. 2. Jumping up and down with excitement. 3. Friends singing and dancing. 4. Pure joy and happiness."
  },
  243: {
    "meaning": "즐거운, 쾌활한",
    "story": "1. A person whistling a happy tune. 2. Wearing bright, colorful clothes. 3. Smiling at everyone on the street. 4. Spreading cheerful energy everywhere."
  },
  244: {
    "meaning": "훈련",
    "story": "1. A soccer player lacing up cleats. 2. Doing warm-up stretches. 3. Running drills on the field. 4. Exhausted but stronger after training."
  },
  245: {
    "meaning": "훈련하다",
    "story": "1. A boxing coach holding pads. 2. A boxer throwing punch combinations. 3. Sweating through intense rounds. 4. Getting ready for the big fight."
  },
  246: {
    "meaning": "감독, 코치",
    "story": "1. A man in a tracksuit on the sideline. 2. Shouting tactics to the team. 3. Drawing plays on a whiteboard. 4. Celebrating a victory with the players."
  },
  247: {
    "meaning": "느슨하게 하다",
    "story": "1. A belt that's too tight after dinner. 2. Reaching down to the buckle. 3. Loosening it by one notch. 4. Breathing comfortably again."
  },
  248: {
    "meaning": "알레르기",
    "story": "1. Spring flowers blooming everywhere. 2. Sneezing uncontrollably. 3. Eyes watering and nose running. 4. Taking an antihistamine for relief."
  },
  249: {
    "meaning": "기르다, 사육하다",
    "story": "1. A farm with baby chicks. 2. Feeding them grain daily. 3. Keeping them warm in a coop. 4. The chicks growing into healthy hens."
  },
  250: {
    "meaning": "학생, 제자",
    "story": "1. A classroom full of students. 2. A teacher writing on the board. 3. A student raising a hand to answer. 4. Getting an A on the test."
  },
  251: {
    "meaning": "정렬하다",
    "story": "1. Books scattered randomly on a shelf. 2. Taking them all down. 3. Arranging them by size and color. 4. A perfectly aligned bookshelf."
  },
  252: {
    "meaning": "숙소",
    "story": "1. Searching for a place to stay online. 2. Comparing hotels and hostels. 3. Booking a cozy apartment. 4. Arriving at the accommodation with bags."
  },
  253: {
    "meaning": "멀리하다, 떼어놓다",
    "story": "1. A dog getting too close to a cake. 2. Picking up the dog gently. 3. Moving it to another room. 4. Keeping the cake safe and untouched."
  },
  254: {
    "meaning": "그때, 그러면",
    "story": "1. Someone asking 'What did you do then?'. 2. Thinking back to that moment. 3. Remembering the exact events. 4. 'Well, then I decided to leave'."
  },
  255: {
    "meaning": "엄지발가락",
    "story": "1. Stubbing a toe on a table leg. 2. Hopping around in pain. 3. Looking down at the swollen big toe. 4. Putting ice on it carefully."
  },
  256: {
    "meaning": "암시하다, 넌지시 말하다",
    "story": "1. A friend asking about birthday plans. 2. Dropping subtle hints about a surprise. 3. Winking and changing the subject. 4. Not saying it directly but hinting."
  },
  257: {
    "meaning": "알루미늄",
    "story": "1. A shiny roll of aluminum foil. 2. Wrapping leftover food. 3. A crushed soda can for recycling. 4. Lightweight metal used everywhere."
  },
  258: {
    "meaning": "늘이다, 길게 하다",
    "story": "1. A piece of dough on a table. 2. Rolling it with a pin. 3. Stretching it longer and thinner. 4. A perfectly elongated pasta shape."
  },
  259: {
    "meaning": "홍수",
    "story": "1. Dark storm clouds gathering. 2. Torrential rain falling for hours. 3. Rivers bursting their banks. 4. A town submerged in floodwater."
  },
  260: {
    "meaning": "적어도",
    "story": "1. Wanting to buy a car but having little money. 2. Checking the minimum price. 3. Finding a used one that works. 4. At least having basic transportation."
  },
  261: {
    "meaning": "다소, 상당히",
    "story": "1. Tasting a new dish. 2. Finding it somewhat spicy. 3. It's not terrible but not great. 4. A rather unusual flavor."
  },
  262: {
    "meaning": "그네",
    "story": "1. A playground with a wooden swing. 2. A child sitting on the seat. 3. Being pushed higher and higher. 4. Laughing as they swing back and forth."
  },
  263: {
    "meaning": "매우, 고도로",
    "story": "1. A scientist in a lab coat. 2. Working on a highly complex experiment. 3. The results are extremely precise. 4. A highly successful research project."
  },
  264: {
    "meaning": "제단",
    "story": "1. Walking into an old church. 2. Seeing a decorated marble altar. 3. Candles and flowers placed on it. 4. A sacred place for worship."
  },
  265: {
    "meaning": "변경하다, 바꾸다",
    "story": "1. A photo being edited on a computer. 2. Changing the colors and contrast. 3. The original image looking different. 4. The altered version saved as new."
  },
  266: {
    "meaning": "교대하다, 번갈아 하다",
    "story": "1. Two drivers on a long road trip. 2. One drives for two hours. 3. Then they switch seats. 4. Taking turns alternating the driving."
  },
  267: {
    "meaning": "대안",
    "story": "1. A road blocked by construction. 2. Checking the GPS for another route. 3. Finding two alternative paths. 4. Choosing the faster option."
  },
  268: {
    "meaning": "대안의",
    "story": "1. A doctor suggesting standard medicine. 2. The patient asking about other options. 3. Trying herbal and natural remedies. 4. An alternative approach to healing."
  },
  269: {
    "meaning": "교대의, 번갈아 하는",
    "story": "1. Workers doing rotating shifts. 2. One team works mornings. 3. The other team works nights. 4. Alternating schedules throughout the week."
  },
  270: {
    "meaning": "높이, 키",
    "story": "1. A child standing against a wall. 2. A parent marking their height with a pencil. 3. Measuring with a tape. 4. 'You've grown 5 centimeters!'"
  },
  271: {
    "meaning": "높은",
    "story": "1. Looking up at a skyscraper downtown. 2. A tall giraffe at the zoo. 3. A high mountain with snow. 4. Everything reaching toward the sky."
  },
  272: {
    "meaning": "남티롤의",
    "story": "1. A map of northern Italy. 2. The South Tyrol region highlighted. 3. Mountains with Austrian-style villages. 4. German and Italian signs side by side."
  },
  273: {
    "meaning": "고원",
    "story": "1. Climbing a steep mountain trail. 2. Reaching a flat area at the top. 3. A wide, grassy plateau stretching out. 4. Spectacular views from the highland."
  },
  274: {
    "meaning": "마찬가지로, 같은 만큼",
    "story": "1. Two friends both scoring 90 on a test. 2. One says 'Good job!' to the other. 3. The other replies 'Likewise, you too!'. 4. Both equally proud of the score."
  },
  275: {
    "meaning": "그렇지 않으면",
    "story": "1. Setting an alarm for 7 AM. 2. 'Wake up, otherwise you'll be late.' 3. Imagining missing the bus. 4. Jumping out of bed immediately."
  },
  276: {
    "meaning": "다른, 그 밖의",
    "story": "1. Finishing one book on the shelf. 2. Reaching for another one. 3. Then yet another after that. 4. So many other books to read."
  },
  277: {
    "meaning": "다른 곳에",
    "story": "1. Looking for keys in the kitchen. 2. Not finding them anywhere. 3. Thinking 'They must be elsewhere.' 4. Finding them in the coat pocket."
  },
  278: {
    "meaning": "남의, 타인의",
    "story": "1. Seeing a shiny bicycle unlocked. 2. Thinking about touching it. 3. Remembering 'It belongs to someone else.' 4. Walking away respectfully."
  },
  279: {
    "meaning": "학생, 생도",
    "story": "1. A school bell ringing in the morning. 2. Students walking into the classroom. 3. Opening textbooks on the desks. 4. A school day of learning begins."
  },
  280: {
    "meaning": "벌집",
    "story": "1. A wooden box in a garden. 2. Bees buzzing in and out. 3. Hexagonal honeycomb inside. 4. Golden honey dripping from the hive."
  },
  281: {
    "meaning": "올리다, 들어올리다",
    "story": "1. A flag at the bottom of a pole. 2. Pulling the rope hand over hand. 3. The flag rising slowly. 4. Fluttering proudly at the top."
  },
  282: {
    "meaning": "연인, 애호가",
    "story": "1. Two people holding hands in a park. 2. A music lover at a concert. 3. A book lover in a library. 4. Passionate about what they love."
  },
  283: {
    "meaning": "사랑하다",
    "story": "1. A couple watching a sunset together. 2. A parent reading a bedtime story. 3. A heart drawn in the sand. 4. Love expressed in many ways."
  },
  284: {
    "meaning": "쓴, 씁쓸한",
    "story": "1. Biting into dark chocolate. 2. The bitter taste surprising the mouth. 3. Making a sour face. 4. Needing something sweet to balance it."
  },
  285: {
    "meaning": "사랑받는",
    "story": "1. A person receiving many birthday cards. 2. Surrounded by friends and family. 3. Gifts piling up on the table. 4. Feeling truly loved and cherished."
  },
  286: {
    "meaning": "대사관",
    "story": "1. A large building with a country's flag. 2. Security guards at the entrance. 3. People applying for visas inside. 4. The official embassy of a nation."
  },
  287: {
    "meaning": "환경의",
    "story": "1. A factory emitting smoke. 2. Protesters with green signs. 3. 'Protect the environment!' banners. 4. New environmental laws being passed."
  },
  288: {
    "meaning": "배경을 설정하다",
    "story": "1. A novelist writing a story. 2. Choosing a setting: 1920s Paris. 3. Describing cobblestone streets and cafés. 4. The story perfectly set in its time."
  },
  289: {
    "meaning": "환경, 분위기",
    "story": "1. Walking into a cozy restaurant. 2. Soft music and dim lighting. 3. Plants and warm wooden furniture. 4. A relaxing and pleasant environment."
  },
  290: {
    "meaning": "범위, 영역",
    "story": "1. A scientist studying marine biology. 2. An artist working in digital design. 3. A lawyer specializing in contracts. 4. Each expert in their own field."
  },
  291: {
    "meaning": "야망, 포부",
    "story": "1. A student dreaming of becoming a doctor. 2. Studying hard every night. 3. Getting accepted to medical school. 4. Ambition driving success forward."
  },
  292: {
    "meaning": "구급차",
    "story": "1. Someone calling 911 urgently. 2. Sirens wailing in the distance. 3. A white ambulance racing through traffic. 4. Paramedics rushing to help."
  },
  293: {
    "meaning": "미국의, 미국인",
    "story": "1. The Statue of Liberty standing tall. 2. A baseball game on a sunny day. 3. A yellow taxi in New York. 4. The American dream in action."
  },
  294: {
    "meaning": "우정",
    "story": "1. Two kids meeting on the first day of school. 2. Sharing lunch and playing together. 3. Growing up as best friends. 4. A lifelong bond of friendship."
  },
  295: {
    "meaning": "친구",
    "story": "1. Calling a friend after a bad day. 2. Meeting for coffee and talking. 3. Laughing until the sadness fades. 4. A true friend always there for you."
  },
  296: {
    "meaning": "찌그러뜨리다",
    "story": "1. Dropping a phone on the ground. 2. Picking it up and seeing a dent. 3. A car bumper with a small ding. 4. Surfaces bruised by impact."
  },
  297: {
    "meaning": "병에 걸리다",
    "story": "1. Getting caught in the rain without an umbrella. 2. Feeling a sore throat the next day. 3. Temperature rising to a fever. 4. Staying in bed, having fallen ill."
  },
  298: {
    "meaning": "아픈, 병든",
    "story": "1. A person coughing in bed. 2. A thermometer showing high temperature. 3. Medicine and tissues on the nightstand. 4. Waiting to recover from sickness."
  },
  299: {
    "meaning": "수갑을 채우다",
    "story": "1. A police officer chasing a suspect. 2. Catching them at a dead end. 3. Clicking handcuffs onto their wrists. 4. Leading them to the patrol car."
  },
  300: {
    "meaning": "쌓다, 모으다",
    "story": "1. Collecting coins in a piggy bank. 2. Adding more every week. 3. The bank getting heavier and heavier. 4. Breaking it open to find a pile of savings."
  }
}

if __name__ == "__main__":
    vocab_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "data", "vocab.json")
    print(f"Updating vocab at: {vocab_path}")
    enrich_util.update_vocab(vocab_path, updates)
