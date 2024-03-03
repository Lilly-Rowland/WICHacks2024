DROP TABLE IF EXISTS Response;

CREATE TABLE Response (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    year ENUM('1', '2', '3', '4+') NOT NULL,
    major VARCHAR(50),
    confidence INT CHECK (confidence >= 1 AND confidence <= 10),
    imposter ENUM('yes', 'no'),
    support ENUM('Classmates', 'Professors', 'Friends', 'Family', 'Extracurriculars', 'Other'),
    feedback VARCHAR(400)
);