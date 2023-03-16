from services.service_factory import ServiceFactory
from activity.activity_service_graphdb import ActivityServiceGraphDB
from activity_execution.activity_execution_service_graphdb import ActivityExecutionServiceGraphDB
from appearance.appearance_service_graphdb import AppearanceServiceGraphDB
from arrangement.arrangement_service_graphdb import ArrangementServiceGraphDB
from channel.channel_service_graphdb import ChannelServiceGraphDB
from experiment.experiment_service_graphdb import ExperimentServiceGraphDB
from life_activity.life_activity_service_graphdb import LifeActivityServiceGraphDB
from measure.measure_service_graphdb import MeasureServiceGraphDB
from measure_name.measure_name_service_graphdb import MeasureNameServiceGraphDB
from modality.modality_service_graphdb import ModalityServiceGraphDB
from observable_information.observable_information_service_graphdb import ObservableInformationServiceGraphDB
from participant.participant_service_graphdb import ParticipantServiceGraphDB
from participant_state.participant_state_service_graphdb import ParticipantStateServiceGraphDB
from participation.participation_service_graphdb import ParticipationServiceGraphDB
from personality.personality_service_graphdb import PersonalityServiceGraphDB
from recording.recording_service_graphdb import RecordingServiceGraphDB
from registered_channel.registered_channel_service_graphdb import RegisteredChannelServiceGraphDB
from registered_data.registered_data_service_graphdb import RegisteredDataServiceGraphDB
from scenario.scenario_service_graphdb import ScenarioServiceGraphDB
from time_series.time_series_service_graphdb import TimeSeriesServiceGraphDB
from activity.activity_service import ActivityService
from activity_execution.activity_execution_service import ActivityExecutionService
from appearance.appearance_service import AppearanceService
from arrangement.arrangement_service import ArrangementService
from channel.channel_service import ChannelService
from experiment.experiment_service import ExperimentService
from life_activity.life_activity_service import LifeActivityService
from measure.measure_service import MeasureService
from measure_name.measure_name_service import MeasureNameService
from modality.modality_service import ModalityService
from observable_information.observable_information_service import ObservableInformationService
from participant.participant_service import ParticipantService
from participant_state.participant_state_service import ParticipantStateService
from participation.participation_service import ParticipationService
from personality.personality_service import PersonalityService
from recording.recording_service import RecordingService
from registered_channel.registered_channel_service import RegisteredChannelService
from registered_data.registered_data_service import RegisteredDataService
from scenario.scenario_service import ScenarioService
from time_series.time_series_service import TimeSeriesService
from time_series.time_series_service_graphdb_with_signal_values import TimeSeriesServiceGraphDBWithSignalValues


class GraphServiceFactory(ServiceFactory):

    def get_activity_service(self) -> ActivityService:
        return ActivityServiceGraphDB(
            activity_execution_service=ActivityServiceGraphDB
        )

    def get_activity_execution_service(self) -> ActivityExecutionService:
        return ActivityExecutionServiceGraphDB(
            activity_service=ActivityServiceGraphDB,
            arrangement_service=ArrangementServiceGraphDB,
            scenario_service=ScenarioServiceGraphDB,
            experiment_service=ExperimentServiceGraphDB,
            participation_service=ParticipationServiceGraphDB
        )

    def get_appearance_service(self) -> AppearanceService:
        return AppearanceServiceGraphDB(
            participant_state_service=ParticipantStateServiceGraphDB
        )

    def get_arrangement_service(self) -> ArrangementService:
        return ArrangementServiceGraphDB(
            activity_execution_service=ActivityExecutionServiceGraphDB
        )

    def get_channel_service(self) -> ChannelService:
        return ChannelServiceGraphDB(
            registered_channel_service=RegisteredChannelServiceGraphDB)

    def get_experiment_service(self) -> ExperimentService:
        return ExperimentServiceGraphDB(
            activity_execution_service=ActivityExecutionServiceGraphDB
        )

    def get_life_activity_service(self) -> LifeActivityService:
        return LifeActivityServiceGraphDB(
            observable_information_service=ObservableInformationServiceGraphDB
        )

    def get_measure_service(self) -> MeasureService:
        return MeasureServiceGraphDB(
            measure_name_service=MeasureNameServiceGraphDB,
            time_series_service=TimeSeriesServiceGraphDB
        )

    def get_measure_name_service(self) -> MeasureNameService:
        return MeasureNameServiceGraphDB(
            measure_service=MeasureServiceGraphDB
        )

    def get_modality_service(self) -> ModalityService:
        return ModalityServiceGraphDB(
            observable_information_service=ObservableInformationServiceGraphDB
        )

    def get_observable_information_service(self) -> ObservableInformationService:
        return ObservableInformationServiceGraphDB(
            modality_service=ModalityServiceGraphDB,
            life_activity_service=LifeActivityServiceGraphDB,
            recording_service=RecordingServiceGraphDB,
            time_series_service=TimeSeriesServiceGraphDB
        )

    def get_participant_service(self) -> ParticipantService:
        return ParticipantServiceGraphDB(
            participant_state_service=ParticipantStateServiceGraphDB
        )

    def get_participant_state_service(self) -> ParticipantStateService:
        return ParticipantStateServiceGraphDB(
            participant_service=ParticipantStateServiceGraphDB,
            appearance_service=AppearanceServiceGraphDB,
            personality_service=PersonalityServiceGraphDB,
            participation_service=ParticipationServiceGraphDB
        )

    def get_participation_service(self) -> ParticipationService:
        return ParticipationServiceGraphDB(
            activity_execution_service=ActivityExecutionServiceGraphDB,
            participant_state_service=ParticipantStateServiceGraphDB,
            recording_service=RecordingServiceGraphDB
        )

    def get_personality_service(self) -> PersonalityService:
        return PersonalityServiceGraphDB(
            participant_state_service=ParticipantStateServiceGraphDB
        )

    def get_recording_service(self) -> RecordingService:
        return RecordingServiceGraphDB(
            participation_service=ParticipationServiceGraphDB,
            registered_channel_service=RegisteredChannelServiceGraphDB,
            observable_information_service=ObservableInformationServiceGraphDB
        )

    def get_registered_channel_service(self) -> RegisteredChannelService:
        return RegisteredChannelServiceGraphDB(
            channel_service=ChannelServiceGraphDB,
            registered_data_service=RegisteredDataServiceGraphDB,
            recording_service=RecordingServiceGraphDB
        )

    def get_registered_data_service(self) -> RegisteredDataService:
        return RegisteredDataServiceGraphDB(
            registered_channel_service=RegisteredChannelServiceGraphDB
        )

    def get_scenario_service(self) -> ScenarioService:
        return ScenarioServiceGraphDB(
            activity_execution_service=ActivityExecutionServiceGraphDB,
            experiment_service=ExperimentServiceGraphDB
        )

    def get_time_series_service(self) -> TimeSeriesService:
        return TimeSeriesServiceGraphDB(
            measure_service=MeasureServiceGraphDB,
            observable_information_service=ObservableInformationServiceGraphDB
        )


class GraphWithSignalValuesServiceFactory(GraphServiceFactory):
    def get_time_series_service(self) -> TimeSeriesService:
        return TimeSeriesServiceGraphDBWithSignalValues(
            measure_service=MeasureServiceGraphDB,
            observable_information_service=ObservableInformationServiceGraphDB
        )
