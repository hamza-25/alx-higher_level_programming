-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN 
(SELECT tv_shows.title
FROM tv_shows
RIGHT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy')
GROUP BY tv_shows.title
ORDER BY tv_shows.title ASC;
