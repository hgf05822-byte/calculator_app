from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class DiaryApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.label = Label(text="اكتب مذكراتك هنا:", size_hint=(1, 0.1))
        self.layout.add_widget(self.label)
        
        self.text_input = TextInput(hint_text='ماذا حدث اليوم؟', size_hint=(1, 0.6))
        self.layout.add_widget(self.text_input)
        
        self.btn = Button(text="حفظ المذكرة", size_hint=(1, 0.2))
        self.btn.bind(on_press=self.save_note)
        self.layout.add_widget(self.btn)
        
        self.result = Label(text="", size_hint=(1, 0.1))
        self.layout.add_widget(self.result)
        
        return self.layout

    def save_note(self, instance):
        note = self.text_input.text
        if note:
            self.result.text = "تم حفظ المذكرة بنجاح!"
            self.text_input.text = ""

if __name__ == '__main__':
    DiaryApp().run()
