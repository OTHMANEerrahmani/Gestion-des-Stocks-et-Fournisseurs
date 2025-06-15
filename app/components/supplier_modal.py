import reflex as rx
from app.states.stock_state import StockState


def supplier_modal() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            rx.el.h3(
                rx.cond(
                    StockState.supplier_id_edit,
                    "Modifier Fournisseur",
                    "Ajouter Fournisseur",
                ),
                class_name="text-lg font-semibold leading-6 text-gray-900 mb-4",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Nom du Fournisseur:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        default_value=StockState.supplier_name,
                        name="supplier_name",
                        placeholder="Ex: Agriculteurs Réunis",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Adresse:",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        default_value=StockState.supplier_address,
                        name="supplier_address",
                        placeholder="Ex: 123 Rue Principale, Ville",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Contact (Email/Téléphone):",
                        class_name="block text-sm font-medium text-gray-700",
                    ),
                    rx.el.input(
                        default_value=StockState.supplier_contact,
                        name="supplier_contact",
                        placeholder="Ex: contact@example.com / 0123456789",
                        class_name="mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm",
                    ),
                    class_name="mb-6",
                ),
                rx.el.div(
                    rx.el.button(
                        "Annuler",
                        on_click=StockState.toggle_supplier_modal(
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
                on_submit=StockState.save_supplier,
            ),
            class_name="bg-white p-6 rounded-lg shadow-xl w-full max-w-md mx-auto",
        ),
        open=StockState.show_supplier_modal,
        class_name="fixed inset-0 z-50 open:flex items-center justify-center p-4",
    )