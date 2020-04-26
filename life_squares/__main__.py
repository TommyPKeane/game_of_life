from . import game;

def get_cross(x, y,):
   arr = [
      (x + 0, y - 1,),
      (x + 0, y + 0,),
      (x + 0, y + 1,),
      (x - 1, y + 0,),
      (x + 1, y + 0,),
   ];
   return arr;


def get_block(x, y,):
   arr = [
      (x - 1, y - 1,),
      (x + 0, y + 0,),
      (x - 1, y + 0,),
      (x + 0, y - 1,),
   ];
   return arr;


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


if __name__ == '__main__':

   initial_cells = [];
   initial_cells.extend(get_glider(9,10,));
   initial_cells.extend(get_glider(15,20,));
   initial_cells.extend(get_glider(21,30,));
   initial_cells.extend(get_glider(27,40,));

   initial_cells.extend(get_toad(90,80,));

   initial_cells.extend(get_block(75,77,));

   initial_cells = list(set(initial_cells));

   game_obj = game.Game(
      100,
      100,
      initial_cells,
   );
   game_obj.run(50);
# fi