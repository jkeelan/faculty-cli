import pytest

from test.fixtures import PROFILE


@pytest.fixture
def mock_profile(mocker):
    profile_mock = mocker.patch(
        "faculty.config.resolve_profile", return_value=PROFILE
    )
