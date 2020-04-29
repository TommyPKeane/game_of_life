
import os;
import pathlib;
import typing;

from . import cell;
from . import universe;
from . import writer;


crnt_dir = pathlib.Path(__file__).parent;


class Game(object):
   """Game of Life for Automata Cells."""
   template_str = typing.Optional[str];
   crnt_universe = typing.Optional[universe.Universe];
   writer_obj = typing.Optional[writer.Writer];

   def __init__(
      self,
      array_wdth,
      array_hght,
      live_cells,
   ):
      self.crnt_universe = universe.Universe(
         array_wdth,
         array_hght,
         live_cells,
      );
      self.writer_obj = writer.CursesWriter(array_wdth, array_hght,);
      return None;
   # fed

   def run(self, length):
      self.writer_obj.render(self.crnt_universe.cells, 0, length,)
      for i in range(1, (length + 1), 1):
         self.crnt_universe.tick();
         self.writer_obj.render(self.crnt_universe.cells, i, length,);
      # rof
      self.writer_obj.close();
   # fed
# ssalc
