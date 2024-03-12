-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT t.`title`
  FROM tv_genres` AS t
       INNER JOIN `tv_show_genres` AS s
       ON t. `id = s.`genre_id`

       INNER JOIN `tv_shows` AS g
       ON g.`id` = s.`show_id`
       WHERE g.`name` = "comedy"
ORDER BY t.'title';

