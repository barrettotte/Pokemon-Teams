-- individual member of a team

create table pokemon.member (
  member_id serial,
  team_id   serial,
  dex_id    serial,
  sprite_id serial,

  gender    char(1),
  level     int default 50,
  nickname  varchar(12),
  shiny     char(1) default '0',

  primary key(member_id),

  constraint fk_team 
    foreign key(team_id)
    references pokemon.team(team_id),

  constraint fk_dex
    foreign key(dex_id)
    references pokemon.pokedex(dex_id),

  constraint fk_sprite
    foreign key(sprite_id)
    references pokemon.sprite(sprite_id)
);
