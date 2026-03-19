-- 1. Most successful team (most wins all time)
SELECT winner, COUNT(*) AS total_wins
FROM matches
GROUP BY winner
ORDER BY total_wins DESC
LIMIT 5;

-- 2. Top 10 run scorers all time
SELECT batsman, SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY batsman
ORDER BY total_runs DESC
LIMIT 10;

-- 3. Top 10 wicket takers (excluding run outs)
SELECT bowler, COUNT(*) AS total_wickets
FROM deliveries
WHERE dismissal_kind NOT IN ('run out', 'retired hurt', 'obstructing the field')
  AND player_dismissed IS NOT NULL
GROUP BY bowler
ORDER BY total_wickets DESC
LIMIT 10;

-- 4. Season with highest average match score
SELECT m.season, ROUND(AVG(season_runs)::numeric, 2) AS avg_match_score
FROM matches m
JOIN (
    SELECT matchid, SUM(total_runs) AS season_runs
    FROM deliveries
    GROUP BY matchid
) d ON m.matchid = d.matchid
GROUP BY m.season
ORDER BY avg_match_score DESC
LIMIT 5;

-- 5. Most Player of the Match awards
SELECT player_of_match, COUNT(*) AS awards
FROM matches
GROUP BY player_of_match
ORDER BY awards DESC
LIMIT 10;

