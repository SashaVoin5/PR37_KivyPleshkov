from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', 'false')
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from random import randint

number_correct_answers=0
number_question=1
music = SoundLoader.load('Денис RiDer - Моя жизнь это - музыка (dizer.net).wav')


question_list = [['https://klike.net/uploads/posts/2020-09/1599373200_1.jpg', 'ЦСК', 'Спартак', 'Зенит', 'Ростов', 2],
              ['https://upload.wikimedia.org/wikipedia/ru/thumb/f/f4/FC_CSKA_Moscow_Logo.svg/1200px-FC_CSKA_Moscow_Logo.svg.png', 'ЦСК', 'Спартак', 'Зенит', 'Ростов', 1],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/FC_Zenit_1_star_2015_logo.svg/1200px-FC_Zenit_1_star_2015_logo.svg.png', 'Зенит', 'ЦСК', 'Спартак', 'Ростов', 1],
              ['https://upload.wikimedia.org/wikipedia/ru/thumb/c/c5/FC_Lokomotiv.png/200px-FC_Lokomotiv.png', 'Ростов', 'Спартак', 'ЦСК', 'Локомотив Москва', 4],
              ['https://upload.wikimedia.org/wikipedia/ru/thumb/2/24/FC_Barcelona.svg/1200px-FC_Barcelona.svg.png', 'Зенит', 'ЦСК', 'Бареселона', 'Ростов', 3],
              ['https://upload.wikimedia.org/wikipedia/ru/thumb/9/96/Manchester_City_FC.svg/1200px-Manchester_City_FC.svg.png', 'Манчестер Сити', 'Бареселона', 'Ростов', 'Спартак', 1],
              ['https://upload.wikimedia.org/wikipedia/ru/9/98/Real_Madrid.png', 'Бовария', 'Арсенал', 'Ливерпуль', 'Реал Мадрид',4],
              ['https://upload.wikimedia.org/wikipedia/ru/thumb/f/f7/FC_Chelsea_Logo.svg/1200px-FC_Chelsea_Logo.svg.png', 'Бареселона', 'Манчестер Сити', 'Челси', 'Спартак', 3],
              ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq3SSysXhkeIzeuOe8BD1tCcwkUUhHz38EzudTEFcxcGPfj_57V9HIhCcBeAvxIMO-eHA&usqp=CAU', 'Челси', 'Манчестер сити', 'Бавария', 'Спартак', 3],
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/2022_ACF_Fiorentina_logo.svg/200px-2022_ACF_Fiorentina_logo.svg.png', 'Фиорентина', 'Ювентус', 'Ливерпуль', 'Бовария',1],
              ['https://milanac.ru/wp-content/uploads/2021/03/ac-milan-logo-1.png', 'Ювентус', 'Ливерпуль', 'Бовария', 'Милан', 4], 
              ['https://footballfacts.ru/imageget.php?im=club/6885/324.png&size=s', 'Ювентус', 'Ганза', 'Ливерпуль', 'Милан', 2],#бРАК
              ['https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/FC_Internazionale_Milano_2021.svg/1200px-FC_Internazionale_Milano_2021.svg.png', 'ЦСК', 'Интер Милан', 'Ростов', 'Милан', 2],
              ['https://upload.wikimedia.org/wikipedia/ru/thumb/6/66/Valencia_Cf_Logo_original.png/191px-Valencia_Cf_Logo_original.png', 'Валенсия', 'Милан', 'Ливерпуль', 'Ростов', 1],
              ['https://upload.wikimedia.org/wikipedia/ru/thumb/b/be/SS_Lazio_logo.png/200px-SS_Lazio_logo.png', 'Честер', 'Ливерпуль', 'Лацио', 'Бовария', 3]]

class MainWidget(BoxLayout):
    def new_question(self):
        if(len(question_list)>0):
                       
            question = question_list[randint(0,len(question_list)-1)]           
            self.ids['img_question'].source = question[0]
            self.ids['btn_answer1'].text = question[1]
            self.ids['btn_answer2'].text = question[2]
            self.ids['btn_answer3'].text = question[3]
            self.ids['btn_answer4'].text = question[4]
        else:
            text = '\n Результат: ' + str(number_correct_answers) + ' из 15'            
            self.ids['lbl_question'].text = text
            self.remove_widget(self.ids['img_question'])
            self.remove_widget(self.ids['layout_btns'])

    def btn_pressed(self, number_button):
        question:list
        for i in question_list:
            if(i[0] == self.ids['img_question'].source):
               question = i
               break #Перебор списка, чтобы выбрать вопрос который выпал из списка
        global number_correct_answers
        global number_question
        if(number_button == question[5]):           
            number_correct_answers += 1
        else:          
              
            
            if music:
                print("Sound found at %s" % music.source)
                print("Sound is %.3f seconds" % music.length)
                music.play()
                   
        number_question+=1
        question_list.remove(question)
        self.new_question()     

class MainApp(App):
    def build(self):
        
        app = MainWidget()        
        app.new_question()
        return app

if __name__ == '__main__':
    MainApp().run()