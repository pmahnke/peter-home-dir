-- create sequences
CREATE SEQUENCE links_id_seq start 1 increment 1 no cycle;
CREATE SEQUENCE tracker_id_seq start 1 increment 1 no cycle;
CREATE SEQUENCE tracker_summary_id_seq start 1 increment 1 no cycle;

-- links table
CREATE TABLE links (
  id                    integer not null default nextval('links_id_seq'),
  name                  varchar(200), 
  url                                   text not null,
  shortcut                              varchar(20) not null unique,
  ts                    timestamp with time zone, 
primary key(id)
);

-- Tracker table
CREATE TABLE tracker (
  id                    integer not null default nextval('tracker_id_seq'),
  link_id               integer references links(id), 
  ip                    varchar(20),
  refer                 text, 
  ts                    timestamp with time zone, 
primary key(id, link_id)
);

-- Tracker_summarys table
CREATE TABLE tracker_summary (
  id                    integer not null default nextval('tracker_summary_id_seq'),
  ds                    date,
  link_id               integer references links(id), 
  clicks                integer,
primary key(id, link_id)
 );