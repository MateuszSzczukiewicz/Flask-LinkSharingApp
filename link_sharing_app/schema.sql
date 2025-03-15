DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS links;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    image_url TEXT
);

CREATE TABLE links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    platform TEXT NOT NULL CHECK ( platform in ('GitHub', 'Frontend_Mentor', 'Twitter', 'LinkedIn', 'YouTube', 'Facebook', 'Twitch', 'Dev.to', 'Codewars', 'Codepen', 'freeCodeCamp', 'GitLab', 'Hashnode', 'Stack_Overflow') ),
    url TEXT UNIQUE NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
)
