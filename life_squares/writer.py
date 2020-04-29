import curses;
import typing;

from . import cell;


class Writer(object):
   """Base Universe Output Writer."""

   RENDER_COLOURS = {
      cell.STATES.LIVE: None,
      cell.STATES.DEAD: None,
   };

   def render(self,):
      return None;
   # fed

   def close(self,):
      return None;
   # fed
# ssalc


class CursesWriter(Writer):
   """Universe Output Writer to Terminal using `curses`."""
   RENDER_CHARACTERS = {
      cell.STATES.LIVE: "■",
      cell.STATES.DEAD: "_",
   };

   aspect_ratio = [3, 1];  # [w, h]

   screen_obj = typing.Optional[str];

   def __init__(self, window_w, window_h,):
      self.screen_obj = curses.initscr();
      self.screen_obj.resize(
         window_h * self.aspect_ratio[1],
         window_w * self.aspect_ratio[0],)
      return None;
   # fed

   def render(self, universe_cells, crnt_tick, length,):
      for (loc, cell_obj) in universe_cells.items():
         self.screen_obj.addstr(
            loc[1] * self.aspect_ratio[1],  # y
            loc[0] * self.aspect_ratio[0],  # x
            self.RENDER_CHARACTERS[cell_obj.state_crnt]
         )
      # rof
      self.screen_obj.refresh()
      curses.napms(250)
      return None;
   # fed

   def close(self,):
      curses.endwin();
      return None;
   # fed
# ssalc


class SvgWriter(Writer):
   """Universe Output Writer for SVG Images."""
   RENDER_SIZE = 5;

   RENDER_INDENTATION = "      ";  # @TODO: Parse this dynamically.

   RENDER_COLOURS = {
      cell.STATES.LIVE: "black",
      cell.STATES.DEAD: "white",
   };

   template_str = typing.Optional[str];

   def __init__(self, ):
      with open(os.path.join(crnt_dir, "template.html"), "r") as file_obj:
         self.template_str = file_obj.read();
      # htiw
      return None;
   # fed

   def render(self, universe_cells, crnt_tick, length,):
      title_str = "GameOfLife_{0:04d}-{1:04d}".format(crnt_tick, length);
      template_str = self.template_str.replace(
         "{{TITLE}}",
         title_str,
      );
      cells_str = "";
      for (loc, cell_obj) in universe_cells.items():
         cells_str += (
            self.RENDER_INDENTATION
            + "<rect x=\"{0}\" y=\"{1}\" width=\"{2}\" height=\"{2}\" fill=\"{3}\"/>\n".format(
               self.RENDER_SIZE * loc[0],
               self.RENDER_SIZE * loc[1],
               self.RENDER_SIZE,
               self.RENDER_COLOURS[cell_obj.state_crnt],
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
      return None;
   # fed

   def close(self,):
      return None;
   # fed
# ssalc
