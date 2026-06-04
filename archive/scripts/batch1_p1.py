from enrich_util import update_vocab

batch1_data = {
    1: {
        "meaning": "알파벳 A",
        "story": "1. Looking at an alphabet book. 2. Pointing at the large letter 'A'. 3. Writing 'A' on a chalkboard. 4. Holding up an apple (mela) starting with 'A'."
    },
    2: {
        "meaning": "~으로, ~에, ~까지 (전치사)",
        "story": "1. Standing at a crossroads. 2. Seeing a sign pointing 'A Roma'. 3. Walking along the path. 4. Arriving at the Colosseum in Rome."
    },
    3: {
        "meaning": "눈부신, 현혹시키는",
        "story": "1. Driving at night in a dark tunnel. 2. A car coming from the opposite side with bright lights. 3. Character squinting and covering eyes. 4. Putting on sunglasses to block the glare."
    },
    4: {
        "meaning": "(개가) 짖다",
        "story": "1. A dog sleeping peacefully. 2. A mailman walks by the gate. 3. Dog jumps up quickly. 4. Dog barking loudly 'Bau! Bau!' at the mailman."
    },
    5: {
        "meaning": "버리다, 포기하다, 떠나다",
        "story": "1. A character standing in front of a messy house. 2. Packing a suitcase with a sad face. 3. Leaving the key on the table. 4. Walking away into the distance with a bag."
    },
    6: {
        "meaning": "버려진, 소외된",
        "story": "1. A busy playground with many kids. 2. A slide stands alone in the rain. 3. Dust and cobwebs covering the slide. 4. A lonely dog sitting next to the empty slide."
    },
    7: {
        "meaning": "포기, 유기, 방치",
        "story": "1. A plant in a pot looking dry. 2. A person walking past without watering it. 3. The plant drooping more and more. 4. An empty watering can lying nearby on dry ground."
    },
    8: {
        "meaning": "낮추다, 내리다",
        "story": "1. Music playing very loudly. 2. Neighbors complaining about the noise. 3. Character turning the volume knob down. 4. Everyone relaxing in a quiet room."
    },
    9: {
        "meaning": "아래로, 타도하라 (구호)",
        "story": "1. A person pointing down at the floor. 2. A group of protesters holding 'Abbasso' signs. 3. Dropping a heavy box to the ground. 4. A character looking down from a high balcony."
    },
    10: {
        "meaning": "충분히, 꽤",
        "story": "1. A chef pouring sugar into a bowl. 2. Tasting the mixture with a spoon. 3. Smiling and giving a thumbs up. 4. A full plate of cookies ready to eat."
    },
    11: {
        "meaning": "쓰러뜨리다, 격하시키다",
        "story": "1. A tall tower made of blocks. 2. A character pointing a finger at it. 3. Pushing the top block gently. 4. The entire tower crashing down into a pile."
    },
    12: {
        "meaning": "(가축에게) 물을 주다",
        "story": "1. A thirsty cow standing in the field. 2. Character bringing a bucket of water. 3. Cow drinking happily from the bucket. 4. The cow looking refreshed and healthy."
    },
    13: {
        "meaning": "복장, 의류",
        "story": "1. Looking into an empty closet. 2. Shopping at a clothing store. 3. Trying on a stylish suit in the mirror. 4. Walking out dressed elegantly in new clothes."
    },
    14: {
        "meaning": "결합하다, 짝을 맞추다",
        "story": "1. Holding a blue sock. 2. Searching through a pile of laundry. 3. Finding the matching blue sock. 4. Wearing both socks together perfectly."
    },
    15: {
        "meaning": "구독, 예매권",
        "story": "1. Standing at a train station ticket window. 2. Buying a monthly pass card. 3. Swiping the card at the gate. 4. Sitting comfortably on the train for the commute."
    },
    16: {
        "meaning": "구독하다, 가입시키다",
        "story": "1. Reading an interesting magazine online. 2. Clicking the 'Subscribe' button. 3. Getting a welcome email on the phone. 4. Receiving the first printed magazine in the mailbox."
    },
    17: {
        "meaning": "풍부한, 넓은",
        "story": "1. A small bowl with one grape. 2. Looking at a huge basket full of diverse fruits. 3. A table overflowing with various delicious dishes. 4. Character smiling in front of the feast."
    },
    18: {
        "meaning": "풍부하다, 많이 있다",
        "story": "1. A dry riverbed with no water. 2. Rain falling heavily for hours. 3. The river filling up and overflowing. 4. Fish swimming happily in the deep water."
    },
    19: {
        "meaning": "단추를 채우다",
        "story": "1. Putting on a coat in the cold. 2. Fingers touching a wooden button. 3. Pushing the button through the hole. 4. Coat fully closed and character staying warm."
    },
    20: {
        "meaning": "껴안다, 포옹하다",
        "story": "1. Two best friends haven't seen each other in years. 2. Running towards each other with open arms. 3. A warm, joyful embrace. 4. Laughing together while still hugging."
    }
}

if __name__ == "__main__":
    update_vocab("assets/data/vocab.json", batch1_data)
