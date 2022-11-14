"""
CP1404 Practical 8 - Miles to Kilometres Converter
Estimated Time: 60 minutes
Actual Time: 54 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesKmConverterApp(App):
    """MilesKmConverterApp is a Kivy App for converting miles to kilometres."""
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Convert miles to kilometres"
        return self.root

    def handle_calculate(self):
        """Handle calculation and output result to label widget."""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle the increments determined by the up/down button, update text input with new value and handle
        calculation of new value."""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Convert text input from text entry widget into a float and return 0 if text not valid."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesKmConverterApp().run()
