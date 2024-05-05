from domain.new import News, PoliticalEnum, VerbosityEnum
from domain.playlist import Playlist
from domain.user import User


def fill_users_array():
    user_mockup = [User(
        username="john_doe",
        email="john@example.com",
        full_name="John Doe",
        playlist=[
            Playlist(
                name="My Favorites",
                likes=100,
                news_list=[
                    News(
                        name="Breaking News",
                        author="Reporter X",
                        verbosity=VerbosityEnum.CONCISE,
                        languages=["English"],
                        political_orientation=PoliticalEnum.NEUTRAL
                    ),
                    News(
                        name="In-depth Analysis",
                        author="Analyst Y",
                        verbosity=VerbosityEnum.IN_DEPTH,
                        languages=["English", "Spanish"],
                        political_orientation=PoliticalEnum.LIBERAL
                    )
                ]
            )
        ]
    ),
        User(
        username="alice_smith",
        email="alice@example.com",
        full_name="Alice Smith",
        playlist=[
            Playlist(
                name="Weekend Vibes",
                likes=75,
                news_list=[
                    News(
                        name="Entertainment Update",
                        author="Entertainment Reporter",
                        verbosity=VerbosityEnum.CONCISE,
                        languages=["English"],
                        political_orientation=PoliticalEnum.NEUTRAL
                    ),
                    News(
                        name="Music Trends",
                        author="Music Critic",
                        verbosity=VerbosityEnum.IN_DEPTH,
                        languages=["English"],
                        political_orientation=PoliticalEnum.NEUTRAL
                    )
                ]
            )
        ]
    ),
        User(
        username="sam_jones",
        email="sam@example.com",
        full_name="Sam Jones",
        playlist=[
            Playlist(
                name="Tech News",
                likes=120,
                news_list=[
                    News(
                        name="Latest Gadgets",
                        author="Tech Enthusiast",
                        verbosity=VerbosityEnum.IN_DEPTH,
                        languages=["English", "French"],
                        political_orientation=PoliticalEnum.NEUTRAL
                    ),
                    News(
                        name="Cybersecurity Updates",
                        author="Security Expert",
                        verbosity=VerbosityEnum.CONCISE,
                        languages=["English", "Spanish"],
                        political_orientation=PoliticalEnum.NEUTRAL
                    )
                ]
            )
        ]
    ),
        User(
        username="lisa_brown",
        email="lisa@example.com",
        full_name="Lisa Brown",
        playlist=[
            Playlist(
                name="World News",
                likes=90,
                news_list=[
                    News(
                        name="Global Politics",
                        author="Political Analyst",
                        verbosity=VerbosityEnum.IN_DEPTH,
                        languages=["English", "Arabic"],
                        political_orientation=PoliticalEnum.NEUTRAL
                    ),
                    News(
                        name="Environmental Issues",
                        author="Environmental Reporter",
                        verbosity=VerbosityEnum.CONCISE,
                        languages=["English", "Chinese"],
                        political_orientation=PoliticalEnum.LIBERAL
                    )
                ]
            )
        ]
    ),
        User(
        username="mike_williams",
        email="mike@example.com",
        full_name="Mike Williams",
        playlist=[
            Playlist(
                name="Sports Highlights",
                likes=150,
                news_list=[
                    News(
                        name="Football Analysis",
                        author="Sports Analyst",
                        verbosity=VerbosityEnum.IN_DEPTH,
                        languages=["English"],
                        political_orientation=PoliticalEnum.NEUTRAL
                    ),
                    News(
                        name="Basketball Updates",
                        author="Sports Reporter",
                        verbosity=VerbosityEnum.CONCISE,
                        languages=["English", "Spanish"],
                        political_orientation=PoliticalEnum.NEUTRAL
                    )
                ]
            )
        ]
    )
    ]
    return user_mockup
