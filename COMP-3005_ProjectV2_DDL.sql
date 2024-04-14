-- drop table gym_equipment;
-- drop table room_booking;
-- drop table adminstration_staff;
-- drop table group_fitness;
-- drop table training_session;
-- drop table trainer;
-- drop table routine;
-- drop table fitness_metrics;
-- drop table fitness_goals;
-- drop table fitness_acheivements;
-- drop table member;



create table member
	(
        MID SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        gender VARCHAR(255) NOT NULL,
        age  VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        password  VARCHAR(255) NOT NULL,
        goal_value FLOAT,
        free_day VARCHAR(255)
	);

create table fitness_metrics
	(
        FMID SERIAL PRIMARY KEY,
        MID SERIAL,
        date DATE,
        weight FLOAT,
        BFP FLOAT,
        FOREIGN KEY(MID)
            REFERENCES member(MID)
	);

create table fitness_goals
    (
        FGID SERIAL PRIMARY KEY,
        MID SERIAL,
        goal VARCHAR(255),
        time DATE,
        FOREIGN KEY(MID)
            REFERENCES member(MID)
    );

create table fitness_acheivements
    (
        FAID SERIAL PRIMARY KEY,
        MID SERIAL,
        acheivement VARCHAR(255),
        time DATE,
        FOREIGN KEY(MID)
            REFERENCES member(MID)
    );

create table routine
	(
        RID SERIAL PRIMARY KEY,
        MID SERIAL,
        exercise_name VARCHAR(255),
        duration TIME,
        FOREIGN KEY(MID)
            REFERENCES member(MID)
	);

create table trainer
    (
        TID SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        free_day VARCHAR(255) NOT NULL,
        trainingrate INT NOT NULL
    );

create table training_session
    (
        TSID SERIAL PRIMARY KEY,
        MID SERIAL,
        TID SERIAL,
        scheduled_time TIMESTAMP NOT NULL,
        FOREIGN KEY(MID)
            REFERENCES member(MID),
        FOREIGN KEY(TID)
            REFERENCES trainer(TID)
    );

create table group_fitness
    (
        GFID SERIAL PRIMARY KEY,
        TID SERIAL,
        dayslot VARCHAR(255) NOT NULL,
        activity VARCHAR(255) NOT NULL,
        signupcount INT,
        FOREIGN KEY(TID)
            REFERENCES trainer(TID)
    );

create table adminstration_staff
    (
        AID SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        password  VARCHAR(255) NOT NULL
    );

create table room_booking
    (
        RBID SERIAL PRIMARY KEY,
        room_number INT,
        dayslot VARCHAR(255)
    );

create table gym_equipment
    (
        EID SERIAL PRIMARY KEY,
        equipment VARCHAR(255) NOT NULL,
        last_day_checked DATE,
        amount INT 
    );