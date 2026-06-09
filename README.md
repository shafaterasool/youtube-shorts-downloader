# youtube-shorts-downloader
A Python CLI tool to download all YouTube Shorts from any channel using yt-dlp. Supports parallel downloads, auto-folder organization, and cross-platform use (Windows, macOS, Linux). For authorized use only.


# 📱 YouTube Shorts Channel Downloader

A simple Python script to download all YouTube Shorts from any YouTube channel using `yt-dlp`.

---

## ⚠️ Disclaimer

This tool is intended **for authorized use only**. Only download content from channels you own or have explicit permission to download. Respect YouTube's [Terms of Service](https://www.youtube.com/t/terms) and copyright laws.

---

## ✨ Features

- 📥 Downloads all Shorts from any YouTube channel
- 📂 Automatically organizes downloads into timestamped folders
- ⚡ Supports 4 parallel downloads for faster speed
- 🔧 Auto-installs `yt-dlp` if not already present
- 🖥️ Cross-platform support: Windows, macOS, Linux
- 📁 Auto-opens the download folder after completion

---

## 🛠️ Requirements

- Python 3.7 or higher
- `yt-dlp` (auto-installed if missing)
- Internet connection

---

## 📦 Installation

**1. Clone the repository:**

```bash
git clone https://github.com/your-username/youtube-shorts-downloader.git
cd youtube-shorts-downloader
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the script:

```bash
python youtube_shorts_downloader.py
```

You will be prompted to enter:

1. **YouTube Channel URL** — e.g., `https://www.youtube.com/@channelname` or just `@channelname`
2. **Download folder** — default is `./youtube_shorts`

**Example input:**

```
📝 YouTube Channel URL (or @channelname):
> https://www.youtube.com/@examplechannel

💾 Download folder (default: ./youtube_shorts):
> [press Enter for default]
```

---

## 📁 Output Structure

```
youtube_shorts/
└── downloads_20241215_143022/
    ├── Short Title 1.mp4
    ├── Short Title 2.mp4
    └── Short Title 3.mp4
```

Each run creates a new timestamped subfolder so previous downloads are never overwritten.

---

## 🔧 How It Works

1. Appends `/shorts` to the channel URL to target only Shorts content
2. Uses `yt-dlp` with the `best` format option
3. Downloads up to 4 videos in parallel (`-N 4`)
4. Saves files as `%(title)s.%(ext)s`

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `yt-dlp` not found | Run `pip install -U yt-dlp` manually |
| Download fails | Update yt-dlp: `pip install -U yt-dlp` |
| Folder won't open | Open the folder path shown in the terminal manually |
| No Shorts found | Verify the channel has a `/shorts` tab on YouTube |

---

## 📄 License

This project is for personal and educational use only. The author is not responsible for any misuse of this tool.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📬 Contact

Feel free to open an [Issue](https://github.com/your-username/youtube-shorts-downloader/issues) for bugs or feature requests.
