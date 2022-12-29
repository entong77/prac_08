from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

__author__ = 'Zhao Entong'
MILES_TO_KM = 1.60934


class MilesConverter(App):
    message = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation output result to label widget."""
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """Handle up/down button press, update the text input with new value, call calculation function."""
        value = self.get_validated_miles() + change
        self.root.ids.text_input.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverter().run()