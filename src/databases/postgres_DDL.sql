DROP TABLE IF EXISTS song;

CREATE TABLE song(
    song_id BIGSERIAL NOT NULL,
    title VARCHAR(200) NOT NULL,
    artistname VARCHAR(200) NOT NULL,
    isexplicit BOOLEAN NOT NULL,
    duration INT NOT NULL
);
