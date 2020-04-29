from . import game;
from . import patterns;


if __name__ == '__main__':

   pattern_provider = patterns.Moore1Patterns();

   initial_cells = [];
   # initial_cells.extend(pattern_provider.get_glider(9,10,));
   # initial_cells.extend(pattern_provider.get_glider(15,20,));
   # initial_cells.extend(pattern_provider.get_glider(21,30,));
   # initial_cells.extend(pattern_provider.get_glider(27,35,));

   # initial_cells.extend(pattern_provider.get_toad_v(5,5,));
   # initial_cells.extend(pattern_provider.get_toad_h(35,5,));

   # initial_cells.extend(pattern_provider.get_beacon(30,10,));
   # initial_cells.extend(pattern_provider.get_beehive(4,20,));
   initial_cells.extend(pattern_provider.get_tub(20,25,));
   initial_cells.extend(pattern_provider.get_tub(20,27,));
   initial_cells.extend(pattern_provider.get_tub(24,25,));
   initial_cells.extend(pattern_provider.get_tub(24,27,));

   initial_cells.extend(pattern_provider.get_tub(10,15,));
   initial_cells.extend(pattern_provider.get_tub(10,17,));
   initial_cells.extend(pattern_provider.get_tub(14,15,));
   initial_cells.extend(pattern_provider.get_tub(14,17,));

   initial_cells = list(set(initial_cells));

   game_obj = game.Game(
      40,
      40,
      initial_cells,
   );
   game_obj.run(100);
# fi
