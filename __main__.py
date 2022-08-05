from controllers.base import Controller
from views.view import View

view = View()
controller = Controller(view)

controller.run()
