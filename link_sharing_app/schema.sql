DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS link;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    image_url TEXT
);

CREATE TABLE link (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    platform TEXT NOT NULL CHECK ( platform in ('GitHub', 'Frontend_Mentor', 'Twitter', 'LinkedIn', 'YouTube', 'Facebook', 'Twitch', 'Dev.to', 'Codewars', 'Codepen', 'freeCodeCamp', 'GitLab', 'Hashnode', 'Stack_Overflow') ),
    url TEXT UNIQUE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
)
