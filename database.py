import sqlite3


def create_database():
    # This will create a new database file 'mydatabase.db' if it doesn't exist
    conn = sqlite3.connect('twitter_data_analysis.db')
    cursor = conn.cursor()

    # Create a new table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tweets (
        tweet_id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        tweet_text TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        likes_count INTEGER
    );
    """)
    conn.commit()

    # Insert example tweets
    def insert_tweet(username, tweet_text, likes_count):
        cursor.execute("""
        INSERT INTO tweets (username, tweet_text, likes_count)
        VALUES (?, ?, ?)
        """, (username, tweet_text, likes_count))
        conn.commit()

    # Inserting example data
    insert_tweet('user1', 'This is my first tweet!', 10)
    insert_tweet('user2', 'Just another day on Twitter.', 20)
    insert_tweet('user3', 'Feeling excited about the weekend!', 15)

    conn.close()


if __name__ == "__main__":
    create_database()
