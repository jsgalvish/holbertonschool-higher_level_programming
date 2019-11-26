-- select shows in hbtn_0d_tvshows that have one genre
-- create database
-- select all shows with genre
  CREATE DATABASE IF NOT EXISTS hbtn_0d_tvshows;
  SELECT tv_shows.title, tv_show_genres.genre_id
    FROM tv_shows
    JOIN tv_show_genres
      ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id;
