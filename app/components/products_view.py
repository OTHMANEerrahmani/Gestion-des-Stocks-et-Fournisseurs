import reflex as rx
from app.states.stock_state import StockState


def products_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Gestion des Produits",
                class_name="text-2xl font-semibold text-gray-800",
            ),
            rx.el.button(
                rx.icon("plus", class_name="mr-2"),
                "Ajouter Produit",
                on_click=StockState.toggle_product_modal(
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
                            "Référence",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Quantité",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Seuil Critique",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Fournisseur",
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
                        StockState.products_with_supplier_names,
                        lambda product: rx.el.tr(
                            rx.el.td(
                                product["name"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
                            ),
                            rx.el.td(
                                product["reference"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                product[
                                    "quantity_in_stock"
                                ],
                                class_name=rx.cond(
                                    product["is_critical"],
                                    "px-6 py-4 whitespace-nowrap text-sm font-bold text-red-600",
                                    "px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                                ),
                            ),
                            rx.el.td(
                                product[
                                    "critical_threshold"
                                ],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                product["supplier_name"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                rx.el.button(
                                    rx.icon(
                                        "pencil",
                                        class_name="h-4 w-4",
                                    ),
                                    on_click=StockState.toggle_product_modal(
                                        product["id"]
                                    ),
                                    class_name="text-blue-600 hover:text-blue-900 mr-2 p-1 rounded hover:bg-blue-100",
                                ),
                                rx.el.button(
                                    rx.icon(
                                        "trash-2",
                                        class_name="h-4 w-4",
                                    ),
                                    on_click=StockState.delete_product(
                                        product["id"]
                                    ),
                                    class_name="text-red-600 hover:text-red-900 p-1 rounded hover:bg-red-100",
                                ),
                                class_name="px-6 py-4 whitespace-nowrap text-sm font-medium",
                            ),
                            class_name=rx.cond(
                                product["is_critical"],
                                "bg-red-50 hover:bg-red-100",
                                "hover:bg-gray-50",
                            ),
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