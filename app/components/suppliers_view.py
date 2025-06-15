import reflex as rx
from app.states.stock_state import StockState


def suppliers_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Gestion des Fournisseurs",
                class_name="text-2xl font-semibold text-gray-800",
            ),
            rx.el.button(
                rx.icon("plus", class_name="mr-2"),
                "Ajouter Fournisseur",
                on_click=StockState.toggle_supplier_modal(
                    None
                ),
                class_name="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 flex items-center",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Nom",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Adresse",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Contact",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        StockState.suppliers,
                        lambda supplier: rx.el.tr(
                            rx.el.td(
                                supplier["name"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
                            ),
                            rx.el.td(
                                supplier["address"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                supplier["contact"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                rx.el.button(
                                    rx.icon(
                                        "pencil",
                                        class_name="h-4 w-4",
                                    ),
                                    on_click=StockState.toggle_supplier_modal(
                                        supplier["id"]
                                    ),
                                    class_name="text-blue-600 hover:text-blue-900 mr-2 p-1 rounded hover:bg-blue-100",
                                ),
                                rx.el.button(
                                    rx.icon(
                                        "trash-2",
                                        class_name="h-4 w-4",
                                    ),
                                    on_click=StockState.delete_supplier(
                                        supplier["id"]
                                    ),
                                    class_name="text-red-600 hover:text-red-900 p-1 rounded hover:bg-red-100",
                                ),
                                class_name="px-6 py-4 whitespace-nowrap text-sm font-medium",
                            ),
                            class_name="hover:bg-gray-50",
                        ),
                    ),
                    class_name="bg-white divide-y divide-gray-200",
                ),
                class_name="min-w-full divide-y divide-gray-200 shadow border-b border-gray-200 sm:rounded-lg",
            ),
            class_name="overflow-x-auto",
        ),
        class_name="p-6",
    )