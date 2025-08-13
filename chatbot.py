# Simple AI Chatbot without sklearn, using a large dataset

# Friendly conversation dataset
training_data = [
    ("Hey, how’s your day going?", "Pretty good! How about you?"),
    ("I’m doing fine, thanks for asking.", "Glad to hear that!"),
    ("What are you up to today?", "Just relaxing at home. You?"),
    ("Same here, just taking it easy.", "Sometimes that’s the best way to spend the day."),
    ("Have you eaten yet?", "Yeah, I just had lunch."),
    ("What did you eat?", "I had some pasta, it was delicious."),
    ("Sounds nice!", "Yeah, it really hit the spot."),
    ("How’s the weather over there?", "It’s sunny and warm today."),
    ("Lucky you, it’s raining here.", "Rain can be cozy though."),
    ("True, I’m enjoying it with some tea.", "That sounds perfect."),
    ("Are you watching anything lately?", "Yeah, I just started a new show."),
    ("What’s it about?", "It’s a mystery series, really keeps me guessing."),
    ("I love mysteries!", "Same, they keep me hooked."),
    ("Do you like reading books?", "Yes, I read almost every night."),
    ("What kind of books?", "Mostly fantasy and adventure."),
    ("Sounds fun!", "Yeah, it’s a great escape."),
    ("Do you play games?", "Yes, sometimes in my free time."),
    ("What games do you play?", "Mostly puzzle and strategy games."),
    ("Cool, I like those too.", "We should play together sometime."),
    ("Yeah, that’d be great!", "Definitely!"),
    ("Have you traveled anywhere recently?", "Not lately, but I’d love to."),
    ("Where would you like to go?", "Somewhere with mountains and nature."),
    ("That sounds peaceful.", "Yeah, it would be."),
    ("Do you like cooking?", "Yes, I enjoy trying new recipes."),
    ("What’s your favorite dish to make?", "Probably homemade pizza."),
    ("Yum, pizza is the best!", "Totally agree."),
    ("Do you like pets?", "Yes, I love animals."),
    ("Do you have any pets?", "Yes, I have a cat."),
    ("What’s their name?", "Her name is Luna."),
    ("Cute name!", "Thanks, she’s adorable."),
    ("Do you enjoy walking outside?", "Yes, especially in the evening."),
    ("Evening walks are so relaxing.", "Yeah, I love the fresh air."),
    ("Do you like music?", "Yes, I listen every day."),
    ("What kind of music?", "Mostly pop and indie."),
    ("Nice, I like indie too.", "It’s got a great vibe."),
    ("Do you watch YouTube?", "Yes, pretty often."),
    ("What do you watch there?", "Mostly vlogs and tech videos."),
    ("Tech videos are interesting.", "Yeah, I like learning new things."),
    ("Do you like coffee?", "Yes, I can’t start my day without it."),
    ("Same, coffee is life!", "Totally!"),
    ("Do you like tea?", "Yes, especially in the evenings."),
    ("Tea is so calming.", "Yeah, I love herbal blends."),
    ("Do you like drawing?", "Yes, I doodle sometimes."),
    ("That’s cool!", "Thanks, it’s just for fun."),
    ("Do you like learning new skills?", "Yes, always!"),
    ("What’s the last thing you learned?", "I started learning guitar."),
    ("That’s awesome!", "Yeah, it’s challenging but fun."),
    ("Do you enjoy exercising?", "Yes, I try to stay active."),
    ("What’s your favorite workout?", "Probably jogging."),
    ("Jogging feels great.", "Yeah, it clears my mind."),
    ("Do you like beaches?", "Yes, I love the ocean."),
    ("Same here, so peaceful.", "Yeah, the waves are calming."),
    ("Do you enjoy late-night talks?", "Yes, those are the best."),
    ("Agreed, they feel so deep.", "Exactly!"),
    ("Do you like rainbows?", "Yes, they’re beautiful."),
    ("Totally, nature’s magic.", "For sure."),
    ("Do you like sunsets?", "Yes, I love watching them."),
    ("They’re so calming.", "Yeah, the colors are amazing."),
    ("Do you like stargazing?", "Yes, it’s magical."),
    ("Totally agree.", "It’s so peaceful."),
    ("Do you enjoy cooking together?", "Yes, it’s fun and bonding."),
    ("Same here!", "Yeah, it’s great.")
]

