#Официальный сайт: http://www.riverbankcomputing.com/software/pyqt/download5
#PyQt4 является инструментом создания GUI приложений, представляет симбиоз языка Python и библиотеки Qt.

#Модули в PyQt4: 
#QtCore предназначен для работы со файлами, каталогами, временем, URL, типами данных, потоками, процессами. 
#QtGui хранит внутри себя графические компоненты и взаимодействующие с ними классы. (кнопки,  цвета, шрифты, окна, панели, изображения) 
#QtNetwork хранит классы сетевого программирования. Позволяет создать TCP/IP, UDP клиентские и серверные приложения. 
#QtSql хранит классы для работы с базами данных.
#QtXml хранит классы для работы с xml. 
#QtSvg хранит компоненты для работы с масштабируемой векторной графикой (SVG),(двумерная графикаи графическими приложениями XML).
#QtOpenGL предназначен для бесшовной интеграции QtGui и библиотеки OpenGL. 

#Подключаем библиотеки, необходимые для создания программы
import sys
from PyQt5 import QtCore, QtGui
 
#Обязательное создание экземпляра основного приложения и передача параметров командной строки
app = QtGui.QApplication(sys.argv)

#Создаем объект окна, который наследует nрактически все классы, реализующие комnоненты графического интерфейса.
widget = QtGui.QWidget()

#Изменяем размеры окна с помощью метода resize()
widget.resize(300, 150)

#Зададим заголовок программы
widget.setWindowTitle('MyProgramm')

#Создадим надпись(можно использовать теги HTML)
label = QtGui.QLabel("<center>Hello!</center>")

#Создадим кнопку и присвоем ей надпись
btn = QtGui.QPushButton("CloseWindow")

#Создадим контейнер, в который помести надпись и кнопку
box = QtGui.QVBoxLayout()
box.addWidget(label)
box.addWidget(btn)

#Добавим контейнер в основное окно
widget.setLayout(box)

#Обработчик сигнала, генерируемый nри нажатии кноnки.
#Аргументы: 
#btn - объект, генерируещий сигнал
#QtCore.SIGNAL("clicked()") - название сигнала
#QtGui.qApp - объект, nринимающий сигнал
#QtCore.SLOT("quit()") - метод объекта, который будет вызван nри вызове события
QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))

#Отобразим окно прогаммы с помощью метода show()
widget.show()

#Основной цикл обработки событий программы, получает и обрабатывает события окна системы, передает их виджетам. 
#По окончании работы основного цикла, программа закончит работу. sys.exit() передает информацию ОС об оканчании работы приложения.
sys.exit(app.exec_())