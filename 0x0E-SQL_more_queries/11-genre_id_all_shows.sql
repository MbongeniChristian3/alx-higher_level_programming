-- Lists all shows contained in the database hbtn_Od_tvshows
-- lists all rows of a table in a database
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
OREDER BY tv_show.title ASC, tv_show_genres.genre_id ASC;
