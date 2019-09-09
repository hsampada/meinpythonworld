class parent():
    def __init__(self,last_name,eye_color):
        print("Parent constructor called")
        
        self.last_name=last_name
        self.eye_color=eye_color


class child(parent):
    def __init__(self,last_name,eye_color,toys):
        print("Chid constructor called")
        parent.__init__(self,last_name,eye_color)
        self.toys=toys
        
