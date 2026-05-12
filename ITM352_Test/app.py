# Libraries to run the app.
# Flask runs the website, render_template loads our HTML page, jsonify sends data to the browser, request reads data sent from the browser.
# Lets us track seconds for the timers. (Brandon)
# sqlite3 is the database library built into Python — no installation needed (Brandon)
# math is used to calculate bracket sizes and bye rounds (Brandon)
from flask import Flask, render_template, jsonify, request
import time
import sqlite3
import math

# This creates the Flask app itself and everything runs through this one line.
app = Flask(__name__)

# Match State >:D (Brandon)
# This is an important part of the whole program.
# Instead of storing scores in separate variables, we use one big dictionary
# that holds everything about the current match in one place.
# This makes it easy to send the entire match status to the browser at once,
# and easy to reset everything when a new match starts. A lot easier than the other way because I kept messing up trying to figure it out (Brandon)

match_state = {
    # Each player has a name, a club, and their own score dictionary
    "player_a": {
        "name": "Blue",
        "club": "",
        "score": {
            "ippon": 0,
            "waza_ari": 0,
            "yuko": 0,
            "shido": 0,
            "hansoku_make": False  # This is a boolean because it's either on or off (Brandon)
        }
    },
    "player_b": {
        "name": "White",
        "club": "",
        "score": {
            "ippon": 0,
            "waza_ari": 0,
            "yuko": 0,
            "shido": 0,
            "hansoku_make": False
        }
    },

    # The main match timer tracks how many seconds are left,
    # whether it's currently running, and if we're in golden score mode (Ethan)
    "timer": {
        "seconds_left": 240,  # Default match length is 4 minutes (240 seconds)
        "running": False,
        "golden_score": False,
        "duration": 240
    },

    # Osae-komi is the pin hold timer. In judo, holding someone down
    # for a certain number of seconds awards points automatically (Ethan)
    "osae_komi": {"active": False, "seconds": 0, "player": None},

    # Injury timer tracks how long a player has been injured during the match
    "injury": {"active": False, "seconds": 0, "player": None},

    # Status tracks what phase the match is in
    "status": "not_started",  # not_started, active, paused, completed (Ethan)

    # Winner is None until someone wins, then it becomes "a" or "b"
    "winner": None,

    # History is a list that logs every action taken during the match
    # so the referee can see what happened and undo mistakes
    "history": []
}


# HELPER FUNCTIONS (Cassiddy)
# These are small reusable functions that do one specific thing.
# We use them inside the bigger route functions below to avoid writing the same code over and over.

def get_score(player):
    # A shortcut to grab just the score dictionary for a given player.
    # Instead of typing match_state["player_a"]["score"] every time,
    # we just call get_score("a") which is much cleaner. (Cass)
    return match_state[f"player_{player}"]["score"]


def record_action(action_type, player, description):
    # Every time something happens in the match (a point is scored, timer starts, etc.)
    # we log it here so the referee has a full history of the match.
    # We insert at position 0 so the most recent action always shows up at the top. (Cass)
    match_state["history"].insert(0, {
        "action": action_type,
        "player": player,
        "description": description,
        "time": time.strftime("%H:%M:%S")  # Records the real clock time it happened
    })


def check_winner():
    # This function checks the current scores against IJF (International Judo Federation) rules
    # to see if anyone has won the match yet.
    # It checks in order of priority — ippon first, then waza-ari, then penalties.
    # Returns "a", "b", or None if there is no winner yet. (Ethan)
    score_a = get_score("a")
    score_b = get_score("b")

    # Ippon is the highest score in judo and it ends the match immediately! (Ethan)
    if score_a["ippon"] >= 1:
        return "a"
    if score_b["ippon"] >= 1:
        return "b"

    # Two waza-ari is equal to an ippon and also ends the match (Ethan)
    if score_a["waza_ari"] >= 2:
        return "a"
    if score_b["waza_ari"] >= 2:
        return "b"

    # Hansoku-make is a disqualification the other player wins (Ethan)
    if score_a["hansoku_make"]:
        return "b"
    if score_b["hansoku_make"]:
        return "a"

    # No winner yet
    return None


