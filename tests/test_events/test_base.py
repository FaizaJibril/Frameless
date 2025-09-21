from unittest import TestCase
from fastapi.testclient import TestClient
from frameless.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('frameless', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertEqual(cm.output,
                             ['INFO:frameless:Starting up ...',
                              'INFO:frameless:Shutting down ...'])
