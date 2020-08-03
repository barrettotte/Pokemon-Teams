
class Team():

  def __init__(self, team_id, name):
    self.team_id = team_id
    self.name = name


class Member():
  
  def __init__(self, team_id, dex_id, sprite_id, gender, level, nickname, shiny):
    self.team_id = team_id
    self.dex_id = dex_id
    self.sprite_id = sprite_id
    self.gender = gender
    self.level = level
    self.nickname = nickname
    self.shiny = shiny


class DexRecord():

  def __init__(self, dex_id, name):
    self.dex_id = dex_id
    self.name = name


class Sprite():

  def __init__(self, dex_id, form, has_female, slug):
    self.dex_id = dex_id
    self.form = form
    self.has_female = has_female
    self.slug = slug
