-- individual member of a team

create table pokemon.member (
  member_id serial,
  team_id   serial,
  dex_id    serial,

  gender    char(1),
  level     int default 50,
  nickname  varchar(12),
  shiny     char(1) default '0',

  primary key(member_id),

  constraint fk_team 
    foreign key(team_id)
    references team(team_id),
    
  constraint fk_dex
    foreign key(dex_id)
    references pokedex(dex_id)
);
