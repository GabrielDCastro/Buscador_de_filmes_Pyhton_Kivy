from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
import requests
import json

class Texto(App):
    def build(self):
        self.aimg = None  
        self.img_error = None
        self.box=FloatLayout()
        self.Img=Image(source='background.jpg', size_hint=(1,1), allow_stretch=True, keep_ratio=False, pos_hint=({"center_x":.5, "center_y":.5}))
        self.box.add_widget(self.Img)
        button=Button(text='Pesquisar',  pos_hint=({"center_x":.8, "center_y":.875}), size_hint=(.3, .10), font_size=30, on_release=self.incrementar)
        self.Img1=Image(source='lupa.png', allow_stretch=True, keep_ratio=False, size_hint=(.06,.06), pos_hint=({"center_x":.6, "center_y":.875}))
        self.box.add_widget(self.Img1)
        self.label = TextInput(font_size=20, size_hint=(.6, .10), pos_hint=({"center_x":.35, "center_y":.67}), disabled=True)
        self.label1 = TextInput(font_size=15, size_hint=(.6, .10), pos_hint=({"center_x":.35, "center_y":.55}), disabled=True)
        self.label2 = TextInput(font_size=20, size_hint=(.6, .10), pos_hint=({"center_x":.35, "center_y":.43}),  disabled=True)
        self.label3 = TextInput(font_size=20, size_hint=(.6, .10), pos_hint=({"center_x":.35, "center_y":.31}) ,disabled=True)
        self.label4 = TextInput(font_size=20, size_hint=(.6, .10), pos_hint=({"center_x":.35, "center_y":.19}) ,disabled=True)
        self.label5 = TextInput(font_size=20, size_hint=(.6, .10), pos_hint=({"center_x":.35, "center_y":.07}) ,disabled=True) 
        self.busca = TextInput(font_size=35, hint_text='Digite o nome do filme', size_hint=(.50, .10), pos_hint=({"center_x":.30, "center_y":.875}))
        self.box.add_widget(self.busca)
        self.box.add_widget(button)
        self.box.add_widget(self.label)
        self.box.add_widget(self.label1)
        self.box.add_widget(self.label2)
        self.box.add_widget(self.label3)
        self.box.add_widget(self.label4)
        self.box.add_widget(self.label5)
        
        return self.box

    def incrementar(self,button):
        if(len(self.busca.text) == 0):
            return
        
        filme = self.requisicao(self.busca.text)

        if not self.aimg == None:
            self.box.remove_widget(self.aimg)
        
        if filme['error_code'] == 1:
            texto_label = ('Filme nao encontrado')
            texto_label1 = ('')
            texto_label2 = ('')
            texto_label3 = ('') 
            texto_label4 = ('')
            texto_label5 = ('')

            self.label.text = texto_label
            self.label1.text = texto_label1
            self.label2.text = texto_label2
            self.label3.text = texto_label3
            self.label4.text = texto_label4
            self.label5.text = texto_label5
            error_url = "https://www.materialui.co/materialIcons/navigation/cancel_black_108x108.png"
        
            self.img_error = AsyncImage(source=error_url, pos_hint=({"center_y":.45, "center_x":.83}))

            self.box.add_widget(self.img_error)

            if not self.aimg == None:
                self.box.remove_widget(self.aimg)
            
            return

 
        else:
            nome = filme['data']['name']
            resumo = filme['data']['plot']
            ano = filme['data']['year']
            atores = filme['data']['stars']
            diretor = filme['data']['director']
            genero = filme['data']['genre']
            url = filme['data']['poster_url']
            
            texto_label = ('Filme: ') + nome
            texto_label1 = ('Sinopse: ') + resumo
            texto_label2 = ('Ano: ') + ano
            texto_label3 = ('Atores: ') + atores
            texto_label4 = ('Diretor: ') + diretor
            texto_label5 = ('Genero: ') + genero
            
            
            self.label.text = texto_label
            self.label1.text = texto_label1
            self.label2.text = texto_label2
            self.label3.text = texto_label3
            self.label4.text = texto_label4
            self.label5.text = texto_label5
            
            self.aimg = AsyncImage(source=url, pos_hint=({"center_y":.45, "center_x":.83}))

            self.box.add_widget(self.aimg)

            if not self.img_error == None:
                self.box.remove_widget(self.img_error)


    def requisicao(self, titulo):
        try:
            req = requests.get('http://theapache64.com/movie_db/search?keyword='+titulo)
            dicionario = json.loads(req.text)
            return dicionario
        except:
            print('Error na conexão')
        return None        
        
Texto().run()                      
    


