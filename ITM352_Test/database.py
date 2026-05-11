import sqlite3

# this function creates the database and all the tables we need
# it runs once when you first set up the bracket system
def init_db():
    conn = sqlite3.connect('tournament.db')
    c = conn.cursor()

    # stores the tournament itself
    c.execute('''
        CREATE TABLE IF NOT EXISTS tournaments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # stores each participant registered for the tournament
    c.execute('''
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tournament_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            club TEXT,
            FOREIGN KEY (tournament_id) REFERENCES tournaments(id)
        )
    ''')

    # stores each match in the bracket
    # bye means a player gets a free pass to the next round
    c.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tournament_id INTEGER NOT NULL,
            round_number INTEGER NOT NULL,
            match_number INTEGER NOT NULL,
            player_a_id INTEGER,
            player_b_id INTEGER,
            winner_id INTEGER,
            is_bye INTEGER DEFAULT 0,
            confirmed INTEGER DEFAULT 0,
            FOREIGN KEY (tournament_id) REFERENCES tournaments(id),
            FOREIGN KEY (player_a_id) REFERENCES participants(id),
            FOREIGN KEY (player_b_id) REFERENCES participants(id),
            FOREIGN KEY (winner_id) REFERENCES participants(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database created successfully!")

# run this file directly to set up the database
if __name__ == "__main__":
    init_db()