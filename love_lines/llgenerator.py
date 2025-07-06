import random
# from pprint import pprint
# Define smart templates, middles, endings, and emojis
templates = [
    "You're {middle}{end}",
    "With you, I found {middle}{end}",
    "Your love is {middle}{end}",
    "Every moment with you is {middle}{end}",
    "You are {middle}{end}",
    "I never knew love until I felt {middle}{end}",
    "Being with you feels like {middle}{end}",
    "In your smile, I see {middle}{end}",
    "Every heartbeat reminds me of {middle}{end}",
    "Loving you is like finding {middle}{end}"
]

middles = [
    "the peace in my chaos", "my greatest adventure", "a dream I never want to wake up from",
    "everything I didn’t know I needed", "magic in human form", "the answer to my silent prayers",
    "home, no matter where we are", "love in its purest form", "the melody my soul sings",
    "a forever kind of feeling", "the spark in my soul", "a blessing I hold close",
    "sunshine on my darkest days", "the miracle I never expected", "what love should feel like",
    "the rhythm of my heart", "the light I've always searched for", "a poem written by the stars",
    "comfort I never thought I'd find", "a fairytale turned real"
]

endings = [
    ".", " and I love you more each day.", ", always and forever.", " — and it means the world to me.",
    ", and I’m never letting go.", ", and it feels like home.", " and I’m grateful every second.",
    ", and it changed everything.", ", and it's all I ever wanted.", ", and I can't imagine life without it."
]

emojis = ["❤️", "💘", "💖", "🫶", "💫", "🥺", "🔥", "🌹", "🌈", "🎶", "🌌", "💞", "😘"]


loveline = set()


# generator 
while len(loveline)<2000:
    template = random.choice(templates)
    middle = random.choice(middles)
    ending = random.choice(endings)
    emoji = random.choice(emojis)
    line = f"{template.format(middle=middle, end = ending)} {emoji}" 
    loveline.add(line)
lllist = list(loveline)

#function to show random love lines
def show_line():
    return random.choice(lllist)