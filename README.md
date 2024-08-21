Hands-Free Desktop Assistant
This is a Python-based voice-controlled desktop assistant that automates tasks through voice commands. The assistant performs a wide range of actions including web searches, file management, sending emails, controlling media, managing system operations, and more—all hands-free.

Features
- Web Search: Perform Google and YouTube searches directly using voice commands.
- File Management: Search and open files stored on your computer with voice commands.
- Email Sending: Send emails to specified recipients by speaking the subject and body.
- Media Control: Play music on YouTube, adjust system volume, and control media playback.
- System Operations: Open and close applications like the command prompt, manage system volume, take screenshots, and more.
- News Updates: Fetch and read out the latest news headlines.
- Reminders: Set voice-based reminders for important tasks.
- Simple Calculations: Perform basic arithmetic calculations via voice commands.

Technologies Used
- Python
- `pyttsx3`: Text-to-speech engine
- `speech_recognition`: Recognizes and processes voice commands
- `wikipedia`: Searches Wikipedia for information
- `pywhatkit`: Plays YouTube videos through voice commands
- `pyautogui`: Controls keyboard and mouse actions
- `requests`: Fetches data like IP addresses and news headlines
- `smtplib`: Sends emails using voice input
- `cv2`: For potential computer vision tasks like screenshots

Prerequisites
- Python 3.x
- Required Python Libraries (Install using pip):
  pip install pyttsx3 speechrecognition wikipedia pywhatkit pyautogui opencv-python requests smtplib pytz

Setup
1. Clone the repository:
   git clone https://github.com/YourUsername/hands-free-desktop-assistant.git
   cd hands-free-desktop-assistant

2. Install the required libraries:
   pip install -r requirements.txt

3. Set up your email credentials inside the `send_email` function (replace placeholders with your email and password):
   EMAIL_ADDRESS = "your-email@example.com"
   EMAIL_PASSWORD = "your-password"


4. Run the program:
   python assistant.py

Usage:
Once the program is running, the assistant will greet you and listen for your voice commands. You can say commands like:
- "Open YouTube and play [song name]"
- "Send an email to [recipient]"
- "Set a reminder for tomorrow at 5 PM"
- "What is the latest news?"
- "Search [topic] on Wikipedia"
- "Take a screenshot"

Simply speak to interact with the assistant, and it will carry out the tasks accordingly.

Challenges:
Building this assistant involved integrating various Python libraries to handle speech recognition, media control, file handling, and system operations efficiently. One key challenge was ensuring accurate speech recognition and seamlessly executing commands in a multi-tasking environment.

Future Enhancements:
- Natural Language Processing (NLP): Improving the assistant's ability to understand more complex sentences and questions.
- Task Scheduling: Adding the ability to schedule tasks at specific times.
- Integration with Smart Devices: Connecting the assistant with IoT devices to control smart home appliances.

Contributions:
Feel free to contribute by submitting a pull request. Any suggestions, enhancements, or bug fixes are welcome!
