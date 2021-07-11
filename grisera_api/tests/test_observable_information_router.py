from observable_information.observable_information_router import *
import unittest
import unittest.mock as mock
import asyncio


class TestObservableInformationRouter(unittest.TestCase):

    @mock.patch.object(ObservableInformationService, 'save_observable_information')
    def test_create_observable_information_without_error(self, save_observable_information_mock):
        save_observable_information_mock.return_value = ObservableInformationOut(modality='motion',
                                                                                 live_activity='sound', id=1)
        response = Response()
        observable_information = ObservableInformationIn(modality='motion', live_activity='sound')
        observable_information_router = ObservableInformationRouter()

        result = asyncio.run(observable_information_router.
                             create_observable_information(observable_information, response))

        self.assertEqual(result, ObservableInformationOut(modality='motion', live_activity='sound',
                                                          id=1, links=get_links(router)))
        save_observable_information_mock.assert_called_once_with(observable_information)
        self.assertEqual(response.status_code, 200)

    @mock.patch.object(ObservableInformationService, 'save_observable_information')
    def test_create_observable_information_with_error(self, save_observable_information_mock):
        save_observable_information_mock.return_value = ObservableInformationOut(modality='motion',
                                                                                 live_activity='sound',
                                                                                 errors={'errors': ['test']})
        response = Response()
        observable_information = ObservableInformationIn(modality='motion', live_activity='sound')
        observable_information_router = ObservableInformationRouter()

        result = asyncio.run(observable_information_router.
                             create_observable_information(observable_information, response))

        self.assertEqual(result, ObservableInformationOut(modality='motion', live_activity='sound',
                                                          errors={'errors': ['test']}, links=get_links(router)))
        save_observable_information_mock.assert_called_once_with(observable_information)
        self.assertEqual(response.status_code, 422)
