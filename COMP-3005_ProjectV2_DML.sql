-- delete from gym_equipment;
-- delete from room_booking;
-- delete from group_fitness;
-- delete from training_session;
-- delete from fitness_metrics;
-- delete from fitness_acheivements;
-- delete from fitness_goals;
-- delete from routine;
-- delete from trainer;
-- delete from member;
-- delete from adminstration_staff;


alter sequence gym_equipment_EID_seq restart with 1; 
alter sequence room_booking_RBID_seq restart with 1; 
alter sequence group_fitness_GFID_seq restart with 1; 
alter sequence member_MID_seq restart with 1; 
alter sequence trainer_TID_seq restart with 1; 
alter sequence adminstration_staff_AID_seq restart with 1; 

INSERT INTO member (name, gender, age, email, password, goal_value, free_day) 
VALUES 
('Alice', 'Female', '25', 'alice@example.com', 'pass123', 200.0, 'M'),
('Bob', 'Male', '35', 'bob@example.com', 'bobpass', 180.0, 'T'),
('Emily', 'Female', '28', 'emily@example.com', 'emilypass', 160.0, 'W'),
('Alice', 'Female', '25', 'alice@example.com', 'password123', 200.0, 'TH'),
('Bob', 'Male', '35', 'bob@example.com', 'password456', 180.0, 'F'),
('Eve', 'Female', '28', 'eve@example.com', 'password789', 0.0, 'M');

INSERT INTO trainer (name, free_day, trainingrate) 
VALUES 
('Trainer_1', 'M', 50 ),
('Trainer_2', 'W', 60),
('Trainer_3', 'F', 55);

INSERT INTO adminstration_staff (email, password) 
VALUES 
('admin1@example.com', 'adminpassword1'),
('admin2@example.com', 'adminpassword2'),
('admin3@example.com', 'adminpassword3');


INSERT INTO  group_fitness(TID, dayslot,activity,signupcount) 
VALUES 
(1, 'M', 'Cycling', 2),
(1, 'M', 'Yoga', 0),
(2, 'W', 'Zumba', 3);

INSERT INTO  room_booking (room_number, dayslot) 
VALUES 
(213, 'M'),
(154, 'W');

INSERT INTO  gym_equipment (equipment, last_day_checked,amount) 
VALUES 
('Bench', '2024-04-10', 4),
('Machine Press', '2024-04-12', 2);

