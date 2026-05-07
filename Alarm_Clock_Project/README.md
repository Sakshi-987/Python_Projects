# ⏰ Alarm Clock using Python & Pygame

A simple yet functional command-line based Alarm Clock application built using Python and the Pygame library. This project allows users to set a custom countdown timer in minutes and seconds, after which an alarm sound is played automatically.

The project was developed to strengthen understanding of:
- Python fundamentals
- Functions and loops
- Real-time countdown logic
- Time handling
- Audio playback using Pygame
- File path management
- Terminal-based UI updates

---

# 🚀 Features

- ⏳ Real-time countdown timer
- 🔊 Alarm sound playback using Pygame
- 🕒 Displays timer in MM:SS format
- 🔁 Live updating timer on the same terminal line
- ⚡ Lightweight and beginner-friendly project
- 🧠 Built using core Python concepts

---

# 🛠️ Technologies Used

- Python 3
- Pygame
- Time Module
- OS Module

---

# 📚 Concepts Used

This project demonstrates practical implementation of:

- Functions
- Loops (`for loop`)
- `range()` function
- `divmod()` for time conversion
- String formatting using f-strings
- Escape characters (`\r`)
- Real-time execution using `time.sleep()`
- Audio playback using `pygame.mixer`

---

# 📂 Project Structure

```bash
Alarm_Clock_Project/
│
├── alarm_clock.py
├── alarm.mp3
└── README.md
```

---

# ⚙️ How It Works

1. User enters minutes and seconds.
2. Total time is converted into seconds.
3. A countdown loop starts running.
4. Timer updates every second in real time.
5. Once the timer reaches `00:00`, the alarm sound is triggered.
6. Program continues running until the audio playback finishes.

---

# 🔍 Core Logic

## Countdown Loop

```python
for time_left in range(seconds, 0, -1):
```

- Starts countdown from total seconds
- Decreases by 1 after every iteration
- Stops automatically when timer reaches 0

---

## Time Conversion

```python
mins, secs = divmod(time_left, 60)
```

Converts total seconds into:
- Minutes
- Remaining seconds

Example:

```python
125 seconds → 2 minutes 5 seconds
```

---

## Real-Time Countdown

```python
time.sleep(1)
```

Pauses program execution for 1 second after every loop iteration, creating a real-time countdown effect.

---

## Same Line Timer Update

```python
print(..., end="")
```

and

```python
\r
```

are used to continuously update the timer on the same terminal line instead of printing multiple new lines repeatedly.

---

## Audio Playback

```python
pygame.mixer.music.load(sound_file)
pygame.mixer.music.play()
```

Used to:
- Load the alarm audio file
- Play sound automatically when countdown ends


# 💻 Sample Output

```bash
Enter minutes: 0
Enter seconds: 10

Alarm in: 00:09
Alarm in: 00:08
Alarm in: 00:07
...
Time's up!
```

(Alarm sound starts playing)



# ⚠️ Challenges Faced

During development, some challenges encountered were:

- Managing correct audio file paths
- Understanding working directory vs file directory
- Implementing real-time countdown behavior
- Updating timer dynamically on same console line
- Handling audio playback using Pygame mixer

---

# 🚀 Future Improvements

Planned upgrades for future versions:

- 🖥️ GUI Alarm Clock using Tkinter
- ⏸️ Pause / Resume functionality
- 🔁 Snooze feature
- 🔊 Volume control
- ⏰ Multiple alarms support
- 🌙 Dark mode interface
- 📱 Desktop notifications

---

# 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

- Python fundamentals
- Real-time program execution
- Multimedia handling using Pygame
- Modular programming
- Debugging and problem-solving
- File path management
- Building beginner-level real-world applications

---

# 📌 Author

Sakshi Sahu  
B.Tech CSE Student | Java(DSA) & Python | Full Stack Development | Learning SpringBoot & System Design