import reflex as rx
from app.states.stock_state import StockState


def stock_entry_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            rx.el.h3(
                "Nouvelle Entrée de Stock",
                class_name="text-lg font-semibold leading-6 text-gray-900 mb-4",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Produit:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.select(
                        rx.el.option(
                            "Sélectionner Produit", value=""
                        ),
                        rx.foreach(
                            StockState.product_options_for_select,
                            lambda option: rx.el.option(
                                option[0], value=option[1]
                            ),
                        ),
                        default_value=StockState.entry_product_id,
                        name="entry_product_id",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Quantité:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        type="number",
                        default_value=StockState.entry_quantity,
                        name="entry_quantity",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Date d'Entrée:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        type="date",
                        default_value=StockState.entry_date,
                        name="entry_date",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Fournisseur (Optionnel):",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.select(
                        rx.el.option(
                            "Sélectionner Fournisseur",
                            value="",
                        ),
                        rx.foreach(
                            StockState.supplier_options_for_select,
                            lambda option: rx.el.option(
                                option[0], value=option[1]
                            ),
                        ),
                        default_value=StockState.entry_supplier_id,
                        name="entry_supplier_id",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Notes (Optionnel):",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        default_value=StockState.entry_notes,
                        name="entry_notes",
                        placeholder="Ex: Réception commande #123",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-6",
                ),
                rx.el.div(
                    rx.el.button(
                        "Annuler",
                        on_click=StockState.toggle_entry_modal,
                        type="button",
                        class_name="mr-2 px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500",
                    ),
                    rx.el.button(
                        "Enregistrer Entrée",
                        type="submit",
                        class_name="px-4 py-2 text-sm font-medium text-white bg-green-600 border border-transparent rounded-md shadow-sm hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500",
                    ),
                    class_name="flex justify-end",
                ),
                on_submit=StockState.save_stock_entry,
            ),
            class_name="bg-white p-6 rounded-lg shadow-xl w-full max-w-md mx-auto",
        ),
        open=StockState.show_entry_modal,
        class_name="fixed inset-0 z-50 open:flex items-center justify-center p-4",
    )