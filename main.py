import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Quote(BoxLayout):
    quote_widget = ObjectProperty()

    def get_random_quote(self):
        rs = (None, None)
        try:
            conn = sqlite3.connect('db/randomquotes')
            c = conn.cursor()
            c.execute( 'SELECT quote, author FROM quotes ORDER BY RANDOM() LIMIT 1')
            rs = c.fetchone()   
        except sqlite3.Error:
            pass
        finally:
            conn.close()
    
        data = {'quote': rs[0], 'author': rs[1]}
        
        return data
    
    def display_quote(self):
        random_quote = self.get_random_quote()
        self.quote_widget.text = r'"%s"%s-- %s' % \
            (random_quote['quote'], '\n' * 2, random_quote['author'])
        
class RandomQuotesApp(App):
    def build(self):
        quote = Quote()
        quote.display_quote()
        return quote

if __name__ == '__main__':
    RandomQuotesApp().run()