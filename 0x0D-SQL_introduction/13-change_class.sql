-- Lists all genres from the database hbtn_0d_tvshows along with the number of 
-- shows linked to each
-- Does not display genres without linked shows
-- Records are ordered by descending number of showa linked
SELECTED g.`name`AS `genre`,
         COUNT(*) AS `number of shows`
  FROM `tv_genres` AS g
                INNER JOIN `tv_show_genres_` AS t
                ON G.`id` =t. `genre_id`
GROUP BY g. `name`
ORDER BY number_of _shows` DESC;
~                                                                                  
~                                   
