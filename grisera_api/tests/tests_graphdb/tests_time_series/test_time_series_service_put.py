import unittest
import unittest.mock as mock

from time_series.time_series_model import *
from models.not_found_model import *

from time_series.time_series_service_graphdb import TimeSeriesServiceGraphDB
from graph_api_service import GraphApiService


class TestTimeSeriesServicePut(unittest.TestCase):

    @mock.patch.object(GraphApiService, 'create_properties')
    @mock.patch.object(GraphApiService, 'get_node')
    @mock.patch.object(GraphApiService, 'delete_node_properties')
    @mock.patch.object(GraphApiService, 'get_node_relationships')
    def test_update_time_series_without_error(self, get_node_relationships_mock, delete_node_properties_mock,
                                                    get_node_mock, create_properties_mock):
        database_name = "neo4j"
        id_node = 1
        create_properties_mock.return_value = {}
        delete_node_properties_mock.return_value = {}
        get_node_relationships_mock.return_value = {"relationships": [
                                                    {"start_node": id_node, "end_node": 19,
                                                     "name": "testRelation", "id": 0,
                                                     "properties": None},
                                                    {"start_node": 15, "end_node": id_node,
                                                     "name": "testReversedRelation", "id": 0,
                                                     "properties": None}]}
        get_node_mock.return_value = {'id': id_node, 'labels': ['Time Series'],
                                      'properties': [{'key': 'type', 'value': "Epoch"},
                                                                                     {'key': 'source', 'value': "cos"}, {'key': 'identifier', 'value': 5}],
                                      "errors": None, 'links': None}
        additional_properties = [PropertyIn(key='identifier', value=5)]
        time_series_in = TimeSeriesPropertyIn(type="Epoch", source="cos", additional_properties=additional_properties)
        time_series_out = TimeSeriesOut(type="Epoch", source="cos", id=id_node, relations=
                                 [RelationInformation(second_node_id=19, name="testRelation", relation_id=0)],
                                                    reversed_relations=
                                 [RelationInformation(second_node_id=15, name="testReversedRelation", relation_id=0)],
                                 additional_properties=additional_properties)
        calls = [mock.call(1, database_name)]
        time_series_service = TimeSeriesServiceGraphDB()

        result = time_series_service.update_time_series(id_node, time_series_in, database_name)

        self.assertEqual(result, time_series_out)
        get_node_mock.assert_has_calls(calls)
        create_properties_mock.assert_called_once_with(id_node, time_series_in, database_name)
        get_node_relationships_mock.assert_called_once_with(id_node, database_name)

    @mock.patch.object(GraphApiService, 'get_node')
    def test_update_time_series_without_label(self, get_node_mock):
        database_name = "neo4j"
        id_node = 1
        get_node_mock.return_value = {'id': id_node, 'labels': ['Test'], 'properties': None,
                                      "errors": None, 'links': None}
        not_found = NotFoundByIdModel(id=id_node, errors="Node not found.")
        additional_properties = [PropertyIn(key='identifier', value=5)]
        time_series_in = TimeSeriesPropertyIn(type="Epoch", source="cos", additional_properties=additional_properties)
        time_series_service = TimeSeriesServiceGraphDB()

        result = time_series_service.update_time_series(id_node, time_series_in, database_name)

        self.assertEqual(result, not_found)
        get_node_mock.assert_called_once_with(id_node, database_name)

    @mock.patch.object(GraphApiService, 'get_node')
    def test_update_time_series_with_error(self, get_node_mock):
        database_name = "neo4j"
        id_node = 1
        get_node_mock.return_value = {'id': id_node, 'errors': ['error'], 'links': None}
        not_found = NotFoundByIdModel(id=id_node, errors=['error'])
        additional_properties = [PropertyIn(key='identifier', value=5)]
        time_series_in = TimeSeriesPropertyIn(type="Epoch", source="cos", id=id_node, additional_properties=additional_properties)
        time_series_service = TimeSeriesServiceGraphDB()

        result = time_series_service.update_time_series(id_node, time_series_in, database_name)

        self.assertEqual(result, not_found)
        get_node_mock.assert_called_once_with(id_node, database_name)
