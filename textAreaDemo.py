"""
Author  : Louisgene  
Date    : 7/14/2023
Program : textAreaDemo.py

GUI-based focusing multi-line text areas  

"""

from breezypythongui import EasyFrame
import tkinter as tk
# Other imports go here

# Class header (application name will change project to project)
class TextAreaDemo(EasyFrame):
    # Definition of our class constructor method
    def __init__(self):
        #Call to the Easy Frame constrctor method
        EasyFrame.__init__(self, title = "Investment calculator", width = 450, height = 400, resizable = False)
        
        
        #Create and add data the components to the window
        self.addLabel(text = "Initial Amount", row = 0, column = 0)
        self.addLabel(text = "Number of the Years", row = 1, column = 0)
        self.addLabel(text = "Interest Rate in %", row = 2, column = 0)

        self.amount = self.addFloatField(value = 0, row = 0, column = 1)
        self.period = self.addIntegerField(value = 0, row = 1, column = 1)
        self.rate = self.addIntegerField(value = 0, row = 2, column = 1)

        self.outputArea = self.addTextArea("", row = 4, column = 0, columnspan = 2,
            width = 50, height = 15)
        self.outputArea["background"] = "lightgreen"
        self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2,
            command = self.compute)
        self.compute["background"] = "lightgreen"
        self.compute["foreground"]= "black"
        self.compute["width"] = 21

    #definition of the compute() function
    def compute(self):
        #compute the investment schedule based on the inputs and outputs the schedule
        #obtain and validate the inputs
        startBalance = self.amount.getNumber()
        rate = self.rate.getNumber() / 100
        years = self.period.getNumber()
        if startBalance == 0 or rate == 0 or years== 0:
            return

        #Set the hearder for the table
        result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")
        
        #compute and append the result for each year
        totalInterest = 0.0
        for year in range(1, years + 1):
            interest = startBalance * rate
            endBalance = startBalance + interest
            result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
            startBalance = endBalance
            totalInterest += interest

            #Append the total for the period
            result += "Ending Balance: $%0.2f\n" % endBalance
            result += "total interest earned: $%0.2f\n" % totalInterest

            #Output the result while preserving read-only status
            self.outputArea["state"] = "normal"
            self.outputArea.setText(result)
            self.outputArea["state"] = "disabled"

class CenterScreenGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Centered Window")

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the x and y coordinates for the window
        x = (screen_width // 2) - (500 // 2)  # Center horizontally
        y = (screen_height // 2) - (300 // 2)  # Center vertically

        # Set the window size and position
        self.root.geometry(f"500x300+{x}+{y}")


# Global definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
    TextAreaDemo().mainloop()
    
# Create an instance of Tkinter root window
root = tk.Tk()
# Create an instance of the CenterScreenGui class
app = CenterScreenGui(root)

# Global call to main() for program entry
if __name__ == '__main__':
    main()