-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_genres.name
FROM tv_genres
WHERE name NOT IN 
(SELECT tv_genres.name
FROM tv_show_genres
RIGHT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter')
GROUP BY tv_genres.name
ORDER BY tv_genres.name ASC;
