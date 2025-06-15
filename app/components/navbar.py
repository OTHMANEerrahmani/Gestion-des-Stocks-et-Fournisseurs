import reflex as rx
from app.states.stock_state import StockState


def navbar_link(text: str, view_name: str) -> rx.Component:
    return rx.el.button(
        text,
        on_click=lambda: StockState.set_view(view_name),
        class_name=rx.cond(
            StockState.current_view == view_name,
            "px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md shadow-sm hover:bg-blue-700",
            "px-4 py-2 text-sm font-medium text-gray-700 bg-white rounded-md shadow-sm hover:bg-gray-50 border border-gray-300",
        ),
    )


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            navbar_link("Dashboard", "dashboard"),
            navbar_link("Produits", "products"),
            navbar_link("Fournisseurs", "suppliers"),
            navbar_link("Entrées de Stock", "entries"),
            navbar_link("Sorties de Stock", "exits"),
            class_name="flex space-x-4",
        ),
        class_name="bg-gray-100 p-4 shadow-md mb-6",
    )