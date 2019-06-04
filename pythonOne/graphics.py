"""
created on 2/29/29
"""
### Imports
from . import program as p
from . import control as c
from contextlib import contextmanager
from warnings import warn
from random import randint
### Functions
def init_graphics(title, width="500", height="500"):
    if not ("ui" in p.current_program.options):
        raise ValueError("'ui' must be in options")
    if p.current_program.lang == "py":
        p.current_program.add("root = tk.Tk()")
        p.current_program.add("root.title(" + title + ")")
        p.current_program.add("root.geometry('" + width + "x" + height + "')")
        p.current_program.add("root.resizable(False, False)")
        p.current_program.add("canvas = tk.Canvas(root, width=" + width + ", height=" + height + ")")
        p.current_program.add("canvas.pack()")
    if p.current_program.lang == "cs":
        p.current_program.add("// Title: " + title)
        p.current_program.add("this.MinWidth = " + width + ";")
        p.current_program.add("this.MaxWidth = " + width + ";")
        p.current_program.add("this.MinHeight = " + height + ";")
        p.current_program.add("this.MaxHeight = " + height + ";")
def finish_graphics():
    if p.current_program.lang == "py":
        p.current_program.add("root.mainloop()")

## Timer
def set_timer(name, func, ms, repeat=True):
    if p.current_program.lang == "py":
        p.current_program.add("def " + name + "():")
        """
        p.current_program.indent += 1
        p.current_program.add("while True:")
        """
        p.current_program.indent += 1
        p.current_program.add(func + "()")
        if repeat:
            p.current_program.add("root.after(" + ms + ", " + name + ")")
        p.current_program.indent -= 1
        """
        p.current_program.add(name + " = threading.Thread(target=" + func + ")")
        p.current_program.add(name + ".start()")
        """
        p.current_program.add("root.after(" + ms + ", " + name + ")")
    if p.current_program.lang == "cs":
        p.current_program.add("var " + name + " = new DispatcherTimer();")
        p.current_program.add(name + ".Tick += " + func + ";")
        p.current_program.add(name + ".Interval = new TimeSpan(0, 0, 0, 0, " + ms + ");")
        p.current_program.add(name + ".Start();")
@contextmanager
def timer_handler(name):
    if p.current_program.lang == "py":
        p.current_program.add("def " + name + "():")
    if p.current_program.lang == "cs":
        p.current_program.add("public " + ("static " if not ("ui" in p.current_program.options) else "") + "void " + name + "(object source, object e) {")
    p.current_program.indent += 1
    yield
    c.close()

## Drawing
def clear():
    if p.current_program.lang == "py":
        p.current_program.add("for i in range(len(shapes)):")
        p.current_program.indent += 1
        p.current_program.add("canvas.delete(shapes[i])")
        p.current_program.indent -= 1
        p.current_program.add("del shapes[:]")
    if p.current_program.lang == "cs":
        p.current_program.add("canvas.Children.Clear()")
def draw_rect(x, y, width, height, fill, stroke):
    number = str(randint(0, 10000))
    if p.current_program.lang == "py":
        p.current_program.add("rect" + number + " = canvas.create_rectangle(" + x + "," + y + "," + x + " + " + width + "," + y + " + " + height + ",outline='" + stroke + "'.lower(),fill='" + fill + "'.lower())")
        p.current_program.add("shapes.append(rect" + number + ")")
    if p.current_program.lang == "cs":
        p.current_program.add("var rect" + number + " = new Rectangle();")
        p.current_program.add("rect" + number + ".Width = " + width + ";")
        p.current_program.add("rect" + number +".Height = " + height + ";")
        p.current_program.add("rect" + number + ".Fill = new SolidColorBrush(Windows.UI.Colors." + fill + ");")
        p.current_program.add("rect" + number + ".Stroke = new SolidColorBrush(Windows.UI.Colors." + stroke + ");")
        p.current_program.add("canvas.Children.Add(rect" + number + ");")
        p.current_program.add("Canvas.SetLeft(rect" + number + ", " + x + ");")
        p.current_program.add("Canvas.SetTop(rect" + number + ", " + y + ");")
def draw_image(x, y, img_path):
    if p.current_program.lang == "py":
        warn("'py' does not support images")
    if p.current_program.lang == "cs":
        number = str(randint(0, 10000))
        p.current_program.add("Image img" + number + " = new Image();")
        p.current_program.add("img" + number + ".Source = new BitmapImage(new Uri(\"ms-appx:///" + img_path + "\"));")
        p.current_program.add("canvas.Children.Add(img" + number + ");")
        p.current_program.add("Canvas.SetLeft(img" + number + ", " + x + ");")
        p.current_program.add("Canvas.SetTop(img" + number + ", " + y + ");")
def draw_text(x, y, text, font_size=12, color="White"):
    if p.current_program.lang == "cs":
        number = str(randint(0, 10000))
        p.current_program.add("TextBlock text" + number + " = new TextBlock();")
        p.current_program.add("text" + number + ".Text = " + text + ";")
        p.current_program.add("text" + number + ".FontSize = " + font_size + ";")
        p.current_program.add("text" + number + ".Foreground = new SolidColorBrush(Windows.UI.Colors." + color + ");")
        p.current_program.add("canvas.Children.Add(text" + number + ");")
        p.current_program.add("Canvas.SetLeft(text" + number + ", " + x + ");")
        p.current_program.add("Canvas.SetRight(text" + number + ", " + y + ");")
    

## Events
# Click
@contextmanager
def on_click_handler(name, button="left"):
    if not (button in ["left", "right"]):
        raise ValueError("button must be right or left")
    if p.current_program.lang == "py":
        p.current_program.add("def " + name + "(e):")
    if p.current_program.lang == "cs":
        p.current_program.add("public void " + name  + "(object sender, PointerRoutedEventArgs e) {")
    p.current_program.indent += 1
    if p.current_program.lang == "cs":
        p.current_program.add("var pt = e.GetCurrentPoint(this);")
        if button == "left":
            p.current_program.add("if (pt.Properties.IsLeftButtonPressed) {")
        else:
            p.current_program.add("if (pt.Properties.IsRightButtonPressed) {")
        p.current_program.indent += 1
    yield
    if p.current_program.lang == "cs":
        c.close()
        p.current_program.add("e.Handled = true;")
    c.close()
def on_click(handler, button="left"):
    if p.current_program.lang == "py":
        p.current_program.add("canvas.bind('<Button-" + ("1" if button == "left" else "3") + ">'," + handler + ")")
    if p.current_program.lang == "cs":
        p.current_program.add("canvas.PointerPressed += " + handler + ";")
def get_click_pos(x_or_y):
    if not (x_or_y in ["x", "y"]):
        raise ValueError("x_or_y must 'x' or 'y'!")
    if p.current_program.lang == "py":
        return "e." + x_or_y
    if p.current_program.lang == "cs":
        return "pt.Position." + x_or_y.upper()
# Press
