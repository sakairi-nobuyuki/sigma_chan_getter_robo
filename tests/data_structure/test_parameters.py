# coding: utf-8

from sigma_chan_getter_robo.data_structure.parameters import Parameters


class TestParameters:
    """Test for getter-robo parameters"""

    def test_init(self, mock_parameters_dict):
        """Test initializing parameters

        Args:
            mock_parameters_dict (_type_): _description_
        """

        parameters = Parameters(**mock_parameters_dict)

        assert isinstance(parameters, Parameters)
