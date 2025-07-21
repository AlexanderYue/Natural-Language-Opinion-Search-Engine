INSERT INTO reviews (review_id, product_id, customer_id, review_title, review_written_date, customer_name, review_from_title, review_text, helpful_count, out_of_helpful_count, customer_review_rating, number_of_comments, amazon_verified_purchase, amazon_vine_program_review, review_with_metadata) VALUES
('r1', 'p1', 'c1', 'Terrible sound', '2024-01-02', 'Alice', 'NoiseX', 'The audio quality was extremely poor and static-filled.', 4, 5, '2', 1, TRUE, FALSE, ''),
('r2', 'p2', 'c2', 'Excellent Wi-Fi', '2024-02-10', 'Bob', 'SignalMaster', 'Strong and stable wifi signal even in the basement.', 12, 12, '5', 2, TRUE, FALSE, ''),
('r3', 'p3', 'c3', 'Mouse Fail', '2024-03-15', 'Carla', 'ClickZone', 'The mouse button has a clicking problem and often gets stuck.', 3, 4, '2', 0, TRUE, FALSE, ''),
('r4', 'p4', 'c4', 'GPS Map is Awesome', '2024-04-01', 'Dave', 'TrackIt', 'The GPS map is super useful and helped us navigate easily.', 9, 10, '5', 3, TRUE, FALSE, ''),
('r5', 'p5', 'c5', 'Sharp Images', '2024-05-05', 'Eva', 'CamSharp', 'Image quality is sharp and colors are vibrant.', 6, 6, '5', 0, TRUE, FALSE, ''),
('r6', 'p6', 'c6', 'Waste of money', '2024-06-01', 'Frank', 'NoiseX', 'Terrible product with poor battery life.', 0, 2, '1', 1, TRUE, FALSE, ''),
('r7', 'p7', 'c7', 'Not bad', '2024-06-12', 'Gina', 'BudgetGear', 'Audio quality was okay, not poor but not excellent.', 2, 5, '3', 1, TRUE, FALSE, ''),
('r8', 'p8', 'c8', 'Decent purchase', '2024-06-25', 'Hank', 'DailyMouse', 'The mouse buttons feel responsive and click well.', 3, 3, '4', 0, TRUE, FALSE, ''),
('r9', 'p9', 'c9', 'Mapping Genius', '2024-07-01', 'Ivy', 'NavigatorX', 'I love how useful the GPS map is during my hikes.', 5, 6, '5', 2, TRUE, TRUE, ''),
('r10', 'p10', 'c10', 'Photo quality OK', '2024-07-10', 'Jake', 'FotoBasic', 'The image quality is decent, but not very sharp.', 1, 2, '3', 0, TRUE, FALSE, '');
