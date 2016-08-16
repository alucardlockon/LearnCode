drop table if exists myweibo
create table myweibo(
	wid bigint primary key auto_increment,
	userid int,
	content varchar(1000),
	tranmit_id bigint
)

drop table if exists myweibo_user
create table myweibo_user(
	uid int primary key auto_increment,
	username varchar(255),
	usermail varchar(500),
	password varchar(255),
	selfintro varchar(4000),
	first_login_time datetime,
	last_login_time datetime
)

drop table if exists myweibo_follow
create table myweibo_follow(
	uid int,
	followed_uid int
)

drop table if exists myweibo_follow
create table myweibo_like(
	uid int,
	wid bigint
)