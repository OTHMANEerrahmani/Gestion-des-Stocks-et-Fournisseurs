import reflex as rx
from typing import TypedDict, List, Optional
import uuid
import datetime


class Product(TypedDict):
    id: str
    name: str
    reference: str
    description: str
    quantity_in_stock: int
    critical_threshold: int
    expiration_date: str
    lot_number: str
    supplier_id: Optional[str]


class Supplier(TypedDict):
    id: str
    name: str
    address: str
    contact: str


class StockEntry(TypedDict):
    id: str
    product_id: str
    quantity: int
    date: str
    supplier_id: Optional[str]
    notes: str


class StockExit(TypedDict):
    id: str
    product_id: str
    quantity: int
    date: str
    destination: str
    notes: str


class StockState(rx.State):
    products: List[Product] = []
    suppliers: List[Supplier] = []
    stock_entries: List[StockEntry] = []
    stock_exits: List[StockExit] = []
    product_id_edit: str = ""
    product_name: str = ""
    product_reference: str = ""
    product_description: str = ""
    product_quantity_in_stock: str = "0"
    product_critical_threshold: str = "0"
    product_expiration_date: str = ""
    product_lot_number: str = ""
    product_supplier_id: str = ""
    supplier_id_edit: str = ""
    supplier_name: str = ""
    supplier_address: str = ""
    supplier_contact: str = ""
    entry_product_id: str = ""
    entry_quantity: str = "0"
    entry_date: str = ""
    entry_supplier_id: str = ""
    entry_notes: str = ""
    exit_product_id: str = ""
    exit_quantity: str = "0"
    exit_date: str = ""
    exit_destination: str = ""
    exit_notes: str = ""
    show_product_modal: bool = False
    show_supplier_modal: bool = False
    show_entry_modal: bool = False
    show_exit_modal: bool = False
    current_view: str = "dashboard"

    def _clear_product_form(self):
        self.product_id_edit = ""
        self.product_name = ""
        self.product_reference = ""
        self.product_description = ""
        self.product_quantity_in_stock = "0"
        self.product_critical_threshold = "0"
        self.product_expiration_date = ""
        self.product_lot_number = ""
        self.product_supplier_id = ""

    @rx.event
    def toggle_product_modal(
        self, product_id: Optional[str] = None
    ):
        self.show_product_modal = (
            not self.show_product_modal
        )
        if self.show_product_modal and product_id:
            product = next(
                (
                    p
                    for p in self.products
                    if p["id"] == product_id
                ),
                None,
            )
            if product:
                self.product_id_edit = product["id"]
                self.product_name = product["name"]
                self.product_reference = product[
                    "reference"
                ]
                self.product_description = product[
                    "description"
                ]
                self.product_quantity_in_stock = str(
                    product["quantity_in_stock"]
                )
                self.product_critical_threshold = str(
                    product["critical_threshold"]
                )
                self.product_expiration_date = product[
                    "expiration_date"
                ]
                self.product_lot_number = product[
                    "lot_number"
                ]
                self.product_supplier_id = (
                    product["supplier_id"] or ""
                )
        elif not self.show_product_modal:
            self._clear_product_form()

    @rx.event
    def save_product(self, form_data: dict):
        name = form_data.get("product_name", "")
        reference = form_data.get("product_reference", "")
        description = form_data.get(
            "product_description", ""
        )
        quantity_in_stock_str = form_data.get(
            "product_quantity_in_stock", "0"
        )
        critical_threshold_str = form_data.get(
            "product_critical_threshold", "0"
        )
        expiration_date = form_data.get(
            "product_expiration_date", ""
        )
        lot_number = form_data.get("product_lot_number", "")
        supplier_id = form_data.get(
            "product_supplier_id", ""
        )
        if not name or not reference:
            return rx.toast(
                "Product name and reference are required.",
                duration=3000,
            )
        try:
            quantity = int(quantity_in_stock_str)
            threshold = int(critical_threshold_str)
        except ValueError:
            return rx.toast(
                "Quantity and threshold must be numbers.",
                duration=3000,
            )
        supplier_id_to_save = (
            supplier_id if supplier_id else None
        )
        if self.product_id_edit:
            product_index = next(
                (
                    i
                    for i, p in enumerate(self.products)
                    if p["id"] == self.product_id_edit
                ),
                -1,
            )
            if product_index != -1:
                self.products[product_index] = {
                    "id": self.product_id_edit,
                    "name": name,
                    "reference": reference,
                    "description": description,
                    "quantity_in_stock": quantity,
                    "critical_threshold": threshold,
                    "expiration_date": expiration_date,
                    "lot_number": lot_number,
                    "supplier_id": supplier_id_to_save,
                }
        else:
            new_product: Product = {
                "id": str(uuid.uuid4()),
                "name": name,
                "reference": reference,
                "description": description,
                "quantity_in_stock": quantity,
                "critical_threshold": threshold,
                "expiration_date": expiration_date,
                "lot_number": lot_number,
                "supplier_id": supplier_id_to_save,
            }
            self.products.append(new_product)
        self._clear_product_form()
        self.show_product_modal = False
        return rx.toast(
            "Product saved successfully.", duration=3000
        )

    @rx.event
    def delete_product(self, product_id: str):
        self.products = [
            p
            for p in self.products
            if p["id"] != product_id
        ]
        return rx.toast("Product deleted.", duration=3000)

    def _clear_supplier_form(self):
        self.supplier_id_edit = ""
        self.supplier_name = ""
        self.supplier_address = ""
        self.supplier_contact = ""

    @rx.event
    def toggle_supplier_modal(
        self, supplier_id: Optional[str] = None
    ):
        self.show_supplier_modal = (
            not self.show_supplier_modal
        )
        if self.show_supplier_modal and supplier_id:
            supplier = next(
                (
                    s
                    for s in self.suppliers
                    if s["id"] == supplier_id
                ),
                None,
            )
            if supplier:
                self.supplier_id_edit = supplier["id"]
                self.supplier_name = supplier["name"]
                self.supplier_address = supplier["address"]
                self.supplier_contact = supplier["contact"]
        elif not self.show_supplier_modal:
            self._clear_supplier_form()

    @rx.event
    def save_supplier(self, form_data: dict):
        name = form_data.get("supplier_name", "")
        address = form_data.get("supplier_address", "")
        contact = form_data.get("supplier_contact", "")
        if not name:
            return rx.toast(
                "Supplier name is required.", duration=3000
            )
        if self.supplier_id_edit:
            supplier_index = next(
                (
                    i
                    for i, s in enumerate(self.suppliers)
                    if s["id"] == self.supplier_id_edit
                ),
                -1,
            )
            if supplier_index != -1:
                self.suppliers[supplier_index] = {
                    "id": self.supplier_id_edit,
                    "name": name,
                    "address": address,
                    "contact": contact,
                }
        else:
            new_supplier: Supplier = {
                "id": str(uuid.uuid4()),
                "name": name,
                "address": address,
                "contact": contact,
            }
            self.suppliers.append(new_supplier)
        self._clear_supplier_form()
        self.show_supplier_modal = False
        return rx.toast(
            "Supplier saved successfully.", duration=3000
        )

    @rx.event
    def delete_supplier(self, supplier_id: str):
        for i, product in enumerate(self.products):
            if product["supplier_id"] == supplier_id:
                self.products[i]["supplier_id"] = None
        self.suppliers = [
            s
            for s in self.suppliers
            if s["id"] != supplier_id
        ]
        return rx.toast("Supplier deleted.", duration=3000)

    def _clear_entry_form(self):
        self.entry_product_id = ""
        self.entry_quantity = "0"
        self.entry_date = ""
        self.entry_supplier_id = ""
        self.entry_notes = ""

    @rx.event
    def toggle_entry_modal(self):
        self.show_entry_modal = not self.show_entry_modal
        if not self.show_entry_modal:
            self._clear_entry_form()
        else:
            self.entry_date = (
                datetime.date.today().isoformat()
            )

    @rx.event
    def save_stock_entry(self, form_data: dict):
        product_id = form_data.get("entry_product_id", "")
        quantity_str = form_data.get("entry_quantity", "0")
        date = form_data.get("entry_date", "")
        supplier_id = form_data.get("entry_supplier_id", "")
        notes = form_data.get("entry_notes", "")
        if not product_id or not quantity_str or (not date):
            return rx.toast(
                "Product, quantity, and date are required for stock entry.",
                duration=3000,
            )
        try:
            quantity = int(quantity_str)
            if quantity <= 0:
                return rx.toast(
                    "Quantity must be positive.",
                    duration=3000,
                )
        except ValueError:
            return rx.toast(
                "Quantity must be a number.", duration=3000
            )
        product_index = next(
            (
                i
                for i, p in enumerate(self.products)
                if p["id"] == product_id
            ),
            -1,
        )
        if product_index == -1:
            return rx.toast(
                "Selected product not found.", duration=3000
            )
        new_entry: StockEntry = {
            "id": str(uuid.uuid4()),
            "product_id": product_id,
            "quantity": quantity,
            "date": date,
            "supplier_id": (
                supplier_id if supplier_id else None
            ),
            "notes": notes,
        }
        self.stock_entries.append(new_entry)
        self.products[product_index][
            "quantity_in_stock"
        ] += quantity
        self._clear_entry_form()
        self.show_entry_modal = False
        return rx.toast(
            "Stock entry recorded.", duration=3000
        )

    def _clear_exit_form(self):
        self.exit_product_id = ""
        self.exit_quantity = "0"
        self.exit_date = ""
        self.exit_destination = ""
        self.exit_notes = ""

    @rx.event
    def toggle_exit_modal(self):
        self.show_exit_modal = not self.show_exit_modal
        if not self.show_exit_modal:
            self._clear_exit_form()
        else:
            self.exit_date = (
                datetime.date.today().isoformat()
            )

    @rx.event
    def save_stock_exit(self, form_data: dict):
        product_id = form_data.get("exit_product_id", "")
        quantity_str = form_data.get("exit_quantity", "0")
        date = form_data.get("exit_date", "")
        destination = form_data.get("exit_destination", "")
        notes = form_data.get("exit_notes", "")
        if (
            not product_id
            or not quantity_str
            or (not date)
            or (not destination)
        ):
            return rx.toast(
                "Product, quantity, date, and destination are required for stock exit.",
                duration=3000,
            )
        try:
            quantity = int(quantity_str)
            if quantity <= 0:
                return rx.toast(
                    "Quantity must be positive.",
                    duration=3000,
                )
        except ValueError:
            return rx.toast(
                "Quantity must be a number.", duration=3000
            )
        product_index = next(
            (
                i
                for i, p in enumerate(self.products)
                if p["id"] == product_id
            ),
            -1,
        )
        if product_index == -1:
            return rx.toast(
                "Selected product not found.", duration=3000
            )
        if (
            self.products[product_index][
                "quantity_in_stock"
            ]
            < quantity
        ):
            return rx.toast(
                f"Not enough stock for {self.products[product_index]['name']}. Available: {self.products[product_index]['quantity_in_stock']}",
                duration=4000,
            )
        new_exit: StockExit = {
            "id": str(uuid.uuid4()),
            "product_id": product_id,
            "quantity": quantity,
            "date": date,
            "destination": destination,
            "notes": notes,
        }
        self.stock_exits.append(new_exit)
        self.products[product_index][
            "quantity_in_stock"
        ] -= quantity
        if (
            self.products[product_index][
                "quantity_in_stock"
            ]
            <= self.products[product_index][
                "critical_threshold"
            ]
        ):
            yield rx.toast(
                f"Warning: Stock for {self.products[product_index]['name']} is at or below critical threshold ({self.products[product_index]['critical_threshold']}). Current: {self.products[product_index]['quantity_in_stock']}",
                duration=5000,
            )
        self._clear_exit_form()
        self.show_exit_modal = False
        return rx.toast(
            "Stock exit recorded.", duration=3000
        )

    @rx.event
    def set_view(self, view_name: str):
        self.current_view = view_name

    @rx.var
    def products_with_supplier_names(self) -> List[dict]:
        return [
            {
                **p,
                "supplier_name": (
                    next(
                        (
                            s["name"]
                            for s in self.suppliers
                            if s["id"] == p["supplier_id"]
                        ),
                        "N/A",
                    )
                    if p["supplier_id"]
                    else "N/A"
                ),
                "is_critical": p["quantity_in_stock"]
                <= p["critical_threshold"],
            }
            for p in self.products
        ]

    @rx.var
    def stock_entries_with_details(self) -> List[dict]:
        return [
            {
                **e,
                "product_name": next(
                    (
                        p["name"]
                        for p in self.products
                        if p["id"] == e["product_id"]
                    ),
                    "N/A",
                ),
                "supplier_name": (
                    next(
                        (
                            s["name"]
                            for s in self.suppliers
                            if s["id"] == e["supplier_id"]
                        ),
                        "N/A",
                    )
                    if e["supplier_id"]
                    else "N/A"
                ),
            }
            for e in self.stock_entries
        ]

    @rx.var
    def stock_exits_with_details(self) -> List[dict]:
        return [
            {
                **e,
                "product_name": next(
                    (
                        p["name"]
                        for p in self.products
                        if p["id"] == e["product_id"]
                    ),
                    "N/A",
                ),
            }
            for e in self.stock_exits
        ]

    @rx.var
    def total_stock_value(self) -> float:
        return sum(
            (p["quantity_in_stock"] for p in self.products)
        )

    @rx.var
    def critical_stock_products(self) -> List[Product]:
        return [
            p
            for p in self.products
            if p["quantity_in_stock"]
            <= p["critical_threshold"]
        ]

    @rx.var
    def product_options_for_select(
        self,
    ) -> list[tuple[str, str]]:
        return [(p["name"], p["id"]) for p in self.products]

    @rx.var
    def supplier_options_for_select(
        self,
    ) -> list[tuple[str, str]]:
        return [
            (s["name"], s["id"]) for s in self.suppliers
        ]