import enum;
import typing;

class STATES(enum.Enum):
   LIVE = -1;
   DEAD = 1;
# ssalc

class NEIGHBOURHOODS(enum.Enum):
   MOORE = 0;
   VON_NEUMANN = 1;
   HEXAGONAL = 2;
# ssalc


class TransitionRuleset(object):

   def _get_neighbour_states(self, cell_obj, universe,):
      """Create a list of the states of all of a cell's neighbours."""
      neighbour_states = [];

      for crnt_neighbour_loc in cell_obj.neighbours:
         neighbour_cell = universe.get_cell(crnt_neighbour_loc)
         neighbour_states.append(neighbour_cell.state_crnt)
      # rof

      return neighbour_states;
   # fed

   def get_next_state(self, cell_obj, universe,):
      """Determine the next state of the given cell based-on the state of relevant cells in the given universe."""
      next_state = typing.Optional[STATES];

      neighbour_states = self._get_neighbour_states(cell_obj, universe)

      live_neighbours = neighbour_states.count(STATES.LIVE)
      dead_neighbours = neighbour_states.count(STATES.DEAD)

      if (cell_obj.state_crnt == STATES.LIVE):
         if (live_neighbours < 2):
            next_state = STATES.DEAD;  # Lonely
            print("Cell Died! {0} | Neighbours: {1}".format(cell_obj.location, neighbour_states,))
         elif (live_neighbours > 3):
            next_state = STATES.DEAD;  # Smothered
            print("Cell Died! {0} | Neighbours: {1}".format(cell_obj.location, neighbour_states,))
         elif (live_neighbours in (2, 3)):
            next_state = STATES.LIVE;  # Comfortable
         else:
            raise ValueError("Bad State Condition")
         # fi
      elif (cell_obj.state_crnt == STATES.DEAD):
         if (live_neighbours == 3):
            next_state = STATES.LIVE;  # Mazel Tov!
            print("Cell Born! {0} | Neighbours: {1}".format(cell_obj.location, neighbour_states))
         else:
            next_state = STATES.DEAD;  # Stasis
         # fi
      else:
         raise ValueError("Unknown Cell State: {0}".format(cell_obj.state_crnt))
      # fi

      return next_state;
   # fed

# ssalc


class Cell(object):
   """A Cell in the Game Of Life, assuming a 2D array of square cells as the Universe.

   @TODO Support more generic universe configurations/layouts.
   @TODO Improve the history to support logging.
   @TODO Support rulesets and smarter initializations.
   @TODO Support neighbourhood radius (larger neighbourhoods).
   """

   neighbours = typing.Optional[tuple];
   neighbourhood = typing.Optional[NEIGHBOURHOODS];

   state_prev = typing.Optional[STATES];
   state_crnt = typing.Optional[STATES];
   # state_next = typing.Optional[STATES];

   location = typing.Optional[tuple];

   transition_obj = typing.Optional[TransitionRuleset];

   def __init__(
      self,
      init_state,
      location,
      neighbourhood,
   ):
      self.state_prev = None;
      self.state_crnt = init_state;
      # self.state_next = None;
      self.location = location;
      self.neighbourhood = neighbourhood;
      self._get_neighbours();
      self.transition_obj = TransitionRuleset();
      return None;
   # fed

   def _get_neighbours(self,):
      new_neighbours = [];
      x = self.location[0];
      y = self.location[1];
      if (self.neighbourhood == NEIGHBOURHOODS.MOORE):
         new_neighbours = [
            (x - 1, y - 1),
            (x - 1, y + 0),
            (x - 1, y + 1),
            (x + 0, y - 1),
            (x + 0, y + 1),
            (x + 1, y - 1),
            (x + 1, y + 0),
            (x + 1, y + 1),
         ]
      elif (self.neighbourhood == NEIGHBOURHOODS.VON_NEUMANN):
         new_neighbours = [
            (x - 1, y + 0),  # Up
            (x + 0, y - 1),  # Left
            (x + 1, y + 0),  # Right
            (x + 0, y + 1),  # Down
         ]
      elif (self.neighbourhood == NEIGHBOURHOODS.HEXAGONAL):
         new_neighbours = [
            (x - 1, y - 1),
            (x - 1, y + 0),
            (x + 0, y + 1),
            (x + 1, y + 0),
            (x + 1, y + 1),
            (x + 0, y + 1),
         ]
      else:
         raise ValueError("Unknown Neighbourhood Configuration: {0}".format(self.neighbourhood));
      # fi
      self.neighbours = new_neighbours;
      return None
   # fed

   def tick(self, universe_obj):
      self.state_prev = self.state_crnt;
      self.state_crnt = self.transition_obj.get_next_state(self, universe_obj);
      return None
   # fed

# ssalc