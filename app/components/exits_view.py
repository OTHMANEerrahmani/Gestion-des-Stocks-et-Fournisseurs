import reflex as rx
from app.states.stock_state import StockState


def exits_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                "Sorties de Stock",
                class_name="text-2xl font-semibold text-gray-800",
            ),
            rx.el.button(
                rx.icon("minus", class_name="mr-2"),
                "Nouvelle Sortie",
                on_click=StockState.toggle_exit_modal,
                class_name="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 flex items-center",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Date",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Produit",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Quantité",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Destination",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Notes",
                            class_name="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
                        ),
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        StockState.stock_exits_with_details,
                        lambda exit_item: rx.el.tr(
                            rx.el.td(
                                exit_item["date"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                exit_item["product_name"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900",
                            ),
                            rx.el.td(
                                exit_item["quantity"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                exit_item["destination"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
                            ),
                            rx.el.td(
                                exit_item["notes"],
                                class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-500",
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