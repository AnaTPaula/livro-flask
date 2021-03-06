from flask_admin import Admin
from flask_admin.menu import MenuLink

from admin.views import UserView, HomeView, RoleView, CategoryView, ProductView
from model.category import Category
from model.product import Product
from model.role import Role
from model.user import User


def start_views(app, db):
    admin = Admin(app, name='Meu Estoque', base_template='admin/base.html', template_mode='bootstrap3',
                  index_view=HomeView())

    admin.add_view(RoleView(Role, db.session, "Funções", category="Usuários"))
    admin.add_view(UserView(User, db.session, "Usuários", category="Usuários"))
    admin.add_view(CategoryView(Category, db.session, 'Categorias', category="Produtos"))
    admin.add_view(ProductView(Product, db.session, "Produtos", category="Produtos"))
    admin.add_link(MenuLink(name='Logout', url='/logout'))
