from . import game;
from . import patterns;


if __name__ == '__main__':

   initial_cells = [];
   initial_cells.extend(patterns.get_glider(9,10,));
   initial_cells.extend(patterns.get_glider(15,20,));
   initial_cells.extend(patterns.get_glider(21,30,));
   initial_cells.extend(patterns.get_glider(27,40,));

   initial_cells.extend(patterns.get_toad(90,80,));

   initial_cells.extend(patterns.get_block(75,77,));

   initial_cells = list(set(initial_cells));

   game_obj = game.Game(
      40,
      40,
      initial_cells,
   );
   game_obj.run(50);
# fi
