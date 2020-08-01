-- really simple key/val for sprites using https://msikma.github.io/pokesprite/
--
-- base URL: 
--   https://raw.githubusercontent.com/msikma/pokesprite/master/pokemon-gen8/{{regular|shiny}}/{{slug}}.png

create table pokemon.sprite (
  sprite_id serial,
  dex_id    serial,
  form      varchar(32),
  slug      varchar(128),
  shiny     char(1) default '0',

  primary key(sprite_id),

  constraint fk_dex
    foreign key(dex_id)
    references pokedex(dex_id),

);
