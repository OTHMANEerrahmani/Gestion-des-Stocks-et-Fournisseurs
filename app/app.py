import reflex as rx
from app.states.stock_state import StockState
from app.components.navbar import navbar
from app.components.product_modal import product_modal
from app.components.supplier_modal import supplier_modal
from app.components.stock_entry_modal import (
    stock_entry_modal,
)
from app.components.stock_exit_modal import stock_exit_modal
from app.components.dashboard_view import dashboard_view
from app.components.products_view import products_view
from app.components.suppliers_view import suppliers_view
from app.components.entries_view import entries_view
from app.components.exits_view import exits_view


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        rx.el.div(
            rx.match(
                StockState.current_view,
                ("dashboard", dashboard_view()),
                ("products", products_view()),
                ("suppliers", suppliers_view()),
                ("entries", entries_view()),
                ("exits", exits_view()),
                dashboard_view(),
            ),
            class_name="container mx-auto px-4",
        ),
        product_modal(),
        supplier_modal(),
        stock_entry_modal(),
        stock_exit_modal(),
        rx.toast.provider(),
        class_name="font-['Inter'] bg-gray-50 min-h-screen",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(
            rel="preconnect",
            href="https://fonts.googleapis.com",
        ),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            crossorigin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400..700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="Gestion de Stock")