# Knowledge base Q&A
qa_data = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! How's your day going?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "good": "Glad to hear that!",
    "bad": "I'm sorry to hear that. Want to talk about it?",
    "what is your name": "I'm your friendly Ronit's chatbot!",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome!",
    "thanks": "No problem!",
    "what can you do": "I can chat with you and answer simple questions.",
    "who made you": "I was created by Ronit.",
    "tell me a joke": "Why did the computer go to the doctor? Because it caught a virus!",
    "what is python": "Python is a popular programming language used for many purposes.",
    "how old are you": "I was created just recently!",
    "where are you from": "I live in your computer's memory.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine learning is a subset of AI where computers learn from data.",
    "what is deep learning": "Deep learning is a type of machine learning using neural networks.",
    "what is data science": "Data science is the study of data to extract insights.",
    "what is coding": "Coding is the process of writing instructions for computers.",
    "what is programming": "Programming is creating a set of instructions for a computer to execute.",
    "what is java": "Java is a high-level programming language.",
    "what is html": "HTML is the standard markup language for creating web pages.",
    "what is css": "CSS is used to style HTML documents.",
    "what is javascript": "JavaScript is a programming language for web development.",
    "what is c++": "C++ is a general-purpose programming language.",
    "what is c": "C is one of the oldest programming languages.",
    "what is sql": "SQL is used to manage and query databases.",
    "what is firebase": "Firebase is a platform by Google for building apps.",
    "what is flutter": "Flutter is a UI toolkit by Google for building apps.",
    "what is github": "GitHub is a platform for hosting and sharing code.",
    "what is git": "Git is a version control system for tracking code changes.",
    "what is linux": "Linux is an open-source operating system.",
    "what is windows": "Windows is a popular operating system by Microsoft.",
    "what is macos": "macOS is Apple's operating system for computers.",
    "what is android": "Android is Google's mobile operating system.",
    "what is ios": "iOS is Apple's mobile operating system.",
    "what is cloud computing": "Cloud computing is storing and accessing data over the internet.",
    "what is blockchain": "Blockchain is a decentralized digital ledger.",
    "what is cryptocurrency": "Cryptocurrency is a digital currency secured by cryptography.",
    "what is bitcoin": "Bitcoin is the first and most popular cryptocurrency.",
    "what is ethereum": "Ethereum is a blockchain platform with smart contracts.",
    "what is nft": "NFT stands for Non-Fungible Token.",
    "what is metaverse": "The metaverse is a virtual shared space.",
    "what is vr": "VR stands for Virtual Reality.",
    "what is ar": "AR stands for Augmented Reality.",
    "what is mr": "MR stands for Mixed Reality.",
    "what is ai chatbot": "An AI chatbot is a program that simulates conversation.",
    "what is api": "API stands for Application Programming Interface.",
    "what is rest api": "A REST API is a web service that follows REST principles.",
    "what is json": "JSON is a lightweight data-interchange format.",
    "what is xml": "XML is a markup language for storing and transporting data.",
    "what is yaml": "YAML is a human-readable data serialization format.",
    "what is csv": "CSV is a comma-separated values file format.",
    "what is tsv": "TSV is a tab-separated values file format.",
    "what is big data": "Big data is large, complex data sets.",
    "what is iot": "IoT stands for Internet of Things.",
    "what is robotics": "Robotics is the design and use of robots.",
    "what is automation": "Automation is the use of technology to perform tasks automatically.",
    "what is devops": "DevOps is a set of practices combining development and operations.",
    "what is agile": "Agile is a project management methodology.",
    "what is scrum": "Scrum is an agile framework for managing projects.",
    "what is kanban": "Kanban is a workflow management method.",
    "what is waterfall model": "Waterfall is a sequential project management method.",
    "what is ai ethics": "AI ethics is the study of moral issues in AI.",
    "what is turing test": "The Turing Test checks if a machine can mimic human intelligence.",
    "what is neural network": "A neural network is a series of algorithms that mimic the brain.",
    "what is supervised learning": "Supervised learning is ML with labeled data.",
    "what is unsupervised learning": "Unsupervised learning is ML with unlabeled data.",
    "what is reinforcement learning": "RL is ML where agents learn via rewards and penalties."
}
training_data = [
    {"input": "Hi, how are you?", "output": "I'm good! How about you?"},
    {"input": "I'm doing fine, just relaxing.", "output": "Nice! Any plans for today?"},
    {"input": "Not really, maybe just watch a movie.", "output": "That sounds chill. Which one?"},
    {"input": "Probably a sci-fi, I love those.", "output": "Same here! Have you watched Interstellar?"},
    {"input": "Yes, it’s one of my favorites!", "output": "Mine too, the visuals were amazing."},
    {"input": "What are you up to?", "output": "Just working on some code."},
    {"input": "Hope it’s going well.", "output": "Yeah, making good progress."},
    {"input": "Hey bro, long time no see!", "output": "I know, man! How have you been?"},
    {"input": "Pretty good, just busy with work.", "output": "Same here, deadlines everywhere."},
    {"input": "Remember that trip we planned?", "output": "Oh yeah, we should make it happen soon."},
    {"input": "Definitely, maybe next month?", "output": "Works for me! Let’s set a date."},
    {"input": "Cool, I’ll check my calendar.", "output": "Awesome, can’t wait!"}
]

while True:
    user_input = input("You: ").lower()
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break
    
    # First check in Q&A dataset
    if user_input in qa_data:
        response = qa_data[user_input]
    else:
        # Try to match friendly conversation dataset
        matched = False
        for question, answer in training_data:
            if user_input in question.lower():
                response = answer
                matched = True
                break
        if not matched:
            response = "I don't understand that yet."
    
    print("Bot:", response)
