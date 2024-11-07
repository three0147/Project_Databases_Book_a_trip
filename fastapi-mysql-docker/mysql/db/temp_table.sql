-- CREATE TABLE `product` (
--   `id` int NOT NULL AUTO_INCREMENT,
--   `product_name` varchar(256) NOT NULL,
--   `description` varchar(256) NOT NULL,
--   `price` float,
--   PRIMARY KEY (`id`)
-- );

create table `Customer`(
	`Customer_id` varchar(5) not null,
  `Customer_name` varchar(20) not null,
	`Phonenumber` varchar(12) not null,
	`Email` varchar(20) not null,
	primary key(`Customer_id`)
);


create table `Guide`(
	`Guide_id` varchar(3) not null,
	`Email` varchar(20) not null,
	`Languages` varchar(20) not null,
	primary key(`Guide_id`)
);


create table `Company`(
	`Company_Name` varchar(15) not null,
	`Total` int(6) not null
);


create table `ProgramTour`(
	`location_id` varchar(2) not null,
	`location_Name` varchar(30) not null,
	primary key(`location_id`)
);



create table `Reservation` (
	`Booking_id` varchar(4),
  	`Firstdate` varchar(10) not null,
  	`Lastdate` varchar(10) not null,
  primary key (`Booking_id`),
);
