
import os;
import pathlib;
import typing;

from . import universe;
from . import cell;

RENDER_SIZE = 5;

RENDER_INDENTATION = "      ";  # @TODO: Parse this dynamically.

RENDER_COLOURS = {
   cell.STATES.LIVE: "black",
   cell.STATES.DEAD: "white",
};

crnt_dir = pathlib.Path(__file__).parent;


class Game(object):

   template_str = typing.Optional[str];
   crnt_universe = typing.Optional[universe.Universe];

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

      with open(os.path.join(crnt_dir, "template.html"), "r") as file_obj:
         self.template_str = file_obj.read();
      # htiw
      return None;
   # fed

   def run(self, length):
      self.render(0, length, RENDER_SIZE,)
      for i in range(1, length+1, 1):
         self.crnt_universe.tick();
         self.render(i, length, RENDER_SIZE,);
      # rof
   # fed

   def render(self, crnt_tick, length, render_size,):
      title_str = "GameOfLife_{0:04d}-{1:04d}".format(crnt_tick, length);
      template_str = self.template_str.replace(
         "{{TITLE}}",
         title_str,
      );
      cells_str = "";
      for (loc, cell_obj) in self.crnt_universe.cells.items():
         cells_str += (
            RENDER_INDENTATION
            + "<rect x=\"{0}\" y=\"{1}\" width=\"{2}\" height=\"{2}\" fill=\"{3}\"/>\n".format(
               render_size * loc[0],
               render_size * loc[1],
               render_size,
               RENDER_COLOURS[cell_obj.state_crnt],
            )
         );
      # rof
      template_str = template_str.replace(
         "{{UNIVERSE}}",
         cells_str,
      );
      with open(os.path.join(crnt_dir, title_str + ".html"), "w") as file_obj:
         file_obj.write(template_str);
      # htiw
   # fed

# ssalc