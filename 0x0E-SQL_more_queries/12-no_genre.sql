-- Lists all shows contained in hbtn_Od_tvshows without a genre linked
-- lists all rows of a table in a database that dont have a column
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
OREDER BY tv_show.title ASC, tv_show_genres.genre_id ASC;
