# Voice Buddy

A Python-based Voice Assistant with GUI interface that can perform various tasks through voice commands.

## Features

- Voice-controlled interface with GUI
- Can open various websites (Google, YouTube, Facebook, etc.)
- Tells current time
- Responds to basic queries
- Ambient noise adjustment for better voice recognition
- User-friendly interface with start/stop controls

## Requirements

- Python 3.x
- Required packages:
  - speech_recognition
  - pyttsx3
  - Pillow (PIL)
  - pyaudio

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sanikatandale14/Voice-Buddy.git
```

2. Install required packages:
```bash
pip install speech_recognition pyttsx3 pillow pyaudio
```

3. Run the application:
```bash
python PythonGeeks.py
```

## Usage

1. Click the START button to begin
2. Wait for "Ready! Say Something..." message
3. Speak your command clearly. Available commands:
   - "Open Google"
   - "Open YouTube"
   - "Open Facebook"
   - "Open Gmail"
   - "Open Stack Overflow"
   - "Current time"
   - "Who are you"
   - "What can you do for me"
   - "Shutdown" (to close the assistant)

## Project Structure

```
Voice-Buddy/
├── PythonGeeks.py    # Main application file
├── images/
│   ├── background.png
│   └── frame_image.jpg
└── README.md
```

## Contributing

Feel free to open issues or submit pull requests to improve the project.

## License

This project is open source and available under the [MIT License](LICENSE).