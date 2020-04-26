import copy;
import typing;

from . import cell;

def _init_state(loc, inits):
   state = typing.Optional[cell.STATES];
   if (loc in inits):
      state = cell.STATES.LIVE;
   else:
      state = cell.STATES.DEAD;
   # fi
   return state;
# fed

class Universe(object):

   cells = typing.Optional[dict];
   
   wdth = typing.Optional[int];
   hght = typing.Optional[int];

   init_states = typing.Optional[list];

   def __init__(
      self,
      array_wdth,
      array_hght,
      live_cells,
   ):
      self.wdth = array_wdth;
      self.hght = array_hght;
      self.init_states = live_cells;
      self.cells = {};
      for i in range(0, array_wdth, 1):
         for j in range(0, array_hght, 1):
            self.cells[(i, j,)] = cell.Cell(
                  _init_state((i, j,), self.init_states,),
                  (i, j,),
                  cell.NEIGHBOURHOODS.MOORE,
               );
         # rof
      # rof
      return None;
   # fed

   def get_cell(self, loc,):
      """Retrive cell based-on location, using circular indexing for any negative location(s)."""
      cell_obj = typing.Optional[cell.Cell];
      x = loc[0];
      y = loc[1];
      if (loc[0] < 0):
         x = self.hght + loc[0];
      elif (loc[0] >= self.hght):
         x = loc[0] - self.hght;
      # fi
      if (loc[1] < 0):
         y = self.wdth + loc[1];
      elif (loc[1] >= self.wdth):
         y = loc[1] - self.wdth;
      # fi
      cell_obj = self.cells[(x, y,)];
      return cell_obj;
   # fed

   def tick(self,):
         frozen_universe = copy.deepcopy(self);
         for cell_loc in self.cells:
            self.cells[cell_loc].tick(frozen_universe,);
         # rof
         return None;
   # fed

# ssalc
