import reflex as rx
from app.states.stock_state import StockState


def stat_card(
    title: str,
    value: rx.Var[str | int | float],
    icon: str,
    color_class: str,
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                icon, class_name=f"h-8 w-8 {color_class}"
            ),
            class_name="p-3 bg-gray-100 rounded-full",
        ),
        rx.el.div(
            rx.el.p(
                title,
                class_name="text-sm font-medium text-gray-500",
            ),
            rx.el.p(
                value,
                class_name="text-2xl font-semibold text-gray-900",
            ),
            class_name="ml-4",
        ),
        class_name="bg-white p-6 rounded-lg shadow-md flex items-center",
    )


def dashboard_view() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Tableau de Bord",
            class_name="text-2xl font-semibold text-gray-800 mb-6",
        ),
        rx.el.div(
            stat_card(
                "Total Produits",
                StockState.products.length(),
                "package",
                "text-blue-500",
            ),
            stat_card(
                "Total Fournisseurs",
                StockState.suppliers.length(),
                "truck",
                "text-green-500",
            ),
            stat_card(
                "Total Articles en Stock",
                StockState.total_stock_value.to_string(),
                "archive",
                "text-indigo-500",
            ),
            stat_card(
                "Produits en Seuil Critique",
                StockState.critical_stock_products.length(),
                "badge_alert",
                "text-red-500",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.h3(
            "Produits en Seuil Critique",
            class_name="text-xl font-semibold text-gray-800 mb-4",
        ),
        rx.cond(
            StockState.critical_stock_products.length() > 0,
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
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(
                            StockState.critical_stock_products,
                            lambda product: rx.el.tr(
                                rx.el.td(
                                    product["name"],
                                    class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-700",
                                ),
                                rx.el.td(
                                    product["reference"],
                                    class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-700",
                                ),
                                rx.el.td(
                                    product[
                                        "quantity_in_stock"
                                    ],
                                    class_name="px-6 py-4 whitespace-nowrap text-sm font-bold text-red-600",
                                ),
                                rx.el.td(
                                    product[
                                        "critical_threshold"
                                    ],
                                    class_name="px-6 py-4 whitespace-nowrap text-sm text-gray-700",
                                ),
                                class_name="bg-red-50 hover:bg-red-100",
                            ),
                        ),
                        class_name="bg-white divide-y divide-gray-200",
                    ),
                    class_name="min-w-full divide-y divide-gray-200 shadow border-b border-gray-200 sm:rounded-lg",
                ),
                class_name="overflow-x-auto",
            ),
            rx.el.p(
                "Aucun produit en seuil critique.",
                class_name="text-gray-600",
            ),
        ),
        class_name="p-6",
    )