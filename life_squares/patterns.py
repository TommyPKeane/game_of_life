

def get_cross(x, y,):
   arr = [
      (x + 0, y - 1,),
      (x + 0, y + 0,),
      (x + 0, y + 1,),
      (x - 1, y + 0,),
      (x + 1, y + 0,),
   ];
   return arr;
# fed


def get_block(x, y,):
   arr = [
      (x - 1, y - 1,),
      (x + 0, y + 0,),
      (x - 1, y + 0,),
      (x + 0, y - 1,),
   ];
   return arr;
# fed


def get_toad(x, y,):
   arr = [
      (x - 1, y - 1,),
      (x + 0, y + 0,),
      (x - 1, y + 0,),
      (x + 0, y - 1,),
      (x - 2, y + 0,),
      (x + 1, y - 1,),
   ];
   return arr;
# fed


def get_glider(x, y,):
   """
   ```
       x
     x x
      xx
   ```
   """
   arr = [
      (x - 1, y + 1,),
      (x + 0, y + 1,),
      (x + 1, y + 1,),
      (x + 1, y + 0,),
      (x + 0, y - 1,),
   ];
   return arr;
# fed
