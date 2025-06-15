import reflex as rx
from app.states.stock_state import StockState


def stock_exit_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            rx.el.h3(
                "Nouvelle Sortie de Stock",
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
                        default_value=StockState.exit_product_id,
                        name="exit_product_id",
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
                        default_value=StockState.exit_quantity,
                        name="exit_quantity",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Date de Sortie:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        type="date",
                        default_value=StockState.exit_date,
                        name="exit_date",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Destination/Service:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        default_value=StockState.exit_destination,
                        name="exit_destination",
                        placeholder="Ex: Cuisine / Client XYZ",
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
                        default_value=StockState.exit_notes,
                        name="exit_notes",
                        placeholder="Ex: Vente promotionnelle",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-6",
                ),
                rx.el.div(
                    rx.el.button(
                        "Annuler",
                        on_click=StockState.toggle_exit_modal,
                        type="button",
                        class_name="mr-2 px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500",
                    ),
                    rx.el.button(
                        "Enregistrer Sortie",
                        type="submit",
                        class_name="px-4 py-2 text-sm font-medium text-white bg-red-600 border border-transparent rounded-md shadow-sm hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500",
                    ),
                    class_name="flex justify-end",
                ),
                on_submit=StockState.save_stock_exit,
            ),
            class_name="bg-white p-6 rounded-lg shadow-xl w-full max-w-md mx-auto",
        ),
        open=StockState.show_exit_modal,
        class_name="fixed inset-0 z-50 open:flex items-center justify-center p-4",
    )