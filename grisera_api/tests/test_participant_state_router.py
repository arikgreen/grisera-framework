from participant_state.participant_state_router import *
from participant.participant_model import ParticipantIn
import unittest
import unittest.mock as mock
import asyncio


class TestParticipantStateRouter(unittest.TestCase):

    @mock.patch.object(ParticipantStateService, 'save_participant_state')
    def test_create_participant_state_without_error(self, save_participant_state_mock):
        save_participant_state_mock.return_value = ParticipantStateOut(
            participant=ParticipantIn(sex='male', identifier=5), id=1)
        response = Response()
        participant_state = ParticipantStateIn(participant=ParticipantIn(sex='male', identifier=5))
        participant_state_router = ParticipantStateRouter()

        result = asyncio.run(participant_state_router.create_participant_state(participant_state, response))

        self.assertEqual(result, ParticipantStateOut(participant=ParticipantIn(sex='male', identifier=5),
                                                     id=1, links=get_links(router)))
        save_participant_state_mock.assert_called_once_with(participant_state)
        self.assertEqual(response.status_code, 200)

    @mock.patch.object(ParticipantStateService, 'save_participant_state')
    def test_create_participant_state_with_error(self, save_participant_state_mock):
        save_participant_state_mock.return_value = ParticipantStateOut(
            participant=ParticipantIn(sex='male', identifier=5), errors={'errors': ['test']})
        response = Response()
        participant_state = ParticipantStateIn(participant=ParticipantIn(sex='male', identifier=5))
        participant_state_router = ParticipantStateRouter()

        result = asyncio.run(participant_state_router.create_participant_state(participant_state, response))

        self.assertEqual(result, ParticipantStateOut(participant=ParticipantIn(sex='male', identifier=5),
                                                     errors={'errors': ['test']}, links=get_links(router)))
        save_participant_state_mock.assert_called_once_with(participant_state)
        self.assertEqual(response.status_code, 422)
