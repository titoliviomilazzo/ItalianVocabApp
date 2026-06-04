from enrich_util import update_vocab

batch1_data_p2 = {
    21: {
        "meaning": "포옹",
        "story": "1. Two people waving at each other at an airport. 2. Running quickly to close the distance. 3. Wrapping arms around each other tightly. 4. Smiling with eyes closed during the long hug."
    },
    22: {
        "meaning": "줄이다, 요약하다, 단축하다",
        "story": "1. Looking at a very long, thick book. 2. Writing a short summary on a small notepad. 3. Cutting a long piece of string with scissors. 4. The result is a much shorter, manageable object."
    },
    23: {
        "meaning": "구리빛으로 태우다, 선탠하다",
        "story": "1. Character lying on a beach towel under a bright sun. 2. Putting on sunscreen and relaxing. 3. The skin turning from pale to a healthy golden brown. 4. Showing off the tan lines after a day at the beach."
    },
    24: {
        "meaning": "전나무",
        "story": "1. Walking through a snowy forest. 2. Finding a tall, green evergreen tree. 3. Decorating the tree with lights and stars. 4. A beautiful Christmas tree glowing in the living room."
    },
    25: {
        "meaning": "숙련된, 유능한, 솜씨 좋은",
        "story": "1. A character looking at a pile of broken tools. 2. A master craftsman picking up a hammer. 3. Fixing everything with fast, precise movements. 4. The craftsman smiling next to perfectly repaired items."
    },
    26: {
        "meaning": "능력, 재능, 솜씨",
        "story": "1. A beginner trying to juggle two balls. 2. Watching a street performer juggling five balls at once. 3. Practice and sweat over many days. 4. The character successfully juggling three balls with a grin."
    },
    27: {
        "meaning": "심연, 깊은 구렁, 지옥",
        "story": "1. Standing at the edge of a deep dark canyon. 2. Looking down into the endless black void. 3. Dropping a small stone and waiting for the sound. 4. The stone disappears into the silence of the abyss."
    },
    28: {
        "meaning": "거주자, 주민",
        "story": "1. An empty apartment building. 2. A moving truck arrives with boxes. 3. A person carrying a lamp into the lobby. 4. Lights turning on in the windows as people move in."
    },
    29: {
        "meaning": "거주하다, 살다",
        "story": "1. Looking at a world map. 2. Pointing at a specific cozy house in Italy. 3. Putting a nameplate on the door 'Qui abita Mario'. 4. Relaxing in the living room with a book."
    },
    30: {
        "meaning": "주택, 거처, 집",
        "story": "1. A blueprint of a house on a table. 2. Workers building brick walls. 3. Painting the shutters a bright green color. 4. A finished, beautiful home with smoke coming from the chimney."
    },
    31: {
        "meaning": "옷, 복장, 관습",
        "story": "1. Waking up in pajamas. 2. Choosing a sharp suit for work. 3. Checking the tie and collar in the mirror. 4. Walking out the door looking professional and neat."
    },
    32: {
        "meaning": "습관적인, 평소의",
        "story": "1. Waking up at exactly 7 AM every day. 2. Walking the same path to the cafe. 3. The barista already preparing the 'usual' coffee. 4. Character sitting in the same favorite chair."
    },
    33: {
        "meaning": "길들이다, 가르치다, 익숙하게 하다",
        "story": "1. A wild dog barking at everyone. 2. A trainer offering a treat patiently. 3. Teaching the dog to sit and stay. 4. The dog calmly sitting next to its happy owner."
    },
    34: {
        "meaning": "습관, 관습",
        "story": "1. Checking a calendar with daily checkmarks. 2. Drinking a glass of water every morning. 3. Doing daily stretches upon waking. 4. A healthy character feeling energetic from the routine."
    },
    35: {
        "meaning": "폐지하다, 무효로 하다",
        "story": "1. A wall covered in old, restrictive law posters. 2. A leader crossing out the posters with a big red 'X'. 3. People cheering as the posters are removed. 4. Freedom and celebration in a clean, open plaza."
    },
    36: {
        "meaning": "유산하다, 실패하다, 중단되다",
        "story": "1. Planning a big grand opening for a shop. 2. A sudden heavy storm washes away the decorations. 3. Seeing a 'Closed/Cancelled' sign on the door. 4. The owner looking sadly at the unfinished project."
    },
    37: {
        "meaning": "유산, 실패",
        "story": "1. A bird's nest with a cracked egg. 2. No baby bird inside. 3. The nest looking lonely in the tree. 4. A gray rainy day reflecting the sadness of loss."
    },
    38: {
        "meaning": "아브루초 사람의, 아브루초의",
        "story": "1. A map of the Abruzzo region in Italy. 2. Mountains and sheep grazing in the distance. 3. A person holding a traditional Arrosticini skewer. 4. Celebrating a local festival in a hill town."
    },
    39: {
        "meaning": "남용하다, 악용하다",
        "story": "1. A person taking one candy from a bowl. 2. Another person grabbing the whole bowl. 3. Eating so much they get a stomach ache. 4. Regret while sitting next to many empty wrappers."
    },
    40: {
        "meaning": "남용, 부당한 대우",
        "story": "1. A person using a hammer for everything, even a glass. 2. The glass shatters under the heavy tool. 3. Looking at the mess on the floor. 4. Realizing the tool was used incorrectly and too forcefully."
    },
    41: {
        "meaning": "알파벳 H",
        "story": "1. A child trying to pronounce the silent 'H' in 'Hotel'. 2. Writing a large capital 'H' on the paper. 3. Realizing the letter is there but doesn't make a sound. 4. Looking at a dictionary entry for 'Acca'."
    },
    42: {
        "meaning": "학술원, 예술 학교, 아카데미",
        "story": "1. A grand old building with stone columns. 2. Students inside painting on canvases. 3. A professor giving a lecture on art history. 4. An exhibition of beautiful masterpieces in the hallway."
    },
    43: {
        "meaning": "학문적인, 이론적인",
        "story": "1. A stack of complex research papers. 2. A character wearing a graduation gown. 3. Writing a long thesis at a library desk. 4. Receiving a diploma for academic achievement."
    },
    44: {
        "meaning": "일어나다, 발생하다",
        "story": "1. A quiet street with nothing happening. 2. Suddenly, a street performer starts a show. 3. People gather around in surprise to watch. 4. Everyone talking about what just happened."
    },
    45: {
        "meaning": "야영지, 캠프",
        "story": "1. Arriving at a forest clearing with backpacks. 2. Pitching tents under the tall trees. 3. Building a warm campfire as the sun sets. 4. Sleeping peacefully inside the tents under the stars."
    },
    46: {
        "meaning": "옆에, 곁에",
        "story": "1. A single chair in an empty room. 2. Placing another chair right next to it. 3. Two friends sitting in the chairs together. 4. Sharing a snack side-by-side."
    },
    47: {
        "meaning": "목욕 가운",
        "story": "1. Stepping out of a steaming hot shower. 2. Reaching for a soft, fluffy white robe. 3. Wrapping the robe around and feeling warm. 4. Relaxing on the sofa with a towel on the head."
    },
    48: {
        "meaning": "애무하다, 쓰다듬다",
        "story": "1. A cat sitting on a person's lap. 2. A hand gently stroking the cat's fur. 3. The cat purring and closing its eyes. 4. A peaceful moment of affection between pet and owner."
    },
    49: {
        "meaning": "부랑자, 거지 / (영화 제목) 아카토네",
        "story": "1. A character in tattered clothes sitting on a curb. 2. Watching a busy city street from below. 3. Receiving a small coin from a passerby. 4. A gritty, realistic black-and-white scene like an old movie."
    },
    50: {
        "meaning": "포개다, 겹치다 / (다리를) 꼬다",
        "story": "1. Sitting in a chair while waiting for an interview. 2. Crossing one leg over the other for comfort. 3. Stacking books on top of each other in a pile. 4. Crossing arms while thinking deeply."
    }
}

if __name__ == "__main__":
    update_vocab("assets/data/vocab.json", batch1_data_p2)
