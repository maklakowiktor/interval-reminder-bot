-- DROP TABLE IF EXISTS reminds;

CREATE TABLE IF NOT EXISTS reminds(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    raw_text TEXT NOT NULL,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated DATETIME,
    done BOOLEAN,
    repeats INTEGER
);

-- INSERT INTO reminds(raw_text, created, updated, done, repeats)
-- VALUES 
--     ("Абстракция - это процесс выделения главной идеи и скрытия деталей. В программировании абстракция позволяет создавать объекты, которые представляют только необходимую информацию и функциональность, скрывая детали реализации.", CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, false, 0);