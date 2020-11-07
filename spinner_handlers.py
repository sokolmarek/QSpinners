from main import *


class SpinnerHandlers(MainWindow):

    def update_spinner_4(self, angle):
        style = f"""
            border-radius: 85px;
            background-color: background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{-angle}, 
            stop:0 #689F38, 
            stop:0.454545 #8BC34A, 
            stop:0.784091 #C5E1A5, 
            stop:0.886364 rgba(255, 255, 255, 255), 
            stop:1 rgba(255, 255, 255, 255));\n"
            stop:0.3 #DFDFDF, 
            stop:0.2999 #3F51B5);
        """
        self.ui.circle_outer_4.setStyleSheet(style)

    def update_spinner_3(self):
        style = f"""
                 	border-radius: 85px;
                 	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{-angle}, 
                 	stop:0.3 #DFDFDF, 
                 	stop:0.2999 #3F51B5);
                 """
        self.ui.circle_outer_1.setStyleSheet(style)

    def update_spinner_2(self):
        pass

    def update_spinner_1(self, angle):
        style = f"""
         	border-radius: 85px;
         	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:{-angle}, 
         	stop:0.3 #DFDFDF, 
         	stop:0.2999 #3F51B5);
         """
        self.ui.circle_outer_1.setStyleSheet(style)
