import psycopg2


def get_or_create_player(username):
    cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO UPDATE SET username=EXCLUDED.username RETURNING id", (username,))
    return cur.fetchone()[0]

def get_top_10_scores():
    cur.execute("""
        SELECT p.username, g.score
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        ORDER BY g.score DESC
        LIMIT 10
    """)
    return cur.fetchall()


def get_personal_best(username):
    cur.execute("""
        SELECT COALESCE(MAX(g.score), 0)
        FROM game_sessions g
        JOIN players p ON g.player_id = p.id
        WHERE p.username = %s
    """, (username,))
    
    return cur.fetchone()[0]

def save_or_update(player_name, score, level):
    player_id = get_or_create_player(player_name)
    
    cur.execute("SELECT id FROM game_sessions WHERE player_id=%s", (player_id,))
    session = cur.fetchone()
    
    if session:
        cur.execute(
            """
            UPDATE game_sessions 
            SET 
                score = GREATEST(score, %s), 
                level_reached = GREATEST(level_reached, %s)
            WHERE player_id = %s
            """,
            (score, level, player_id)
        )
    else:
        cur.execute(
            "INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s)",
            (player_id, score, level)
        )
    conn.commit()

conn = psycopg2.connect(
    host="localhost",
    dbname="pygame_db",
    user="postgres",
    password="4376269"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS players (
    id       SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS game_sessions (
    id            SERIAL PRIMARY KEY,
    player_id     INTEGER REFERENCES players(id),
    score         INTEGER   NOT NULL,
    level_reached INTEGER   NOT NULL,
    played_at     TIMESTAMP DEFAULT NOW()
);
""")
conn.commit()