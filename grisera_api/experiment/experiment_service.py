from graph_api_service import GraphApiService
from experiment.experiment_model import ExperimentIn, ExperimentOut
from author.author_service import AuthorService, AuthorOut
from publication.publication_service import PublicationService


class ExperimentService:
    """
    Object to handle logic of experiments requests

    Attributes:
        graph_api_service (GraphApiService): Service used to communicate with Graph API
        author_service (AuthorService): Service used to communicate with Author
        publication_service (PublicationService): Service used to communicate with Publication
    """
    graph_api_service = GraphApiService()
    author_service = AuthorService()
    publication_service = PublicationService()
    
    def save_experiment(self, experiment: ExperimentIn):
        """
        Send request to graph api to create new experiment

        Args:
            experiment (ExperimentIn): Experiment to be added

        Returns:
            Result of request as experiment object
        """
        node_response_experiment = self.graph_api_service.create_node("Experiment")

        if node_response_experiment["errors"] is not None:
            return ExperimentOut(experiment_name=experiment.experiment_name, errors=node_response_experiment["errors"])

        experiment_id = node_response_experiment["id"]
        properties_response = self.graph_api_service.create_properties(experiment_id, experiment)
        if properties_response["errors"] is not None:
            return ExperimentOut(experiment_name=experiment.experiment_name, errors=properties_response["errors"])

        authors_out = []
        if experiment.authors is not None:
            # Create Nodes Author for experiment
            for author in experiment.authors:
                node_response_author = self.author_service.save_author(author=author)
                # Create relationship between Author and Experiment
                relationship_response_experiment_author = self.graph_api_service.create_relationships(
                    end_node=node_response_author.id, start_node=experiment_id, name="hasAuthor")
                if relationship_response_experiment_author["errors"] is not None:
                    return ExperimentOut(experiment_name=experiment.experiment_name, authors=experiment.authors,
                                         errors=relationship_response_experiment_author["errors"])
                authors_out.append(node_response_author)

        publication_out = None
        if experiment.publication is not None:
            # Create Node Publication for experiment
            publication_out = self.publication_service.save_publication(publication=experiment.publication)
            # Create relationship between Publication and Experiment
            relationship_response_experiment_publication = self.graph_api_service.create_relationships(
                end_node=publication_out.id, start_node=experiment_id, name="hasPublication")
            if relationship_response_experiment_publication["errors"] is not None:
                return ExperimentOut(experiment_name=experiment.experiment_name, publication=experiment.publication,
                                     errors=relationship_response_experiment_publication["errors"])

        return ExperimentOut(experiment_name=experiment.experiment_name, authors=authors_out,
                             publication=publication_out, abstract=experiment.abstract, id=experiment_id,
                             additional_properties=experiment.additional_properties)
