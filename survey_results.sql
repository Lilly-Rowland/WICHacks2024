

DROP TABLE IF EXISTS Response;

CREATE TABLE Response (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    year TEXT CHECK (year IN ('1', '2', '3', '4+')) NOT NULL,
    major VARCHAR(50) NOT NULL,
    confidence INT CHECK (confidence >= 1 AND confidence <= 10),
    imposter TEXT CHECK (imposter IN ('yes', 'no')),
    support TEXT CHECK (support IN ('Classmates', 'Professors', 'Friends', 'Family', 'Extracurriculars', 'Other')),
    feedback VARCHAR(400)
);
