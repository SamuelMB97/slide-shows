from app import SlideShow

TEST_DATA = [
    {"file_name": r"pics\Thumbs Up Music.jpg",
     "caption": "Thumbs Up and Headphones",
     "credit": "No Idea",
     "alt": "Never gonna give you up",
     "keywords": ["thumb", "headphones"]},
    {"file_name": r"pics\Smile to the Music.png",
     "caption": "'Of course I am, convince me otherwise will take all night!'",
     "credit": "You got me",
     "alt": "Nvm",
     "keywords": None},
    {"file_name": r"pics\man-enjoying-music-2214037.jpg",
     "caption": "I'm Lovin' It",
     "credit": "McDonalds",
     "alt": None,
     "keywords": ["Hungry"]},
    {"file_name": r"pics\grizzlyBear.jpg",
     "caption": "Chongus",
     "credit": "IDK",
     "alt": None,
     "keywords": ["You", "Think", "You're", "Hungry"]}
]

app = SlideShow("Test Album", TEST_DATA)
app.run_app()