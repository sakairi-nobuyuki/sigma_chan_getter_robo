# coding: utf-8

import pytest
import os
from pathlib import Path
from sigma_chan_getter_robo.post_process.io import S3Storage

@pytest.fixture
def mock_s3_minio():
    s3 = S3Storage("s3", "", "getter-robo", "http://localhost:9000/", "sigma-chan", "sigma-chan-dayo", "")

    return s3


@pytest.fixture
def mock_file_path():
    root_path = Path(os.path.abspath(__file__)).parent.parent.parent
    return os.path.join(root_path, "data/getter_robo/hoge.dat")
