-- Peter's temporary ad server

-- create sequences
CREATE SEQUENCE advertiser_id_seq start 1 increment 1 no cycle;
CREATE SEQUENCE banner_id_seq start 1 increment 1 no cycle;
CREATE SEQUENCE contact_id_seq start 1 increment 1 no cycle;
CREATE SEQUENCE site_id_seq start 1 increment 1 no cycle;
CREATE SEQUENCE zone_id_seq start 1 increment 1 no cycle;
CREATE SEQUENCE tracker_id_seq start 1 increment 1 no cycle;
CREATE SEQUENCE tracker_summary_id_seq start 1 increment 1 no cycle;


-- Contacts table
CREATE TABLE contacts (
 id 			integer not null default nextval('contact_id_seq'),
 name  		varchar(200), 
 email 		varchar(200), 
 phone 		varchar(50),
primary key(id)
);

-- Advertisers table
CREATE TABLE advertisers (
 id 			integer not null default nextval('advertiser_id_seq'),
 name 			varchar(200), 
 contact_id	integer references contacts(id),
primary key(id)
);

-- Banners table
CREATE TABLE banners (
 id 			integer not null default nextval('banner_id_seq'),
 name 			varchar(200), 
 file_pointer 	varchar(256), 
 url 			text, 
 width 		integer, 
 height		integer, 
 start_date 	date,
 end_date 		date check (end_date >= start_date), 
 is_display 	boolean not null default 'f', 
 advertiser_id integer references advertisers(id),
primary key(id)
);

-- Zones table
CREATE TABLE zones (
 id 			integer not null default nextval('zone_id_seq'),
 name  		varchar(200), 
 description	text, 
 width 		integer, 
 height 		integer,
primary key(id)
);

-- Banners 2 Zones link table
CREATE TABLE banners_zones (
 zone_id 		integer references zones(id),
 banner_id 	integer references banners(id),
 priority 		integer,
primary key(zone_id, banner_id)
);

-- Sites table
CREATE TABLE sites (
 id 			integer not null default nextval('site_id_seq'),
 name  		varchar(200), 
 description 	text, 
 is_display      boolean,
 contact_id 	integer references contacts(id),
primary key(id)
);

-- Zones 2 Sites link table
CREATE TABLE zones_sites (
 zone_id 		integer references zones(id),
 site_id 		integer references sites(id),
primary key(zone_id, site_id)
);

-- Tracker table
CREATE TABLE tracker (
 id 			integer not null default nextval('tracker_id_seq'),
 type  		varchar(30), 
 zone_id 		integer references zones(id), 
 banner_id 	integer references banners(id),
 ip  			varchar(20),
 refer 		text, 
 ts 			timestamp with time zone, 
 bkey 			varchar(50),
primary key(id, zone_id, banner_id)
);

-- Tracker_summarys table
CREATE TABLE tracker_summary (
 id                    integer not null default nextval('tracker_summary_id_seq'),
 ds  			date,
 banner_id             integer references banners(id), 
 zone_id               integer references zones(id),
 views			integer,
 clicks		integer,
primary key(id, banner_id, zone_id)
);

