CREATE TABLE users(
	user_id INT PRIMARY KEY,
	username VARCHAR(50),
	email VARCHAR(100),
	join_date DATE
);

CREATE TABLE posts(
        post_id INT PRIMARY KEY,
	context TEXT,
	created DATETIME,
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES users(user_id)

);

INSERT INTO users (user_id, username,email,join_date) VALUES(1, 'diego_m','diego@gmail.com', '2026-09-27');
INSERT INTO users (user_id, username,email,join_date) VALUES(2, 'john_d','john@gmail.com', '2026-09-26');
INSERT INTO users (user_id, username,email,join_date) VALUES(3, 'jane_d','jane@gmail.com', '2026-09-25');
INSERT INTO users (user_id, username,email,join_date) VALUES(4, 'sam_r','sam@gmail.com', '2026-09-24');
INSERT INTO users (user_id, username,email,join_date) VALUES(5, 'alex_s','alex@gmail.com', '2026-09-23');
INSERT INTO users (user_id, username,email,join_date) VALUES(6, 'matthew_m','matthew@gmail.com', '2026-09-22');
INSERT INTO users (user_id, username,email,join_date) VALUES(7, 'jack_f','jack@gmail.com', '2026-09-21');
INSERT INTO users (user_id, username,email,join_date) VALUES(8, 'jordan_p','jordan@gmail.com', '2026-09-20');
INSERT INTO users (user_id, username,email,join_date) VALUES(9, 'noah_b','noah@gmail.com', '2026-09-19');
INSERT INTO users (user_id, username,email,join_date) VALUES(10, 'liam_o','liam@gmail.com', '2026-09-18');


INSERT INTO posts (post_id, context, created, user_id) VALUES (1, 'Hello everyone, this is my first post!', '2026-09-27 10:30:00', 1);
INSERT INTO posts (post_id, context, created, user_id) VALUES (2, 'Just joined and loving it so far.', '2026-09-26 14:15:00', 2);
INSERT INTO posts (post_id, context, created, user_id) VALUES (3, 'Anyone have study tips for finals?', '2026-09-25 09:45:00', 3);
INSERT INTO posts (post_id, context, created, user_id) VALUES (4, 'Great weather today, heading out for a walk.', '2026-09-24 16:20:00', 4);
INSERT INTO posts (post_id, context, created, user_id) VALUES (5, 'Just finished a long coding session.', '2026-09-23 20:05:00', 5);
INSERT INTO posts (post_id, context, created, user_id) VALUES (6, 'Looking for a good book recommendation.', '2026-09-22 11:00:00', 6);
INSERT INTO posts (post_id, context, created, user_id) VALUES (7, 'Trying out a new recipe tonight.', '2026-09-21 18:30:00', 7);
INSERT INTO posts (post_id, context, created, user_id) VALUES (8, 'Big game this weekend, who is watching?', '2026-09-20 12:10:00', 8);
INSERT INTO posts (post_id, context, created, user_id) VALUES (9, 'Just adopted a puppy!', '2026-09-19 08:50:00', 9);
INSERT INTO posts (post_id, context, created, user_id) VALUES (10, 'Back with a second post this week.', '2026-09-28 09:00:00', 1);
