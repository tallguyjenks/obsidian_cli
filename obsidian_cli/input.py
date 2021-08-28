#!use/bin/env python3

"""
This script is used to create new inputs for my Zettelkasten on the fly.
"""

import datetime as dt

# ============================================================================= #
# GLOBAL VARIABLES
# ============================================================================= #

DROP_POINT_PATH = "/Users/bryanjenks/Documents/70-79_Projects/73_Obsidian_Related/004.73.01_Sterkere/Sterkere/Inbox/"

# ============================================================================= #
# FUNCTIONS
# ============================================================================= #

def get_input_type() -> tuple:
    response = input("""What Type of input is this?\n
[1]: 📚️ Book
[2]: 👤️ Person
[3]: 🐦️ Tweet
[4]: 🎧️ Podcast
[5]: 🎥️ Video
[6]: 📰️ Article
[7]: 📜️ Paper
[8]: 💭️ Thought
[9]: 🌱️ Seedling
[q]: ❌️ Exit\n\n> """)

    data = {
        "1": ("Book", "{"),
        "2": ("Person", "@"),
        "3": ("Tweet", "!"),
        "4": ("Podcast", "%"),
        "5": ("Video", "+"),
        "6": ("Article", "("),
        "7": ("Paper", "&"),
        "8": ("Thought", "="),
        "9": ("Seedling", "")
    }

    return data.get(f"{response}")

def get_file_name(symbol: str) -> str:
    file_name = symbol + " " + input("What should the name of the file be?\n\n>")
    return file_name.replace("/", "")

def get_tags() -> list:
    tags = ""
    while True:
        tag = input("Would you like to add more tags?\n\n> ")
        if tag == "":
            if tags != "":
                tags = tags[:-2]
            break
        else:
            tags += f"[[{tag}]], "
    return tags

def get_input_url(input_type: str) -> tuple:
    url = input("What is the URL of the input?\n\n>")
    is_video = input_type == "Video"
    if is_video:
        short_code = url.split("/")[3]
        return (url, short_code)
    else:
        return (url, None)

def get_channel_host() -> str:
    return input("Who is the channel host of the video?\n\n>")

def get_publish_date() -> str:
    published_today = input("""Was the video published today? [y/n]\n\n> """)
    if published_today == "y":
        return dt.datetime.today().strftime("%Y-%m-%d")

    is_current_year = input("""Was the video published this year? [y/n]\n\n> """)
    year = dt.datetime.now().year if is_current_year == "y" else "20" + input("""What year was the video published? Format: '2021 or '2005'\n\n> 20""")

    is_current_month = input("""Was the video published this month? [y/n]\n\n> """)
    month = dt.datetime.now().strftime("%m") if is_current_month == "y" else input("""What month was the video published? Format: '08' or '11'\n\n> """)

    is_current_day = input("""Was the video published this day? [y/n]\n\n> """)
    day = dt.datetime.now().day if is_current_day == "y" else input("""What day was the video published? Format: '08' or '17'\n\n> """)

    return f"{year}-{month}-{day}"

def get_reviewed_date() -> str:
    is_reviewed = input("""Has the input been reviewed already? [y/n]\n\n> """)
    if is_reviewed == "n" or is_reviewed == "":
        return ""

    reviewed_today = input("""Was the input reviewed today? [y/n]\n\n> """)
    if reviewed_today == "y":
        return dt.datetime.now().strftime("%Y-%m-%d")

    is_current_year = input("""Was the input reviewed this year? [y/n]\n\n> """)
    year = dt.datetime.now().year if is_current_year == "y" else "20" + input("""What year was the input reviewed? Format: '2021 or '1999'\n\n> 20""")

    is_current_month = input("""Was the input reviewed this month? [y/n]\n\n> """)
    month = dt.datetime.now().strftime("%m") if is_current_month == "y" else input("""What month was the input reviewed? Format: '08' or '11'\n\n> """)

    is_current_day = input("""Was the input reviewed this day? [y/n]\n\n> """)
    day = dt.datetime.now().day if is_current_day == "y" else input("""What day was the input reviewed? Format: '08' or '17'\n\n> """)

    return f"[[{year}-{month}-{day}]]"

#==============================================================================#
# MAIN FUNCTION
#==============================================================================#


def main():
    input_type = get_input_type()
    match input_type[0]:    
        case None | "q":
            print("Exiting...")
            exit()
        case "Video":
            file_name = get_file_name(input_type[1])
            file_tags = get_tags()
            url = get_input_url(input_type[0])
            youtube_shortcode = url[1]
            host = get_channel_host()
            publish_date = get_publish_date()
            reviewed_date = get_reviewed_date()
            with open('../templates/Youtube.md', 'r') as f:
                text = f.read()
                text = text.replace('{file_name}', file_name)
                text = text.replace('{file_tags}', file_tags)
                text = text.replace('{url}', url[0])
                text = text.replace('{youtube_shortcode}', youtube_shortcode)
                text = text.replace('{host}', host)
                text = text.replace('{publish_date}', publish_date)
                text = text.replace('{reviewed_date}', reviewed_date)
                print(text)
            with open(DROP_POINT_PATH + f"/{file_name}.md", "w") as file:
                file.write(f"{text}")
    # TODO add other input functions here


if __name__ == "__main__":
    main()
