import random;

class Pattern(object):
   """Base Class"""
   _patterns = [];
   def __init__(self,):
      return None;
   # fed
   def random_pattern(self, x, y,):
      rand_pattern = random.randint(0, len(self._patterns));
      arr = self._patterns[rand_pattern](x, y,);
      return arr;
# ssalc


class Moore1Patterns(Pattern):

   def __init__(self,):
      self._patterns = [
         func
         for
         func in dir(Moore1Patterns)
         if (
            callable(getattr(Moore1Patterns, func))
            and func.startswith("get_")
         )
      ];
      return None;
   # fed

   def get_cross(self, x, y,):
      arr = [
         (x + 0, y - 1,),
         (x + 0, y + 0,),
         (x + 0, y + 1,),
         (x - 1, y + 0,),
         (x + 1, y + 0,),
      ];
      return arr;
   # fed

   def get_block(self, x, y,):
      arr = [
         (x - 1, y - 1,),
         (x + 0, y + 0,),
         (x - 1, y + 0,),
         (x + 0, y - 1,),
      ];
      return arr;
   # fed

   def get_beehive(self, x, y,):
      arr = [
         (x - 1, y - 2,),
         (x + 0, y - 2,),
         (x - 1, y + 0,),
         (x + 0, y + 0,),
         (x - 2, y - 1,),
         (x + 1, y - 1,),
      ];
      return arr;
   # fed

   def get_tub(self, x, y,):
      arr = [
         (x - 1, y + 0,),
         (x + 0, y - 1,),
         (x + 0, y + 1,),
         (x + 1, y + 0,),
      ];
      return arr;
   # fed

   def get_beacon(self, x, y,):
      arr = [];
      arr.extend(self.get_block(x, y,));
      arr.extend(self.get_block(x + 2, y + 2,));
      return arr;
   # fed

   def get_toad_v(self, x, y,):
      arr = [
         (x - 1, y + 0,),
         (x - 1, y - 1,),
         (x - 1, y - 2,),
         (x + 0, y - 1,),
         (x + 0, y + 0,),
         (x + 0, y + 1,),
      ];
      return arr;
   # fed

   def get_toad_h(self, x, y,):
      arr = [
         (x + 1, y - 1,),
         (x + 0, y + 0,),
         (x + 0, y - 1,),
         (x - 1, y - 1,),
         (x - 2, y + 0,),
         (x - 1, y + 0,),
      ];
      return arr;
   # fed

   def get_glider(self, x, y,):
      arr = [
         (x - 1, y + 1,),
         (x + 0, y + 1,),
         (x + 1, y + 1,),
         (x + 1, y + 0,),
         (x + 0, y - 1,),
      ];
      return arr;
   # fed
# ssalc
