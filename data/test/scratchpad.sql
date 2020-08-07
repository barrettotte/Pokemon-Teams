
-- test data for retrieving team
insert into pokemon.team (label) 
values('TEST CREATE')
returning team_id
;


-- test data for retrieving members of team
insert into pokemon.member (team_id, dex_id, sprite_id, gender, level, nickname, slot, shiny)
values (22, 764, 1036, 'M', 50, 'CREATED', 1, '0')
returning member_id
;
