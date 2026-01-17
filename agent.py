from droidrun import Agent

agent = Agent()

content = agent.get_user_input("Enter YouTube playlist or video name")
contact = agent.get_user_input("Enter WhatsApp contact name")


agent.open_app("YouTube")
agent.search(content)
agent.tap(content)

content_type = agent.detect(["Playlist", "videos", "Watch later"])

if content_type == "playlist":

    total = agent.read_number("videos")
    watched = agent.count_elements("Watched")

    progress = round((watched / total) * 100, 2)

else:   # long video one

    current = agent.read_time("current")
    total = agent.read_time("duration")

    progress = round((current / total) * 100, 2)

agent.open_app("Google Sheets")
agent.append_row([content, progress])


message = f"You have completed {progress}% of {content}"
agent.open_app("WhatsApp")
agent.send(contact, message)
