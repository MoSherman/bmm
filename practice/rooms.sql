#create database bmm;
use bmm;

create table rooms
(
roomid mediumint auto_increment primary key,
room_number mediumint not null,
room_name varchar(255)
);

create table objects_in_rooms
(
objectid mediumint auto_increment primary key,
object_name varchar(255),
object_description text,
roomid mediumint not null,
foreign key (roomid) references rooms(roomid)
);

create table room_map
(
id mediumint auto_increment primary key,
room_you_are_in_id mediumint not null,#room number 3
room_next_door mediumint not null,#room number 7
directions varchar(255),#turn left
foreign key (room_you_are_in_id) references rooms(roomid),
foreign key (room_next_door) references rooms(roomid)

)