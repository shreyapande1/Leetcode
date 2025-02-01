SELECT 
    user_id,
    COUNT(user_id) followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id,followers_count