---

## IJF Rules Implemented

| Event | Outcome |
|-------|---------|
| Ippon | Immediate victory |
| 2× Waza-ari | Ippon equivalent → immediate win |
| Hansoku-make | Opponent wins immediately |
| 3× Shido | Auto-triggers hansoku-make |
| Osae-komi 10s | Yuko awarded |
| Osae-komi 15s | Waza-ari awarded |
| Osae-komi 20s | Ippon awarded |
| Time expired (no ippon) | Waza-ari → Yuko → Shido tiebreak |

---

## AI Use Documentation

Our team used Claude (by Anthropic) and ChatGPT throughout this project. Here is an honest and specific breakdown of how AI was used and where.

### What AI Helped With

**Code Structure and Flask**
We used AI to understand how Flask routes work and how to connect the browser to the Python backend. Our ITM352 knowledge of dictionaries, functions, and data types helped us ask the right questions. We already knew we wanted a dictionary for match state management because we learned that structure in class — we used AI to figure out how to send it to the browser using jsonify.

**Bug Fixing**
This is honestly where most of our AI use happened. Debugging took way longer than building. A few specific examples:

- The minus buttons on the scoreboard were not working because negative numbers like `-1` break Flask URL routes. I found this by reading the browser console error myself and then used AI to implement the fix — switching to the words `add` and `subtract` in the URL.
- There were indentation errors in the `apply_score()` function that kept crashing the app every time we tried to run it. Python is very strict about indentation so even one wrong space breaks everything. I pasted the broken section into AI and asked it to fix the spacing while keeping my comments and logic exactly as they were.
- A missing `score = get_score(player)` line was causing a 500 error every time a score button was clicked. AI helped identify which line was missing and where it needed to go.
- The tournament bracket generator was by far the hardest part of this whole project. I spent over 5 hours trying to get it to work. The issue was a combination of the SQLite database locking when multiple connections were open at the same time, and a bug in the bye-round logic that crashed when a `None` placeholder was treated like a real player. I kept running into these errors one after another and used AI to help diagnose each one after I had already identified where in the code the problem was coming from.
- The champion banner was showing up too early — after the very first match was confirmed. I figured out it was a frontend detection issue and used AI to add the correct conditions to only show the banner when the true final match was done.

**Tournament Bracket Design**
We planned the bracket feature ourselves based on what Ethan needed as a referee — single elimination, manual winner confirmation, automatic advancement, and bye handling for odd numbers of players. AI helped implement the SQLite schema and the bracket generation math once we had the design figured out.

**Comments and Documentation**
Every comment in the code was written by one of us after reading and understanding that section. We used AI to explain things we didn't fully understand so we could write accurate comments in our own words. Each comment is labeled with which team member wrote it.

**Logo**
We used ChatGPT's image generation to make the app logo. We specified the judo theme, dark background, and gold color scheme to match the app's overall look.

### What AI Did Not Do

- The idea came from Ethan — not AI
- The feature list came from the three of us based on what a real referee actually needs
- The comments were written by us after understanding the code
- The testing was done by us running the app and breaking things ourselves
- The UI design decisions came from me (Brandon) not knowing judo and needing it to be simple enough for a non-judo person to operate under pressure

### How ITM352 Informed Our AI Use

Because we had learned Python data structures, functions, Flask, and file I/O in class, we were able to ask AI specific questions instead of vague ones. We could read AI's output and catch when it was wrong. We modified suggestions when they broke other things. We understood the code well enough to explain it and comment it ourselves. Without the ITM352 foundation we would not have been able to direct AI the way we did or evaluate whether what it gave us actually made sense.

---

## Testing

| Test | Expected Result | Result |
|------|----------------|--------|
| Click + on Ippon | Score increases to 1, match ends | ✅ Pass |
| Click + on Ippon twice | Score stays at 1 (limit enforced) | ✅ Pass |
| Click − on Yuko at 0 | Score stays at 0 (no negatives) | ✅ Pass |
| Click + on Shido 3 times | Hansoku-make triggers automatically | ✅ Pass |
| Start osae-komi, wait 10s | Yuko awarded automatically | ✅ Pass |
| Start osae-komi, wait 15s | Waza-ari awarded automatically | ✅ Pass |
| Start osae-komi, wait 20s | Ippon awarded, match ends | ✅ Pass |
| Two waza-ari scored | Match ends automatically | ✅ Pass |
| Timer reaches 0:00 | Winner declared by tiebreaker | ✅ Pass |
| Click Golden Score | Timer switches to count up | ✅ Pass |
| Click Undo | Last action removed from history | ✅ Pass |
| Click Reset Match | All scores and timers reset to zero | ✅ Pass |
| Start injury timer | Main match clock pauses automatically | ✅ Pass |
| Declare winner manually | Match ends, winner banner appears | ✅ Pass |
| Create tournament | Tournament saved to database | ✅ Pass |
| Add players | Players appear in registration list | ✅ Pass |
| Remove player | Player removed before bracket generates | ✅ Pass |
| Generate bracket with 4 players | 2 round 1 matches created | ✅ Pass |
| Generate bracket with 6 players | Bye rounds created automatically | ✅ Pass |
| Confirm match winner | Winner highlighted, next round generates | ✅ Pass |
| Complete tournament | Champion banner displayed | ✅ Pass |
| Delete tournament | Tournament and all data removed | ✅ Pass |

---

## Known Limitations

- Match state resets if the Flask server is restarted — there is no persistent scoreboard storage yet
- The app is designed for one active scoreboard match at a time
- Player deletion is only recommended before the bracket is generated
- Tournament bracket is currently single elimination only

---

*Built with Python, Flask, HTML, CSS, JavaScript, and SQLite*  
*ITM352 (Brandon) (Cassiddy)