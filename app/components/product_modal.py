import reflex as rx
from app.states.stock_state import StockState


def product_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            rx.el.h3(
                rx.cond(
                    StockState.product_id_edit,
                    "Modifier Produit",
                    "Ajouter Produit",
                ),
                class_name="text-lg font-semibold leading-6 text-gray-900 mb-4",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Nom du Produit:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        default_value=StockState.product_name,
                        name="product_name",
                        placeholder="Ex: Tomates",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Référence:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        default_value=StockState.product_reference,
                        name="product_reference",
                        placeholder="Ex: TOM001",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Description:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        default_value=StockState.product_description,
                        name="product_description",
                        placeholder="Ex: Tomates cerises bio",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Quantité en Stock:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        type="number",
                        default_value=StockState.product_quantity_in_stock,
                        name="product_quantity_in_stock",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Seuil Critique:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        type="number",
                        default_value=StockState.product_critical_threshold,
                        name="product_critical_threshold",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Date de Péremption:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        type="date",
                        default_value=StockState.product_expiration_date,
                        name="product_expiration_date",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Numéro de Lot:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        default_value=StockState.product_lot_number,
                        name="product_lot_number",
                        placeholder="Ex: LOT2024A",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Fournisseur:",
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
                        default_value=StockState.product_supplier_id,
                        name="product_supplier_id",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-6",
                ),
                rx.el.div(
                    rx.el.button(
                        "Annuler",
                        on_click=StockState.toggle_product_modal(
                            None
                        ),
                        type="button",
                        class_name="mr-2 px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500",
                    ),
                    rx.el.button(
                        "Sauvegarder",
                        type="submit",
                        class_name="px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500",
                    ),
                    class_name="flex justify-end",
                ),
                on_submit=StockState.save_product,
            ),
            class_name="bg-white p-6 rounded-lg shadow-xl w-full max-w-md mx-auto",
        ),
        open=StockState.show_product_modal,
        class_name="fixed inset-0 z-50 open:flex items-center justify-center p-4",
    )