def apply_score(player, field, delta):
    # This function actually changes a player's score.
    # delta is either +1 (adding a point) or -1 (removing a point if it was a mistake).
    # We use limits to make sure scores never go above the legal maximum
    # or below zero (Cass)
    score = get_score(player)

    # Hansoku-make is a special case, it just flips on or off like a switch
    if field == "hansoku_make":
        score["hansoku_make"] = not score["hansoku_make"]
        return

    # These are the maximum values allowed for each score type in judo (Cass)
    limits = {"ippon": 1, "waza_ari": 2, "yuko": 99, "shido": 3}
    if field not in limits:
        return
    current = score[field]
    score[field] = max(0, min(limits[field], current + delta))

    # 3 shido automatically triggers disqualification
    if field == "shido" and score["shido"] >= 3:
        score["hansoku_make"] = True


# ─── Tournament Helper Functions ───────────────────────────────────────────

def get_db():
    # connects to the tournament database
    # row_factory lets us access columns by name instead of index number
    # timeout gives SQLite 10 seconds to wait if the database is busy
    # this fixes the "database is locked" error we were getting (Brandon)
    conn = sqlite3.connect('tournament.db', timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def generate_bracket(tournament_id):
    # generates the first round of matches from the participant list
    # handles byes automatically for odd numbers of players
    # we use try/finally to make sure the connection always closes
    # even if something goes wrong (Brandon)
    conn = get_db()
    c = conn.cursor()

    try:
        # get all participants for this tournament
        participants = c.execute(
            'SELECT * FROM participants WHERE tournament_id = ?', (tournament_id,)
        ).fetchall()

        players = list(participants)
        num_players = len(players)

        # figure out the next power of 2 so we know how many byes we need
        # for example 6 players needs 8 slots so 2 byes are added
        next_power = 2 ** math.ceil(math.log2(num_players)) if num_players > 1 else 2
        num_byes = next_power - num_players

        # add None placeholders for bye slots
        for _ in range(num_byes):
            players.append(None)

        # create round 1 matches
        match_number = 1
        for i in range(0, len(players), 2):
            player_a = players[i]
            player_b = players[i + 1]

            is_bye = 1 if player_a is None or player_b is None else 0
            winner_id = None

            # safely find the winner for bye matches
            # only the real player (not None) gets the automatic win
            if is_bye:
                if player_a is not None:
                    winner_id = player_a['id']
                elif player_b is not None:
                    winner_id = player_b['id']

            c.execute('''
                INSERT INTO matches (tournament_id, round_number, match_number, player_a_id, player_b_id, winner_id, is_bye, confirmed)
                VALUES (?, 1, ?, ?, ?, ?, ?, ?)
            ''', (
                tournament_id,
                match_number,
                player_a['id'] if player_a is not None else None,
                player_b['id'] if player_b is not None else None,
                winner_id,
                is_bye,
                1 if is_bye else 0
            ))
            match_number += 1

        conn.commit()
    finally:
        # always close the connection even if something goes wrong
        conn.close()


def advance_winners(tournament_id, round_number):
    # checks if all matches in a round are confirmed
    # if yes it creates the next round matchups from the winners
    conn = get_db()
    c = conn.cursor()

    try:
        # get all matches for this round
        matches = c.execute(
            'SELECT * FROM matches WHERE tournament_id = ? AND round_number = ?',
            (tournament_id, round_number)
        ).fetchall()

        # check if all matches in the round are done
        all_confirmed = all(m['confirmed'] == 1 for m in matches)
        if not all_confirmed:
            return False

        # get all winners from this round
        winners = [m['winner_id'] for m in matches if m['winner_id']]

        # if only one winner left they are the tournament champion
        if len(winners) == 1:
            return True

        # create next round matches from the winners
        next_round = round_number + 1
        match_number = 1
        for i in range(0, len(winners), 2):
            player_a = winners[i]
            player_b = winners[i + 1] if i + 1 < len(winners) else None
            is_bye = 1 if player_b is None else 0
            winner_id = player_a if is_bye else None

            c.execute('''
                INSERT INTO matches (tournament_id, round_number, match_number, player_a_id, player_b_id, winner_id, is_bye, confirmed)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                tournament_id, next_round, match_number,
                player_a, player_b, winner_id, is_bye,
                1 if is_bye else 0
            ))
            match_number += 1

        conn.commit()
        return True
    finally:
        # always close the connection even if something goes wrong
        conn.close()


# ROUTES
# In Flask, a "route" is a URL that the browser can visit or send data to.
# Each route below handles one specific action on the scoreboard.
# The @app.route decorator tells Flask what URL triggers each function. (Brandon)


@app.route("/")
def index():
    # This is the main page of the app.
    # When someone visits the website, this loads the scoreboard HTML page (Brandon)
    return render_template("index.html")


@app.route("/state")
def state():
    # The browser calls this route every second to get the latest match data.
    # jsonify converts our match_state dictionary into JSON format
    # so the browser can read it and update the scoreboard display (Brandon)
    return jsonify(match_state)


@app.route("/set_players", methods=["POST"])
def set_players():
    # Called when the referee enters player names and clubs at the start of a match.
    # We read the data sent from the form and update the match state. (Ethan)
    data = request.json
    match_state["player_a"]["name"] = data.get("player_a_name", "Blue")
    match_state["player_a"]["club"] = data.get("player_a_club", "")
    match_state["player_b"]["name"] = data.get("player_b_name", "White")
    match_state["player_b"]["club"] = data.get("player_b_club", "")
    return jsonify({"success": True})


@app.route("/score/<player>/<field>/<direction>", methods=["POST"])
def score(player, field, direction):
    # This route handles any score change, adding or removing any point type.
    # We use 'add' and 'subtract' in the URL instead of 1 and -1
    # because negative numbers break the URL format. (Ethan)
    if match_state["status"] == "completed":
        return jsonify({"error": "Match is over"}), 400
    if player not in ("a", "b") or field not in ("ippon", "waza_ari", "yuko", "shido", "hansoku_make"):
        return jsonify({"error": "Invalid input"}), 400
    if direction not in ("add", "subtract"):
        return jsonify({"error": "Invalid direction"}), 400

    # convert the word into a number so apply_score can use it
    delta = 1 if direction == "add" else -1

    apply_score(player, field, delta)
    record_action(
        f"{'+' if delta > 0 else '-'}{field}",
        player,
        f"{match_state[f'player_{player}']['name']}: {field}"
    )

    # After every score change we check if someone has won (Brandon)
    winner = check_winner()
    if winner:
        match_state["status"] = "completed"
        match_state["winner"] = winner

    return jsonify(match_state)


@app.route("/timer/toggle", methods=["POST"])
def timer_toggle():
    # This starts or pauses the match timer depending on the current status.
    # The first time it's called it moves from "not_started" to "active".
    # After that it toggles between "active" and "paused". (Cass)
    if match_state["status"] == "completed":
        return jsonify({"error": "Match is over"}), 400
    if match_state["status"] == "not_started":
        match_state["status"] = "active"
    elif match_state["status"] == "active":
        match_state["status"] = "paused"
    elif match_state["status"] == "paused":
        match_state["status"] = "active"
    match_state["timer"]["running"] = match_state["status"] == "active"
    return jsonify(match_state)


@app.route("/timer/tick", methods=["POST"])
def timer_tick():
    # The browser calls this every second to advance the timer by one second.
    # In regular mode the timer counts down. In golden score it counts up.
    # When the timer hits zero we determine the winner based on current scores. (Ethan)
    if match_state["status"] != "active":
        return jsonify(match_state)

    timer = match_state["timer"]

    if timer["golden_score"]:
        # Golden score is sudden death overtime — timer counts up instead of down
        timer["seconds_left"] += 1
    else:
        if timer["seconds_left"] > 0:
            timer["seconds_left"] -= 1

        if timer["seconds_left"] == 0:
            # Time ran out — figure out winner using IJF tiebreaker rules:
            # compare waza-ari first, then yuko, then whoever has fewer shido (Ethan)
            score_a = get_score("a")
            score_b = get_score("b")
            winner = None

            if score_a["waza_ari"] > score_b["waza_ari"]:
                winner = "a"
            elif score_b["waza_ari"] > score_a["waza_ari"]:
                winner = "b"
            elif score_a["yuko"] > score_b["yuko"]:
                winner = "a"
            elif score_b["yuko"] > score_a["yuko"]:
                winner = "b"
            elif score_a["shido"] < score_b["shido"]:
                winner = "a"
            elif score_b["shido"] < score_a["shido"]:
                winner = "b"

            if winner:
                match_state["status"] = "completed"
                match_state["winner"] = winner
                match_state["timer"]["running"] = False

    return jsonify(match_state)


@app.route("/timer/reset", methods=["POST"])
def timer_reset():
    # Resets the timer back to the full match duration without changing scores. (Brandon)
    # Useful if the referee accidentally starts the timer too early.
    match_state["timer"]["seconds_left"] = match_state["timer"].get("duration", 240)
    match_state["timer"]["running"] = False
    match_state["status"] = "paused"
    return jsonify(match_state)


@app.route("/timer/set_duration", methods=["POST"])
def set_duration():
    # Lets the referee choose how long the match will be before it starts. (Ethan)
    # Options are typically 2, 3, 4, or 5 minutes depending on the competition.
    data = request.json
    duration = int(data.get("duration", 240))
    match_state["timer"]["duration"] = duration
    match_state["timer"]["seconds_left"] = duration
    return jsonify({"success": True})


@app.route("/golden_score", methods=["POST"])
def golden_score():
    # Switches the match into golden score mode (sudden death overtime) - Ethan.
    # This happens when regulation time ends with no winner.
    # The timer resets to 0 and starts counting up until someone scores.
    match_state["timer"]["golden_score"] = True
    match_state["timer"]["seconds_left"] = 0
    match_state["status"] = "paused"
    record_action("golden_score", None, "Golden Score started")
    return jsonify(match_state)


@app.route("/osae_komi/start/<player>", methods=["POST"])
def osae_komi_start(player):
    # Starts the pin hold timer for the specified player.
    # Osae-komi is when one judoka pins the other to the ground. (Ethan)
    # The longer they hold the pin, the more points they earn.
    if player not in ("a", "b"):
        return jsonify({"error": "Invalid player"}), 400
    match_state["osae_komi"] = {"active": True, "seconds": 0, "player": player}
    return jsonify(match_state)


@app.route("/osae_komi/tick", methods=["POST"])
def osae_komi_tick():
    # Called every second while the pin is active.
    # At 10 seconds: awards a yuko
    # At 15 seconds: awards a waza-ari
    # At 20 seconds: awards an ippon and stops the timer (match over) (Ethan)
    # These thresholds are defined by IJF rules.
    ok = match_state["osae_komi"]
    if not ok["active"]:
        return jsonify(match_state)

    ok["seconds"] += 1
    player = ok["player"]

    if ok["seconds"] == 10:
        apply_score(player, "yuko", 1)
        record_action("+yuko", player, "Osae-komi 10s: yuko awarded")
    elif ok["seconds"] == 15:
        apply_score(player, "waza_ari", 1)
        record_action("+waza_ari", player, "Osae-komi 15s: waza-ari awarded")
    elif ok["seconds"] >= 20:
        apply_score(player, "ippon", 1)
        record_action("+ippon", player, "Osae-komi 20s: ippon awarded")
        ok["active"] = False  # Pin timer stops automatically at ippon

    # Check if the new score ended the match (Brandon)
    winner = check_winner()
    if winner:
        match_state["status"] = "completed"
        match_state["winner"] = winner

    return jsonify(match_state)


@app.route("/osae_komi/stop", methods=["POST"])
def osae_komi_stop():
    # Stops the pin timer if the hold is broken before reaching a threshold. (Cass)
    match_state["osae_komi"]["active"] = False
    return jsonify(match_state)


@app.route("/osae_komi/reset", methods=["POST"])
def osae_komi_reset():
    # Fully resets the pin timer back to zero. (Cass)
    match_state["osae_komi"] = {"active": False, "seconds": 0, "player": None}
    return jsonify(match_state)


@app.route("/injury/start/<player>", methods=["POST"])
def injury_start(player):
    # Starts the injury timer for a player.
    # We also pause the main match timer automatically (Cass)
    # because the match clock stops during an injury break.
    if player not in ("a", "b"):
        return jsonify({"error": "Invalid player"}), 400
    match_state["injury"] = {"active": True, "seconds": 0, "player": player}
    if match_state["status"] == "active":
        match_state["status"] = "paused"
        match_state["timer"]["running"] = False
    return jsonify(match_state)


@app.route("/injury/tick", methods=["POST"])
def injury_tick():
    # Advances the injury timer by one second. (Ethan)
    # The max allowed injury time per IJF rules is 5 minutes (300 seconds).
    if match_state["injury"]["active"]:
        match_state["injury"]["seconds"] += 1
    return jsonify(match_state)


@app.route("/injury/stop", methods=["POST"])
def injury_stop():
    # Stops the injury timer when the player is ready to continue. (Brandon)
    match_state["injury"]["active"] = False
    return jsonify(match_state)


@app.route("/injury/reset", methods=["POST"])
def injury_reset():
    # Resets the injury timer completely back to zero. (Brandon)
    match_state["injury"] = {"active": False, "seconds": 0, "player": None}
    return jsonify(match_state)


@app.route("/declare_winner/<player>", methods=["POST"])
def declare_winner(player):
    # Lets the referee manually declare a winner without waiting for time to expire.
    # This is used in situations like a player withdrawing from injury. (Cassiddy)
    if player not in ("a", "b"):
        return jsonify({"error": "Invalid player"}), 400
    match_state["status"] = "completed"
    match_state["winner"] = player
    match_state["timer"]["running"] = False
    record_action("winner_declared", player, f"{match_state[f'player_{player}']['name']} declared winner")
    return jsonify(match_state)


@app.route("/reset", methods=["POST"])
def reset_match():
    # Completely resets the entire match back to zero for a fresh start. (Cass)
    # We save the duration setting so the referee doesn't have to re-enter it.
    global match_state
    duration = match_state["timer"].get("duration", 240)
    match_state = {
        "player_a": {"name": "Blue", "club": "", "score": {"ippon": 0, "waza_ari": 0, "yuko": 0, "shido": 0, "hansoku_make": False}},
        "player_b": {"name": "White", "club": "", "score": {"ippon": 0, "waza_ari": 0, "yuko": 0, "shido": 0, "hansoku_make": False}},
        "timer": {"seconds_left": duration, "running": False, "golden_score": False, "duration": duration},
        "osae_komi": {"active": False, "seconds": 0, "player": None},
        "injury": {"active": False, "seconds": 0, "player": None},
        "status": "not_started",
        "winner": None,
        "history": []
    }
    return jsonify(match_state)


@app.route("/undo", methods=["POST"])
def undo():
    # Removes the most recent action from the history log.
    # Useful if the referee accidentally adds the wrong score. (Brandon)
    if match_state["history"]:
        match_state["history"].pop(0)
    return jsonify(match_state)


# ─── Tournament Routes ──────────────────────────────────────────────────────
# These routes handle everything related to the tournament bracket system
# They use SQLite to store tournament data permanently (Brandon)

@app.route("/tournament")
def tournament():
    # loads the tournament bracket page
    return render_template("tournament.html")


@app.route("/tournament/create", methods=["POST"])
def create_tournament():
    # creates a new tournament with a name
    data = request.json
    name = data.get("name", "My Tournament")
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO tournaments (name) VALUES (?)", (name,))
    tournament_id = c.lastrowid
    conn.commit()
    conn.close()
    return jsonify({"success": True, "tournament_id": tournament_id})


@app.route("/tournament/<int:tournament_id>/register", methods=["POST"])
def register_player(tournament_id):
    # adds a player to the tournament
    data = request.json
    name = data.get("name", "")
    club = data.get("club", "")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "INSERT INTO participants (tournament_id, name, club) VALUES (?, ?, ?)",
        (tournament_id, name, club)
    )
    conn.commit()
    conn.close()
    return jsonify({"success": True})


@app.route("/tournament/<int:tournament_id>/start", methods=["POST"])
def start_tournament(tournament_id):
    # generates the bracket from all registered players
    # needs at least 2 players to start
    # we count and close the connection before calling generate_bracket
    # so we never have two connections open at the same time (Brandon)
    conn = get_db()
    c = conn.cursor()
    count = c.execute(
        "SELECT COUNT(*) FROM participants WHERE tournament_id = ?",
        (tournament_id,)
    ).fetchone()[0]
    conn.close()

    if count < 2:
        return jsonify({"error": "Need at least 2 players"}), 400

    try:
        generate_bracket(tournament_id)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/tournament/<int:tournament_id>/bracket")
def get_bracket(tournament_id):
    # returns the full bracket data so the page can display it
    conn = get_db()
    c = conn.cursor()

    matches = c.execute('''
        SELECT m.*,
            pa.name as player_a_name, pa.club as player_a_club,
            pb.name as player_b_name, pb.club as player_b_club,
            w.name as winner_name
        FROM matches m
        LEFT JOIN participants pa ON m.player_a_id = pa.id
        LEFT JOIN participants pb ON m.player_b_id = pb.id
        LEFT JOIN participants w ON m.winner_id = w.id
        WHERE m.tournament_id = ?
        ORDER BY m.round_number, m.match_number
    ''', (tournament_id,)).fetchall()

    participants = c.execute(
        "SELECT * FROM participants WHERE tournament_id = ?",
        (tournament_id,)
    ).fetchall()

    conn.close()

    return jsonify({
        "matches": [dict(m) for m in matches],
        "participants": [dict(p) for p in participants]
    })


@app.route("/tournament/match/<int:match_id>/confirm", methods=["POST"])
def confirm_winner(match_id):
    # referee manually confirms the winner of a match
    # then checks if the whole round is done and advances winners if so
    data = request.json
    winner_id = data.get("winner_id")
    if not winner_id:
        return jsonify({"error": "Winner ID required"}), 400

    conn = get_db()
    c = conn.cursor()

    c.execute(
        "UPDATE matches SET winner_id = ?, confirmed = 1 WHERE id = ?",
        (winner_id, match_id)
    )

    # get the tournament and round for this match so we can advance winners
    match = c.execute(
        "SELECT * FROM matches WHERE id = ?", (match_id,)
    ).fetchone()

    conn.commit()
    conn.close()

    # try to advance winners to the next round
    advance_winners(match['tournament_id'], match['round_number'])

    return jsonify({"success": True})


@app.route("/tournament/list")
def list_tournaments():
    # returns all tournaments so the user can pick one to view
    conn = get_db()
    c = conn.cursor()
    tournaments = c.execute(
        "SELECT * FROM tournaments ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return jsonify({"tournaments": [dict(t) for t in tournaments]})


@app.route("/tournament/<int:tournament_id>/delete", methods=["POST"])
def delete_tournament(tournament_id):
    # deletes a tournament and all its players and matches from the database
    # we delete matches and participants first before deleting the tournament itself
    conn = get_db()
    c = conn.cursor()
    c.execute("DELETE FROM matches WHERE tournament_id = ?", (tournament_id,))
    c.execute("DELETE FROM participants WHERE tournament_id = ?", (tournament_id,))
    c.execute("DELETE FROM tournaments WHERE id = ?", (tournament_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True})


@app.route("/tournament/player/<int:player_id>/delete", methods=["POST"])
def delete_player(player_id):
    # removes a single player from the tournament
    # only works cleanly before the bracket is generated
    conn = get_db()
    c = conn.cursor()
    c.execute("DELETE FROM participants WHERE id = ?", (player_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True})


# ────────────────────────────────────────────────────────────────────────────
# RUN THE APP
# This starts the Flask development server when you run the file directly.
# debug=True means the server will automatically restart when you save changes, (Ethan)
# which is helpful while you are still building and testing the app (Brandon).
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)