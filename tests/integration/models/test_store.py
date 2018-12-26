from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest

class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store=StoreModel("Test")
        self.assertListEqual(store.items.all(), [], "Store's items length is not 0 even when no items were added to it")
    def test_crud(self):
        with self.app_context():
            store=StoreModel("Test")
            self.assertIsNone(StoreModel.find_by_name("Test"))
            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name("Test"))
            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name("Test"))
    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel("Test")
            item = ItemModel("Test_item", 19.99, 1)
            store.save_to_db()
            item.save_to_db()
            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, "Test_item")
    def test_store_json(self):
        store=StoreModel("Test")
        expected= {

            'id': None,
            'name': "test",
            'items': []
        }
        self.assertDictEqual(store.json(), expected)
    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel("Test")
            item = ItemModel("Test_item", 17, 1)
            store.save_to_db()
            item.save_to_db()
            expected = {
                "id": 1,
                "name": "Test",
                "items": [{"name": "Test_item", "price": 17}]
            }
            self.assertDictEqual(store.json(), expected)

