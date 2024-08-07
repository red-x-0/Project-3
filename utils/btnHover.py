
def btnHover(btn, color, default_color):
  def on_enter(e):
    btn['background'] = color
    
  def on_leave(e):
    btn['background'] = default_color
  
  btn.bind("<Enter>", on_enter)  
  btn.bind("<Leave>", on_leave)
   