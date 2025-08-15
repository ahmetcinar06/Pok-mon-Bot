# Nexo Discord Bot

Nexo is a multi-purpose Discord bot built with **discord.py** and **OpenAI's API**.  
It includes AI chat functionality, moderation tools, server utilities, PC management commands, and fun extras.

---

## 📌 Features

- **AI Chat Mode** (powered by OpenAI GPT-4.1-mini)
- **Moderation** (ban users for advertising/links)
- **Message Filtering** (detects links and bans advertisers)
- **Image Detection** (recognizes when a user sends an image)
- **Server Utilities** (info, roles, member list, invite links)
- **PC Management** (system info, status, antivirus scan, processes, updates)
- **Fun Commands** (games, random numbers)
- **Uptime Tracking**
- **Custom Help Command**

---

## ⚙️ Requirements

Make sure you have:

- Python 3.9+ installed  
- `discord.py` library (`pip install discord.py`)
- `openai` library (`pip install openai`)
- Other optional dependencies for PC management functions

---

## 📥 Installation

1. **Clone this repository** or download the source code.

2. **Install dependencies:**
   ```bash
   pip install discord.py openai


Configure your bot token and API key:

Create a file named config.py

Add:

token = "YOUR_DISCORD_BOT_TOKEN"
In main.py, replace 'Your-OpenAI-API-Key' with your actual OpenAI API key.

Run the bot:

python main.py
💬 Commands
🤖 AI Commands
Command	Description
nexo AI	Enables AI mode (responds without prefix).
nexo çık	Disables AI mode.
nexo AIVersion	Shows the AI model version.

⚒ Moderation & Utilities
Command	Description
(Automatic)	Bans users sending links/ads.
nexo temizle [n]	Deletes the last n messages (default: 5).
nexo aktif	Lists online members.
nexo roller	Lists all server roles.
nexo davet	Creates a temporary invite link.
nexo uptime	Shows how long the bot has been running.

💻 PC Management
Command	Description
nexo pc_about	Shows PC hardware information.
nexo pc_status	Shows system resource usage.
nexo antivirus	Runs antivirus scan.
nexo update	Checks for system updates.
nexo processes	Lists running processes.
nexo oyun	Plays a number guessing game.

🎯 General & Fun
Command	Description
nexo ping	Shows bot latency.
nexo avatar [user]	Displays the avatar of the mentioned user.
nexo kullanici	Shows your username and ID.
nexo sunucu	Shows server name and member count.
nexo sunucuinfo	Shows server creation date and region.
nexo rastgele	Sends the sum of two random numbers.
nexo about	Shows bot description.
nexo info	Shows bot info.
nexo hello	Sends a greeting message.
nexo help	Lists all commands.
nexo dm <message>	Sends you a DM with the provided message.

🚀 AI Mode
When AI mode is enabled (nexo AI), the bot will:

Respond to all your messages without needing the nexo prefix.

Use OpenAI's GPT-4.1-mini to generate responses.

Can be disabled with nexo çık.